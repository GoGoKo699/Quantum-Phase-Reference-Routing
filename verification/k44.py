"""Exact lower and upper bounds for same-color terminals on K4,4."""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations, permutations, product


EDGES = tuple(product(range(4), range(4, 8)))
TERMINALS = {0, 1}
TERMINAL_MASK = sum(1 << vertex for vertex in TERMINALS)
NUM_ORIENTATIONS = 1 << len(EDGES)
FULL_GRAPH = NUM_ORIENTATIONS - 1


def orientation_fibers():
    charge_of = []
    fibers = defaultdict(list)
    for pattern in range(NUM_ORIENTATIONS):
        charges = [0] * 8
        for index, (left, right) in enumerate(EDGES):
            head = right if pattern & (1 << index) else left
            charges[head] += 1
        charge = tuple(charges)
        charge_of.append(charge)
        fibers[charge].append(pattern)
    return charge_of, fibers


def reachable(successors, source):
    visited = {source}
    frontier = [source]
    while frontier:
        for neighbor in successors[frontier.pop()]:
            if neighbor not in visited:
                frontier.append(neighbor)
                visited.add(neighbor)
    return visited


def same_strong_component(pattern):
    successors = [[] for _ in range(8)]
    for index, (left, right) in enumerate(EDGES):
        tail, head = (left, right) if pattern & (1 << index) else (right, left)
        successors[tail].append(head)
    return 1 in reachable(successors, 0) and 0 in reachable(successors, 1)


def cut_bounds(fibers):
    cut_masks = [
        sum(1 << index for index, (left, right) in enumerate(EDGES)
            if ((side >> left) ^ (side >> right)) & 1)
        for side in range(1 << 8) if side & TERMINAL_MASK == 1
    ]
    assert len(cut_masks) == 64

    supported = set()
    vidal_weight = 0
    strict_gap_fibers = 0
    for charge, patterns in fibers.items():
        # The strongly connected component partition is invariant in a fiber.
        if same_strong_component(patterns[0]):
            supported.add(charge)
            largest_crossing_count = max(
                max(Counter(pattern & cut for pattern in patterns).values())
                for cut in cut_masks
            )
            yield_weight = min(len(patterns), 2 * (len(patterns) - largest_crossing_count))
            vidal_weight += yield_weight
            strict_gap_fibers += yield_weight < len(patterns)
    return supported, vidal_weight, strict_gap_fibers


def cycles():
    """Represent each undirected simple cycle by its two directed patterns."""
    edge_index = {edge: index for index, edge in enumerate(EDGES)}
    for size in range(2, 5):
        for left in combinations(range(4), size):
            for right in permutations(range(4, 8), size):
                if right[0] > right[-1]:
                    continue
                for left_tail in permutations(left[1:]):
                    ordered_left = (left[0], *left_tail)
                    forward = 0
                    backward = 0
                    for index in range(size):
                        a, b = ordered_left[index], right[index]
                        c = ordered_left[(index + 1) % size]
                        forward |= 1 << edge_index[a, b]
                        backward |= 1 << edge_index[c, b]
                    yield frozenset((*left, *right)), forward, backward


def submasks(mask):
    subset = mask
    while subset:
        yield subset
        subset = (subset - 1) & mask
    yield 0


def pool_accepts(pattern, paths):
    # The two terminal rows of EDGES occupy the two low groups of four bits.
    from_zero = pattern & paths
    from_one = (pattern >> 4) & paths
    return bool(from_zero & ~from_one and from_one & ~from_zero)


def disagreement_components(differing_edges):
    components = []
    for index, (left, right) in enumerate(EDGES):
        if differing_edges & (1 << index):
            joined = {left, right}
            remaining = []
            for component in components:
                if joined & component:
                    joined |= component
                else:
                    remaining.append(component)
            components = [*remaining, joined]
    return components


