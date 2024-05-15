import numpy as np

class DirectedGraph:
    def __init__(self, num_vertices):

        self.num_vertices = num_vertices
        self.adjacency_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    def add_edge(self, u, v):

        if u >= self.num_vertices or v >= self.num_vertices or u < 0 or v < 0:
            print("Vertex number is out of the allowed range")
            return
        
        self.adjacency_matrix[u][v] = 1 #for multi-graph, value >= 1.

    def in_degree(self, v):

        """Returns the in-degree of vertex v."""
        return np.sum(self.adjacency_matrix[:, v])

    def out_degree(self, v):
       
        """Returns the out-degree of vertex v."""
        return np.sum(self.adjacency_matrix[v, :])

    def display(self):

        """Display the matrix"""

        print("Adjacency Matrix:")
        print(self.adjacency_matrix)
        print()
    def check(self,vertex):
        if vertex >= self.num_vertices:
            return ValueError("Vertex doesn't exist!")

if __name__ == "__main__":
    # Create a directed graph with 5 vertices
    graph = DirectedGraph(5)
    
    # Add some directed edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    
    graph.display()
    
    # Calculate in-degree and out-degree
    while True:

        try:
            ch = int(input("Get the indegree & outdegree of a vertex, Enter the vertex (write -1 to break): "))
            if ch == -1:
                break
            graph.check(ch)  # Check if vertex exists
            print(f"\nThe in-degree of {ch} is: {graph.in_degree(ch)}")
            print(f"The out-degree of {ch} is: {graph.out_degree(ch)}\n")

        except ValueError as e:
            print(e)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
