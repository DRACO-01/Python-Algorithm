class DirectedGraphAdjList:
    def __init__(self):
        self.graph = {}  # Dictionary to store adjacency list for the graph

    def add_edge(self, u, v):
        # If the vertex `u` is not already in the graph, add it with an empty list
        if u not in self.graph:
            self.graph[u] = []
        # Add the edge only in one direction (u -> v)
        self.graph[u].append(v)

    def display(self):
        # Print each node and its list of neighbors
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
