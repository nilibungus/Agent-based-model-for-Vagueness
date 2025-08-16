import pytest
from Vaguenessbaldings import sym_closure, villagedistributer, totalagentsmaker, rewiring_ring_lattice, make_ring_lattice, makesmallworldnetworksinvillages, findneighbours, findallneighbours, beliefassignment, weight_assignment, update_beliefs_with_degroot, update_beliefs_with_degroot_multiple_times

def test_findallneighbours():
    data = findallneighbours(makesmallworldnetworksinvillages( villagedistributer(5, totalagentsmaker(20)), 3, 0.8))
    firstelements = [lst[0] for lst in data]
    assert len(firstelements) == len(set(firstelements))

    norepeat_data = []
    for lst in data:
        if lst not in norepeat_data:
            norepeat_data.append(lst)


    assert len(data) == len(norepeat_data)

def test_weight_assignment():
    for i in range(100):
        assert sum(weight_assignment(20)) == pytest.approx(1)
        i += 1


def test_update_beliefs_with_degroot():
    beliefs = {0: [0.5081031241037909], 1: [0.5054052958447789], 2: [0.5011797250808843], 3: [0.5066469437571604], 4: [0.5076739466861437], 5: [0.5030920085444808], 6: [0.5045398713117496], 7: [0.5028902373857259], 8: [0.5041003848141513], 9: [0.5058237019741115]}

    allneighbours = [[0, 1, 6], [1, 2, 0], [2, 4, 1], [4, 6, 2], [6, 0, 4], [3, 5, 9], [5, 7, 3], [7, 8, 5], [8, 9, 7], [9, 3, 8]]
    res = update_beliefs_with_degroot(allneighbours, beliefs)
    for i in range(1, 4):
        assert len(res[i]) == 2
        i += 1
    for i in range(1, 4):
        for j in range(1):
            assert 0 <= res[i][j] <= 1

def test_update_beliefs_with_degroot_multiple_times():
    beliefsdictionary = update_beliefs_with_degroot_multiple_times(50, findallneighbours(makesmallworldnetworksinvillages(villagedistributer(5, totalagentsmaker(20)), 2, 0.6)), beliefassignment(0.7, 0.01, totalagentsmaker(20)))
    for i in range(20):
        assert len(beliefsdictionary[i]) == 51

def test_beliefassignment():
    agents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rabo = beliefassignment(0.5, 0.01, agents)
    for i in range (1, 10):
        assert len(rabo[i]) == 1

def test_findneighbours():
    lst = [(0, 4), (4, 6), (6, 8), (8, 9), (9, 0), (4, 0), (6, 4), (8, 6), (9, 8), (0, 9)]
    assert findneighbours(0, lst) == [0, 4, 9]
    assert findneighbours(4, lst) == [4, 6, 0]

def test_make_ring_lattice():
    lst = [1,2,3,4]
    ring_lattice = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 1), (3, 2), (4, 3), (1, 4)]
    made_ring_lattice = make_ring_lattice(lst, 2)
    assert set(ring_lattice) == set(made_ring_lattice)

def far_apart_edges(lst, n):
    far_apart = []
    for edge in lst:
        if edge not in far_apart and (edge[0] >= edge[1] + n or edge[1] >= edge[0] + n):
            far_apart.append(edge)
    return far_apart


def test_rewiring_ring_lattice():
    ring_lattice = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 1), (3, 2), (4, 3), (1, 4)]
    nodes = [1,2,3,4]
    assert len(far_apart_edges(rewiring_ring_lattice(ring_lattice, 0.9, nodes), 3)) == len(far_apart_edges(rewiring_ring_lattice(ring_lattice, 0.1, nodes), 3))

def test_makesmallworldnetworksinvillages():
    lst = [[5, 15, 16, 4, 11], [19, 7, 8, 13, 1], [17, 18, 3, 9, 12], [6, 2, 10, 0, 14]]
    assert len(makesmallworldnetworksinvillages(lst, 2, 0.5)) == len(lst)

def test_totalagentsmaker():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert totalagentsmaker(10) == lst

def test_villagedistributer():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert len(villagedistributer(2, lst)) == 2

def test_sym_closure():
    lst = [(1, 2), (2, 3)]
    assert set(sym_closure(lst)) == set([(1, 2), (2, 3), (2, 1), (3, 2)])



