from graph.graph import Graph,Vertex,Edge,Queue

def test_vertex_added():
    vertex = Vertex("A")
    assert vertex.value == "A"

def test_edge_added():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    graph.add_edge(vertex1,vertex2)
    neighbors =graph.get_neighbors(vertex1)
    # print(neighbors.vertex)
    assert neighbors[0].vertex == vertex2

def test_collection_of_all_vertices():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    vertices = graph.get_vertices()
    assert vertices == {vertex1, vertex2}

def test_get_neighbors():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    vertex3 = graph.add_vertex("C")
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex1, vertex3)
    neighbors_of_vertex1 = graph.get_neighbors(vertex1)
    assert len(neighbors_of_vertex1) == 2
    neighbor_values = {edge.vertex.value for edge in neighbors_of_vertex1}
    assert neighbor_values == {"B", "C"}


def test_get_neighbors_with_weight():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    vertex3 = graph.add_vertex("C")
    graph.add_edge(vertex1, vertex2, weight=3)
    graph.add_edge(vertex1, vertex3, weight=5)
    neighbors_of_vertex1 = graph.get_neighbors(vertex1)
    assert len(neighbors_of_vertex1) == 2
    neighbors_info = {(edge.vertex.value, edge.weight) for edge in neighbors_of_vertex1}
    assert neighbors_info == {("B", 3), ("C", 5)}

def test_proper_size():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    vertex3 = graph.add_vertex("C")
    assert graph.size() == 3

def test_graph_with_one_vertex_and_edge():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    graph.add_edge(vertex1, vertex1)
    neighbors_of_vertex1 = graph.get_neighbors(vertex1) 
    assert len(neighbors_of_vertex1) == 1
    assert neighbors_of_vertex1[0].vertex == vertex1







