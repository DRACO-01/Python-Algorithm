class UndirectedGraphAdjList:
    def __init__(self):
        self.graph = {}  # Dictionary to store adjacency list for the graph

    def add_edge(self, u, v):
        # If the vertex `u` is not already in the graph, add it with an empty list
        if u not in self.graph:
            self.graph[u] = []
        # If the vertex `v` is not already in the graph, add it with an empty list
        if v not in self.graph:
            self.graph[v] = []
        # Add the edge both ways (u -> v and v -> u) since the graph is undirected
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        # Print each node and its list of neighbors
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
