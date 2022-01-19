import pytest
from graph.graph import Graph, Vertex

# Node can be successfully added to the graph

def test_add_node():

    graph = Graph()
    expected = "spam"  # a vertex's value that comes back
    added_vertex = graph.add_node("spam")
    actual = added_vertex.value
    assert actual == expected


def test_size_empty():

    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected

# An empty graph properly returns null

def test_get_nodes_empty():

    graph = Graph()
    expected = []
    actual = graph.get_nodes()
    assert actual == expected

# The proper size is returned, representing the number of nodes in the graph

def test_size():

    graph = Graph()
    graph.add_node("first")
    expected = 1
    actual = graph.size()
    assert actual == expected

# A collection of all nodes can be properly retrieved from the graph

def test_get_nodes():

    graph = Graph()
    one = graph.add_node("one")
    two = graph.add_node("two")
    loner = Vertex("loner")
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected

# An edge can be successfully added to the graph

def test_add_edge_simple():
    g = Graph()
    one = g.add_node("one")
    two = g.add_node("two")
    g.add_edge(one, two, 5)
    assert True

# All appropriate neighbors can be retrieved from the graph


def test_add_edge_with_neighbors():
    g = Graph()
    first = g.add_node("one")
    second = g.add_node("two")
    g.add_edge(first, second, 20)

    neighbors = g.get_neighbors(first)
    assert len(neighbors) == 1
    edge = neighbors[0]
    assert edge.vertex == second
    assert edge.weight == 20


def test_bouquet():
    g = Graph()
    first = g.add_node("one")
    g.add_edge(first, first, 10)
    neighbors = g.get_neighbors(first)
    assert len(neighbors) == 1
    edge = neighbors[0]
    assert edge.vertex == first
    assert edge.weight == 10



def test_add_edge_interloper_start():

    graph = Graph()
    start = Vertex("start")
    end = graph.add_node("end")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()
    end = Vertex("end")
    start = graph.add_node("start")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# Neighbors are returned with the weight between nodes included

def test_get_neighbors_weight():

    graph = Graph()
    first = graph.add_node("one")
    second = graph.add_node("two")
    graph.add_edge(second, first, 10)
    neighbors = graph.get_neighbors(second)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[0]
    assert neighbor_edge.vertex.value == "one"
    assert neighbor_edge.weight == 10