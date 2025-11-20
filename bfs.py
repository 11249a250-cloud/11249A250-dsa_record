AIM:
To perform Breadth-First Search (BFS) on a graph by visiting all nodes level by level starting from a given source node without using functions or modules.
program:
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    edges = input("Enter adjacent nodes separated by space: ").split()
    graph[node] = edges

start = input("Enter starting node: ")

queue = [start]
visited = []

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            queue.append(neighbor)
