
    
class Vertex:
    """
    Represents a vertex (node) in a graph.
    """

    def __init__(self, value):
        """
        Initialize a vertex with the given value.
        
        Args:
        - value: The value associated with the vertex.
        """
        self.value = value

    def __str__(self):
        """
        Get a string representation of the vertex.
        
        Returns:
        - A string representation of the vertex's value.
        """
        return str(self.value)
    

class Edge:
    """
    Represents an edge between two vertices in a graph.
    """

    def __init__(self, vertex, weight=0):
        """
        Initialize an edge with the specified destination vertex and optional weight.
        
        Args:
        - vertex: The destination vertex of the edge.
        - weight: The weight/cost associated with the edge (default is 0).
        """
        self.vertex = vertex
        self.weight = weight


class Graph:
    """
    Represents a graph using an adjacency list.
    """

    def __init__(self):
        """
        Initialize an empty graph with an empty adjacency list.
        """
        self.__adj_list = {}


    def add_vertex(self, value):
        """
        Add a vertex with the given value to the graph.
        
        Args:
        - value: The value associated with the vertex.
        
        Returns:
        - The newly created vertex.
        """
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    

    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        if start_vertex == end_vertex :
            edge1 = Edge(end_vertex, weight)
            self.__adj_list[start_vertex].append(edge1)
            return 
        
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)


    def get_vertices(self):
      '''
        Arguments: none
        Returns all of the vertices in the graph as a  
        collection (set, list, or similar)
        Empty collection returned if there are no vertices
      '''
  
      return self.__adj_list.keys()
    

    def size(self):
      return len(self.__adj_list)
    


    def get_neighbors(self,vertex):
      '''
      get neighbors
      A rguments: vertex
      Returns a collection of edges connected to the 
      given vertex
      Include the weight of the connection in the returned collection
      Empty collection returned if there are no vertices
      '''
      return self.__adj_list.get(vertex, [])
    

    def depth_first(self, start_vertex):
        """
        This method explores the graph in a depth-first manner, visiting vertices as deeply as
        possible along each branch before backtracking. It returns a list of vertex values in
        the order they are visited during the traversal.
        
        Args:
        - start_vertex: The vertex from which to start the depth-first traversal.
        
        Returns:
        - A list containing the values of vertices visited in depth-first order.
        """
        result = []
        visited = set()
        
        def helper(vertex):
            if vertex not in visited:
                result.append(vertex.value)
                visited.add(vertex)
                for edge in self.get_neighbors(vertex):
                    neighbor = edge.vertex
                    helper(neighbor)
        
        helper(start_vertex)
        return result








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

    print(g.depth_first(c))

        


