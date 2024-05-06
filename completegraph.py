from graph import Graph

class CompleteGraph(Graph) :

    def __init__(self,num_vertices):
        super().__init__(num_vertices)
    
    def is_complete(self):

        for i in self.adjacency_matrix:
            for j in i:
                if j != 1:
                    return False
        else:
            return True
            
if __name__ == "__main__":
    
    # Create a graph with 5 vertices
    graph = CompleteGraph(3)
    
    # Add some edges
    graph.add_edge(0, 0)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    graph.add_edge(1, 0)
    graph.add_edge(1, 1)
    graph.add_edge(1, 2)

    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(2, 2)

    
    # Display the adjacency matrix
    print()
    print("Graph".center(30,"="))
    print()
        
    graph.display()

    print(f"Graph is complete: {graph.is_complete()}")