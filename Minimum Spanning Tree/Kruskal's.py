# Kruskal's Algorithm
def kruskal(graph):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    :param graph: A dictionary representing the graph with edges as (node1, node2, weight).
    :return: The MST as a list of edges and its total weight.
    """
    # Sort edges by weight.
    edges = sorted(graph['edges'], key=lambda edge: edge[2])

    # Initialize parent and rank for Union-Find.
    parent = {}
    rank = {}

    def find(node):
        # Path compression heuristic.
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        # Union by rank heuristic.
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Initialize Union-Find structure.
    for node in graph['nodes']:
        parent[node] = node
        rank[node] = 0

    mst = []
    total_weight = 0

    # Process edges in sorted order.
    for node1, node2, weight in edges:
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append((node1, node2, weight))
            total_weight += weight

    return mst, total_weight


# Example usage
if __name__ == "__main__":
    # Graph for Kruskal's algorithm.
    graph_kruskal = {
        'nodes': ['A', 'B', 'C', 'D', 'E'],
        'edges': [
            ('A', 'B', 1),
            ('A', 'C', 5),
            ('B', 'C', 4),
            ('B', 'D', 2),
            ('C', 'D', 6),
            ('D', 'E', 3)
        ]
    }
    mst_kruskal, weight_kruskal = kruskal(graph_kruskal)
    print("Kruskal's MST:", mst_kruskal, "with total weight", weight_kruskal)
# Output: Kruskal's MST: [('A', 'B', 1), ('B', 'D', 2), ('D', 'E', 3), ('B', 'C', 4)] with total weight 10