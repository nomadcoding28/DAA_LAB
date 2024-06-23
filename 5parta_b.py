# def dfs(maze,start,goal):
#     visited=set()
#     stack=[start]
#     while stack:
#         current_node=stack.pop()
#         if current_node==goal:
#             return True
#         else:
#             visited.add(current_node)
#         for neighbour in maze[current_node]:
#             if neighbour not in visited:
#                 stack.append(neighbour)
#     return False
# maze = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# start = 'A'
# goal = 'F'

# # Run the DFS algorithm
# found_cheese = dfs(maze, start, goal)
# if found_cheese:
#     print("Cheese found!")
# else:
#     print("Cheese not found.")

from collections import deque


def bfs_check_bipartite(graph, start):
    queue = deque([(start, 0)])  # (node, level)
    visited = set()
    colors = {}  # node: color

    while queue:
        current_node, level = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            # Color the node: Red for odd levels, Blue for even levels
            colors[current_node] = "Red" if level % 2 != 0 else "Blue"

            for neighbor in graph[current_node]:
                if neighbor in colors:
                    # Check for a coloring conflict
                    if colors[neighbor] == colors[current_node]:
                        return False, {}  # Graph is not bipartite
                else:
                    queue.append((neighbor, level + 1))

    return True, colors  # Graph is bipartite and colors is the color mapping


# Example graph represented as an adjacency list
graph1 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
graph = {
    "A": ["1", "2"],
    "B": ["1", "3"],
    "C": ["2", "3"],
    "1": ["A", "B"],
    "2": ["A", "C"],
    "3": ["B", "C"],
}

start_node = "A"
is_bipartite, colors = bfs_check_bipartite(graph, start_node)

if is_bipartite:
    print("The graph is bipartite.")
    print("Node colors:", colors)
else:
    print("The graph is not bipartite.")
