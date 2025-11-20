AIM:
To perform Depth-First Search (DFS) on a graph by visiting nodes as deep as possible along each branch before backtracking, without using functions or modules.
program:
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    edges = input("Enter adjacent nodes separated by space: ").split()
    graph[node] = edges

start = input("Enter starting node: ")

stack = [start]
visited = []

while stack:
    node = stack.pop()
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbor in reversed(graph[node]):
            stack.append(neighbor)
