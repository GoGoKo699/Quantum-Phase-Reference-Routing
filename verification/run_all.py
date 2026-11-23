from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import prod

from k44 import check_k44


def charge_sectors(edges, vertices):
    sectors = defaultdict(list)
    for directions in product((0, 1), repeat=len(edges)):
        charge = [0] * vertices
        for edge, direction in zip(edges, directions):
            charge[edge[direction]] += 1
        sectors[tuple(charge)].append(directions)
    return sectors


def components(edges, directions, vertices):
    outgoing = [set() for _ in range(vertices)]
    for edge, direction in zip(edges, directions):
        outgoing[edge[1 - direction]].add(edge[direction])

    reached = []
    for vertex in range(vertices):
        closure = {vertex}
        frontier = [vertex]
        while frontier:
            new = outgoing[frontier.pop()] - closure
            closure.update(new)
            frontier.extend(new)
        reached.append(closure)
    return tuple(min(u for u in reached[v] if v in reached[u]) for v in range(vertices))


def check_orientation_factorization():
    count = 0
    for vertices in range(2, 6):
        possible = list(combinations(range(vertices), 2))
        for size in range(len(possible) + 1):
            for edges in combinations(possible, size):
                for members in charge_sectors(edges, vertices).values():
                    count += 1
                    labels = components(edges, members[0], vertices)
                    assert all(components(edges, x, vertices) == labels for x in members)
                    # Every edge joining different SCCs is fixed in this sector.
                    assert all(len({x[i] for x in members}) == 1
                               for i, (u, v) in enumerate(edges) if labels[u] != labels[v])
                    # The class is the Cartesian product of within-SCC orientation choices.
                    local = [[i for i, (u, v) in enumerate(edges)
                              if labels[u] == labels[v] == label] for label in set(labels)]
                    assert len(members) == prod(len({tuple(x[i] for i in block) for x in members})
                                               for block in local)
    return count


def theta(lengths, left, right, first_free):
    edges = []
    for length in lengths:
        path = [left, *range(first_free, first_free + length - 1), right]
        edges.extend(zip(path, path[1:]))
        first_free += length - 1
    return edges, first_free


def prediction(lengths):
    h = [Fraction(1, 2 ** (length - 1)) for length in lengths]
    return 1 - 2 * prod(1 - x / 2 for x in h) + prod(1 - x for x in h)


def scc_probability(edges, vertices, left, right):
    successful = 0
    for orientations in charge_sectors(edges, vertices).values():
        labels = components(edges, orientations[0], vertices)
        if labels[left] == labels[right]:
            successful += len(orientations)
    return Fraction(successful, 2 ** len(edges))


def check_theta_and_chain():
    studied = 0
    for paths in range(1, 5):
        for lengths in product((1, 2, 3), repeat=paths):
            edges, vertices = theta(lengths, 0, 1, 2)
            assert scc_probability(edges, vertices, 0, 1) == prediction(lengths)
            studied += 1
    for modules in [((1, 2), (2, 3)), ((2, 2, 2), (1, 3), (2, 2))]:
        first_free = len(modules) + 1
        edges = []
        for index, lengths in enumerate(modules):
            extra, first_free = theta(lengths, index, index + 1, first_free)
            edges.extend(extra)
        assert scc_probability(edges, first_free, 0, len(modules)) == prod(map(prediction, modules))
    return studied


def check_strict_scc_example():
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 0)]
    sectors = charge_sectors(edges, 4)
    favorable = [orientations for orientations in sectors.values()
                 if components(edges, orientations[0], 4)[2]
                 == components(edges, orientations[0], 4)[3]]
    assert len(favorable) == 2
    optimal_weight = Fraction(0)
    edge_indices = [i for i, edge in enumerate(edges) if 2 in edge]
    for sector in favorable:
        assert len(sector) == 3
        counts = Counter(tuple(x[i] for i in edge_indices) for x in sector)
        assert sorted(counts.values()) == [1, 2]
        optimal_weight += Fraction(len(sector), 2 ** len(edges)) * Fraction(2, 3)
    assert scc_probability(edges, 4, 2, 3) == Fraction(3, 16)
    assert optimal_weight == Fraction(1, 8)


def check_pooling_measurements():
    sectors = 0
    biggest_outcome_count = 0
    for active in range(2, 6):
        for charge in range(1, active):
            patterns = [frozenset(s) for s in combinations(range(active), charge)]
            outcomes = [(s, t) for s, t in combinations(patterns, 2) if len(s ^ t) == 2]
            counts = Counter(s for pair in outcomes for s in pair)
            assert all(counts[s] == charge * (active - charge) for s in patterns)
            biggest_outcome_count = max(biggest_outcome_count, len(outcomes))
            sectors += 1
    assert biggest_outcome_count == 30
    return sectors


def check_mesh_and_decoder():
    assert prediction((2,) * 4) == Fraction(55, 128)
    assert prediction((2,) * 5) == Fraction(285, 512)

    def probability(s):
        active = s * s / 2
        return 1 - 2 * (1 - active / 2) ** 5 + (1 - active) ** 5

    assert probability(Fraction(95559851, 10**8)) < Fraction(1, 2)
    assert probability(Fraction(95559852, 10**8)) > Fraction(1, 2)
    for copies in (3, 5, 7, 11):
        for error in product((0, 1), repeat=copies):
            syndrome = (0,) + tuple(error[0] ^ b for b in error[1:])
            correct_first = int(sum(syndrome) > copies // 2)
            assert (error[0] ^ correct_first) == int(sum(error) > copies // 2)


if __name__ == '__main__':
    print('orientation charge sectors verified:', check_orientation_factorization())
    print('parallel-path cases verified:', check_theta_and_chain())
    print('serial test cases verified: 2')
    check_strict_scc_example()
    print('strict graph bound: 3/16, exact optimum: 1/8')
    print('endpoint pooling charge sectors verified:', check_pooling_measurements())
    check_mesh_and_decoder()
    print('mesh threshold and four repetition decoders verified')
    check_k44()
