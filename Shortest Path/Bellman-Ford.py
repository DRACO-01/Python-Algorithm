def bellman_ford(graph, start):
    """
    Implements the Bellman-Ford algorithm to find the shortest paths from a start node to all other nodes in a graph.

    :param graph: A dictionary representing the graph as an adjacency list.
                  Keys are nodes, and values are lists of tuples (neighbor, weight).
    :param start: The starting node for the algorithm.
    :return: A tuple containing a dictionary of shortest distances and a boolean indicating if a negative cycle exists.
    """
    # Initialize distances from the start node to all other nodes as infinity.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to the start node is 0.

    # Number of nodes in the graph.
    num_nodes = len(graph)

    # Relax edges up to (num_nodes - 1) times.
    for _ in range(num_nodes - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                # Relax the edge if a shorter path is found.
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative-weight cycles.
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                return distances, True  # Negative cycle detected.

    return distances, False  # No negative cycle detected.

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list.
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', -3), ('D', 2)],
        'C': [('D', 3)],
        'D': []
    }

    # Find the shortest paths from node 'A'.
    start_node = 'A'
    shortest_distances, has_negative_cycle = bellman_ford(graph, start_node)

    if has_negative_cycle:
        print("The graph contains a negative-weight cycle.")
    else:
        print("Shortest distances from node", start_node, ":", shortest_distances)
