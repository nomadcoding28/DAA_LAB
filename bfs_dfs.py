import collections
def bfs(graph,root):
    visited=set()
    queue=collections.deque([root])
    visited.add(root)
    while queue:
        vertex=queue.popleft()
        print(str(vertex)+" ",end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    "1": ["2", "3"],
    "2": ["1", "3", "4", "5"],
    "3": ["1", "2", "6", "7"],
    "4": ["2", "5", "8", "9"],
    "5": ["2", "4", "9"],
    "6": ["3", "7"],
    "7": ["3", "6"],
    "8": ["4", "9"],
    "9": ["4", "5", "8", "10"],
    "10": ["9"],
}
# bfs(graph, "1")


def dfs(graph,start,cheese):
    visited=set()
    stack=[start]
    while stack:
        current_node=stack.pop(0)
        if current_node==cheese:
            return True
        else:
            visited.add(current_node)
        for neighbour in graph[current_node]:
             if neighbour not in visited:
                stack.append(neighbour)
    return False
# def generate_graph():
#     graph={}
#     n_v=int(input("enter the number of vertices:"))
#     for i in range(n_v):
#         node=input("enter node:")
#         graph[node]=[]
#         n_e=int(input(f"enter the number of edges from {node}:"))
#         for j in range(n_e):
#             dest=input(f"enter the {j+1} dest node:")
#             graph[node].append(dest)
#     return graph
# graph=generate_graph()
startnode=input("enter the start node:")
# bfs(graph,startnode)
print(dfs(graph,startnode,'10'))
