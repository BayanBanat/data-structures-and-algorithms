from collections import deque

class Queue:
    """
    A basic implementation of a queue using Python's deque (double-ended queue).
    
    Methods:
    - enqueue(value): Adds a value to the end of the queue.
    - dequeue(): Removes and returns the value from the front of the queue.
    - __len__(): Returns the number of elements in the queue.
    """

    def __init__(self):
        """
        Initialize an empty queue using a deque.
        """
        self.dq = deque()

    def enqueue(self, value):
        """
        Add the given value to the end of the queue.
        
        Args:
        - value: The value to be added to the queue.
        """
        self.dq.append(value)

    def dequeue(self):
        """
        Remove and return the value from the front of the queue.
        
        Returns:
        - The value removed from the front of the queue.
        """
        return self.dq.popleft()
    
    def __len__(self):
        """
        Get the number of elements in the queue.
        
        Returns:
        - The number of elements in the queue.
        """
        return len(self.dq)
    
    
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
    

    def breadth_first(self,start_vertex):
        """
        Perform breadth-first traversal starting from the given vertex and return the result.
        
        This method explores the graph in a breadth-first manner, visiting vertices level by level,
        starting from the provided start_vertex. It returns a list of vertex values in the order
        they are visited.
        
        Args:
        - start_vertex: The vertex from which to start the breadth-first traversal.
        
        Returns:
        - A list containing the values of vertices visited in breadth-first order.
        """    
        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertex)
        visted.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors =self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result


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
        