def check_fixed_charge_choices(charge_of, fibers, rings):
    best = Counter(charge_of[pattern] for pattern in range(NUM_ORIENTATIONS)
                   if pool_accepts(pattern, 0b1111))
    baseline = sum(best.values())
    assert baseline == 28160

    def add_ring_choice(proposal):
        tested_edges = 0
        for _, forward, backward in proposal:
            assert not tested_edges & (forward | backward)
            tested_edges |= forward | backward
        # The tested rings have disjoint edge sets, so a sum combines their bits.
        directed_patterns = product(*((forward, backward) for _, forward, backward in proposal))
        accepted = Counter(
            charge_of[sum(fixed) | free]
            for fixed in directed_patterns
            for free in submasks(FULL_GRAPH ^ tested_edges)
        )
        for charge, count in accepted.items():
            best[charge] = max(best[charge], count)

    for ring in rings:
        if TERMINALS <= ring[0]:
            add_ring_choice((ring,))
    for first, second in combinations(rings, 2):
        first_edges = first[1] | first[2]
        second_edges = second[1] | second[2]
        if first_edges & second_edges or not first[0] & second[0]:
            continue
        if ((0 in first[0] and 1 in second[0]) or (1 in first[0] and 0 in second[0])):
            add_ring_choice((first, second))
    ring_choice_weight = sum(best.values())
    assert ring_choice_weight == 28352

    pair_supported = set()
    for charge, patterns in fibers.items():
        for first, second in combinations(patterns, 2):
            components = disagreement_components(first ^ second)
            if any(TERMINALS <= component for component in components):
                best[charge] = max(best[charge], 1 << len(components))
                pair_supported.add(charge)
    assert sum(best.values()) == ring_choice_weight
    return baseline, ring_choice_weight, pair_supported


def adaptive_ring_weight(fibers, rings):
    consecutive_rings = [
        (sum(1 << vertex for vertex in vertices), forward | backward, forward, backward)
        for vertices, forward, backward in rings
    ]

    @cache
    def available_rings(remaining):
        return tuple(ring for ring in consecutive_rings if ring[1] & remaining == ring[1])

    @cache
    def solve(remaining, patterns, components):
        paths = (remaining & 0b1111) & ((remaining >> 4) & 0b1111)
        best = sum(pool_accepts(pattern, paths) for pattern in patterns)
        if best == len(patterns):
            return best

        for vertices, ring_edges, forward, backward in available_rings(remaining):
            by_record = defaultdict(list)
            for pattern in patterns:
                measured = pattern & ring_edges
                by_record[measured].append(pattern ^ measured)
            if forward not in by_record:
                continue

            # The two directed patterns give one accepting charge record.
            # Other records each identify the entire measured ring orientation.
            good_record = by_record.pop(forward)
            assert good_record == by_record.pop(backward)
            remaining_after = remaining ^ ring_edges
            joined = vertices
            untouched = []
            for component in components:
                if joined & component:
                    joined |= component
                else:
                    untouched.append(component)
            if joined & TERMINAL_MASK == TERMINAL_MASK:
                weight = 2 * len(good_record)
            else:
                connected = tuple(sorted([*untouched, joined]))
                weight = 2 * solve(remaining_after, tuple(good_record), connected)
            weight += sum(solve(remaining_after, tuple(record), components)
                          for record in by_record.values())
            best = max(best, weight)
            if best == len(patterns):
                break
        return best

    weight = sum(solve(FULL_GRAPH, tuple(patterns), ()) for patterns in fibers.values())
    solve.cache_clear()
    return weight


def check_k44():
    charge_of, fibers = orientation_fibers()
    rings = tuple(cycles())
    assert len(rings) == 204
    assert len(fibers) == 16145

    supported, vidal_weight, strict_gap_fibers = cut_bounds(fibers)
    baseline, ring_choice_weight, pair_supported = check_fixed_charge_choices(charge_of, fibers, rings)
    assert supported == pair_supported
    assert len(supported) == 4323
    scc_weight = sum(len(fibers[charge]) for charge in supported)
    assert scc_weight == 41602
    assert vidal_weight == 37286
    assert strict_gap_fibers == 2466

    adaptive_weight = adaptive_ring_weight(fibers, rings)
    assert adaptive_weight == 28944
    assert baseline <= ring_choice_weight <= adaptive_weight <= vidal_weight <= scc_weight
    print(f"K4,4 fibers verified: {len(fibers)}, SCC-positive: {len(supported)}")
    print(f"K4,4 SCC upper: {Fraction(scc_weight, NUM_ORIENTATIONS)}, "
          f"Vidal upper: {Fraction(vidal_weight, NUM_ORIENTATIONS)}, "
          f"strict cut improvements: {strict_gap_fibers}")
    print(f"K4,4 fixed pooling lower: {Fraction(baseline, NUM_ORIENTATIONS)}, "
          f"charge-based ring-choice lower: {Fraction(ring_choice_weight, NUM_ORIENTATIONS)}, "
          f"adaptive ring lower: {Fraction(adaptive_weight, NUM_ORIENTATIONS)}")


if __name__ == "__main__":
    check_k44()
