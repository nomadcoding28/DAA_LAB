from collections import defaultdict, deque

# Define the graph as an adjacency list
graph = {"A": ["B", "C"], "B": ["C", "D"], "C": ["E"], "D": ["F"], "E": [], "F": []}


def bfs(graph, source):
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


# Example usage
source_node = "A"
reachable_nodes_bfs = bfs(graph, source_node)

print("Reachable nodes from", source_node, "using BFS:", reachable_nodes_bfs)
