import heapq  # Importing heapq for priority queue operations

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start node to all other nodes in a graph.

    :param graph: A dictionary representing the graph as an adjacency list.
                  Keys are nodes, and values are lists of tuples (neighbor, weight).
    :param start: The starting node for the algorithm.
    :return: A dictionary of shortest distances from the start node to each node.
    """
    # Priority queue to store (distance, node) pairs. Initially contains the start node with distance 0.
    priority_queue = [(0, start)]

    # Dictionary to store the shortest known distance to each node. Initialize with infinity for all nodes.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to the start node is 0.

    # Set to track visited nodes to avoid revisiting them.
    visited = set()

    while priority_queue:
        # Pop the node with the smallest distance from the priority queue.
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the node has been visited, skip it.
        if current_node in visited:
            continue

        # Mark the node as visited.
        visited.add(current_node)

        # Update distances for each neighbor of the current node.
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update it.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list.
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }

    # Find the shortest paths from node 'A'.
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    # Print the result.
    print("Shortest distances from node", start_node, ":", shortest_distances)
