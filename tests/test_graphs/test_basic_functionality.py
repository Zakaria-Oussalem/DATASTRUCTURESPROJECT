from Graphs.graphs import Vertex, Graph
import pytest
import numpy as np


# See if vertex functionality works
def test_vertex():
    v1 = Vertex(0)
    v1.add_neighbor(1)
    v1.add_neighbor(2)
    v1.add_neighbor(3)
    assert list(v1.get_nodes()) == [1, 2, 3]


@pytest.fixture
def build_graph():
    g = Graph()
    g.addEdge("Paris", "Agadir", 3.5)
    g.addEdge("Lille", "Paris", 1)
    g.addEdge("Lille", "Brussels", 2.5)
    g.addEdge("Lille", "Krakow", 2)
    g.addEdge("Lille", "Agadir", 4)
    g.addEdge("Krakow", "Canaria", 5.5)
    g.addEdge("Canaria", "Agadir", 0.5)
    return g


@pytest.fixture
def build_simple_graph():
    g = Graph()
    g.addEdge("Paris", "Agadir", 3.5)
    g.addEdge("Lille", "Paris", 1)
    g.addEdge("Lille", "Agadir", 4)

    return g


def test_graph(build_graph):

    assert list(build_graph.getVertices()) == [
        "Paris",
        "Agadir",
        "Lille",
        "Brussels",
        "Krakow",
        "Canaria",
    ]


def test_graph_Count(build_graph):
    assert build_graph.getCount() == 6


def test_Hashing(build_graph):
    assert build_graph.Hash[2] == "Lille"


def test_AdjMatrix(build_simple_graph):
    assert (
        build_simple_graph.getAdjMatrix()
        == np.array([[0, 3.5, 1], [3.5, 0, 4], [1, 4, 0]])
    ).all


def test_remove_neighbor():
    v1 = Vertex(0)
    v1.add_neighbor(1)
    v1.add_neighbor(2)
    v1.add_neighbor(3)
    v1.remove_neighbor(2)
    assert list(v1.get_nodes()) == [1, 3]


def test_remove_vertex(build_graph):
    build_graph.removeVertex("Agadir")
    assert "Agadir" not in build_graph
    assert build_graph.getCount() == 5
