import ast
queue = []
visited = []
def bfs(node,graph,visited): #bfs function
    visited.append(node)
    queue.append(node)
    while queue: #making loop to visite each loop and put in frontier
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)#mark to be visited
                queue.append(neighbour)#adding the neibour to the queue

file = open('BFS.txt','r')
data = file.read()
d = ast.literal_eval(data)
file.close()
bfs('5',d,visited)









