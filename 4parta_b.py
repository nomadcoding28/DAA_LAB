import collections


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
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
print("Following is Breadth First Traversal: ")
bfs(graph, "1")

# def InsertionSort(arr):
#     for i in range(len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=key
#     return arr
# arr=[12,345,65,34,90,2,6,67]
# print(InsertionSort(arr))
