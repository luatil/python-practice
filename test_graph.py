import pytest

from graph import Graph

def test_degree():
    test_graph = Graph()
    test_graph.set_vertices({1, 2, 3, 4})
    test_graph.set_edges({(1, 2), (3, 4), (3, 1)})
    assert test_graph.degree(1) == 2

def test_is_graph_connected():
    test_graph = Graph()
    test_graph.set_vertices({1, 2, 3, 4})
    test_graph.set_edges({(1, 2), (3, 4), (3, 1)})
    assert test_graph.is_graph_connected(1) == True

def test_is_graph_connected_disconnected_graph():
    test_graph = Graph()
    test_graph.set_vertices({1, 2, 3, 4})
    test_graph.set_edges({(1, 2), (3, 4)})
    assert test_graph.is_graph_connected(1) == False

