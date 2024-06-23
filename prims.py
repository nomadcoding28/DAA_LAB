# import heapq
# def prims(graph,start_node):
#     mst = []
#     visited = set([start_node])
#     edges = [(weight, start_node, to) for to, weight in graph[start_node].items()]
#     heapq.heapify(edges)

#     while edges:
#         weight, frm, to = heapq.heappop(edges)
#         if to not in visited:
#             visited.add(to)
#             mst.append((weight, frm, to))
#             for to_next, weight in graph[to].items():
#                 if to_next is not visited:
#                     heapq.heappush(edges, (weight, to, to_next))
#     return mst
# graph = {
#     "A": {"B": 1, "C": 4},
#     "B": {"A": 1, "C": 2, "D": 5},
#     "C": {"A": 4, "B": 2, "D": 1},
#     "D": {"B": 5, "C": 1},
# }
# start_node = "A"
# mst = prims(graph,start_node)
# print(mst)
import heapq

def prim(graph, start_node):
    mst = []
    visited = set([start_node])
    edges = [(weight, start_node, to) for to, weight in graph[start_node].items()]
    heapq.heapify(edges)
    
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            
            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))
    
    return mst

# Function to take user input and create the graph
def create_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        graph[node] = {}
        m = int(input(f"Enter the number of edges from {node}: "))
        for _ in range(m):
            to = input(f"Enter the destination node from {node}: ")
            weight = int(input(f"Enter the weight of edge {node}-{to}: "))
            graph[node][to] = weight
    return graph

# Main program to execute the algorithm
def main():
    graph = create_graph()
    start_node = input("Enter the start node: ")
    mst = prim(graph, start_node)
    print("MST using Prim's Algorithm:", mst)

if __name__ == "__main__":
    main()

