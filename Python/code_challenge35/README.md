# Code Challenge: Class 35
# Graph


## Approach & Efficiency


**Adding a Vertex**
The add_vertex() method is O(1), and the space complexity is also O(1), as it only requires memory for the new vertex object and the adjacency list entry.

**Adding an Edge**
The add_edge() the time complexity is O(1). The space complexity is also O(1), as it only requires memory for the new edge objects.

**Getting Vertices**
The get_vertices() The time complexity is O(V), where V is the number of vertices in the graph. The space complexity is O(V), as the method returns a collection of vertex objects.

**Getting Vertex Neighbors**
The get_neighbors() The time complexity is O(1) on average because dictionary access and list retrieval are constant-time operations. The space complexity is O(E), where E is the number of edges connected to the vertex.

**Breadth-First Traversal**
The breadth_first() The time complexity of the traversal is O(V + E), where V is the number of vertices and E is the number of edges in the graph. The space complexity is O(V), as it requires memory for the queue and the visited set.

**Graph Size**
The size() the time complexity is O(1), and the space complexity is O(1).

## Solution
python Python/code_challenge35/graph/graph.py     

```python
if __name__ == "__main__":
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    e = g.add_vertex('E')
    c = g.add_vertex('C')
    d = g.add_vertex('D')

    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
    print(g.breadth_first(a))
```