# Code Challenge: Class 38
# graph-depth-first

## Whiteboard Process
![img1](./depth%20first.jpg)


## Approach & Efficiency

**depth_first :** 
the worst-case time complexity of the method is O(V + E), as visiting each vertex and each edge.

the space complexity of the function is O(v), where v is the number of vertices in the graph.

   
python Python/code_challenge38/graph-depth_first/graph-depth_first.py

```python
if __name__ == "__main__":
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    c = g.add_vertex('C')
    d = g.add_vertex('D')
    e = g.add_vertex('E')
    f = g.add_vertex('F')
    g_vertex = g.add_vertex('G')
    h = g.add_vertex('H')

    g.add_edge(a, b)
    g.add_edge(b, a)

    g.add_edge(b, c)
    g.add_edge(c, b)

    g.add_edge(c, g_vertex)
    g.add_edge(g_vertex,c)

    g.add_edge(a, d)
    g.add_edge(d, a)

    g.add_edge(b, d)
    g.add_edge(d, b)

    g.add_edge(d, e)
    g.add_edge(e, d)

    g.add_edge(d, h)
    g.add_edge(h, d)

    g.add_edge(d, f)
    g.add_edge(f, d)
    print(g.depth_first(a))
```