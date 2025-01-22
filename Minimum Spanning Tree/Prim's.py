# Prim's Algorithm
def prim(graph, start):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    :param graph: A dictionary representing the graph as an adjacency list.
    :param start: The starting node for the algorithm.
    :return: The MST as a list of edges and its total weight.
    """
    import heapq

    # Priority queue to select the smallest edge.
    priority_queue = []

    # Add all edges from the start node to the priority queue.
    for neighbor, weight in graph[start]:
        heapq.heappush(priority_queue, (weight, start, neighbor))

    visited = set()
    visited.add(start)
    mst = []
    total_weight = 0

    while priority_queue:
        # Get the edge with the smallest weight.
        weight, node1, node2 = heapq.heappop(priority_queue)

        if node2 not in visited:
            visited.add(node2)
            mst.append((node1, node2, weight))
            total_weight += weight

            # Add all edges from the newly added node to the queue.
            for neighbor, w in graph[node2]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (w, node2, neighbor))

    return mst, total_weight

# Example usage
if __name__ == "__main__":

        # Graph for Prim's algorithm.
    graph_prim = {
        'A': [('B', 1), ('C', 5)],
        'B': [('A', 1), ('C', 4), ('D', 2)],
        'C': [('A', 5), ('B', 4), ('D', 6)],
        'D': [('B', 2), ('C', 6), ('E', 3)],
        'E': [('D', 3)]
    }
    mst_prim, weight_prim = prim(graph_prim, 'A')
    print("Prim's MST:", mst_prim, "with total weight", weight_prim)
# Output: Prim's MST: [('A', 'B', 1), ('B', 'D', 2), ('D', 'E', 3), ('B', 'C', 4)] with total weight 10