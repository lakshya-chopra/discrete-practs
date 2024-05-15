from pprint import pprint
import numpy as np

class Graph:
    def __init__(self, num_vertices):

        """Initialize the graph with the number of vertices and 
        create an adjacency matrix with all values set to 0."""

        self.num_vertices = num_vertices
        self.adjacency_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    def add_edge(self, u, v, weight=1):
        """Add an edge between vertex u and vertex v with a given weight."""
        if u >= self.num_vertices or v >= self.num_vertices or u < 0 or v < 0:
            print("Vertex number is out of the allowed range")
            return
        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight  # Assuming it's an undirected graph

    def is_connected(self, u, v):
        """Check if there is a direct edge between vertex u and vertex v."""
        return self.adjacency_matrix[u][v] != 0

    def display(self):
        """Display the adjacency matrix of the graph."""
        pprint(self.adjacency_matrix.tolist())
        print()
    

if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)
    
    # Add some edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    
    # Display the adjacency matrix
    print("Graph".center(30,"="))
    print()
        
    graph.display()
    
    # Check connectivity
    print(f"Is 0 connected to 1? {graph.is_connected(0, 1)}")  # Output: True
    print(f"Is 0 connected to 2? {graph.is_connected(0, 2)}\n")  # Output: False