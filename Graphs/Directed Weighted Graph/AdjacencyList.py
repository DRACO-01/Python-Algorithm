class DirectedWeightedGraphAdjList:
    def __init__(self):
        self.graph = {}  # Dictionary to store adjacency list for the graph

    def add_edge(self, u, v, weight):
        # If the vertex `u` is not already in the graph, add it with an empty list
        if u not in self.graph:
            self.graph[u] = []
        # Add the edge with its weight in the format (v, weight)
        self.graph[u].append((v, weight))

    def display(self):
        # Print each node and its list of neighbors with weights
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
