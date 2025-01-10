class DirectedWeightedGraphAdjMatrix:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        # Create a 2D list (matrix) initialized to infinity (inf) for weights
        self.matrix = [[float('inf')] * vertices for _ in range(vertices)]
        # Set the diagonal (self-loops) to 0 since the distance to itself is zero
        for i in range(vertices):
            self.matrix[i][i] = 0

    def add_edge(self, u, v, weight):
        # Set the weight for the edge `u -> v` in the matrix
        self.matrix[u][v] = weight

    def display(self):
        # Print the adjacency matrix row by row
        for row in self.matrix:
            print(row)
