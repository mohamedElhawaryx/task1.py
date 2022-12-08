
graph ={
    'a':[('b',6),('f',3)],
    'b':[('a',6),('d',2),('c',3)],
    'c':[('b',3),('d',1),('e',5)],
    'd':[('b',2),('c',1),('e',8)],
    'e':[('c',5),('d',8),('j',5), ('i',5)],
    'f':[('a',3),('g',1),('h',3)],
    'g':[('f',1),('i',3)],
    'h':[('f',7),('i',2)],
    'i':[('g',3),('e',5),('j',3),('h',2)],
    'j':[('i',3),('e',5)]
    }
hurestic= {
    'a':10,
    'b':8,
    'c':5,
    'd':7,
    'e':3,
    'f':6,
    'g':5,
    'h':3,
    'i':1,
    'j':0
}
def path_f_cost (path):#cost function
    g_cost = 0
    for (node, cost) in path:
        g_cost +=cost#adding the city distance and the initial distance
    lat_node =path[-1][0]
    h_cost =hurestic[lat_node]
    f_cost =g_cost+h_cost#adding path distance and the estimated distance
    return f_cost

def a_search (graph,start, goal):#crate the search function
    queue = [[(start, 0)]]
    visted= []
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)#popping the last city entered the queue
        node =path[-1][0]
        if node in visted:#check if the city is visited
            continue
        visted.append(node)
        if node == goal:#check if it is the goal
            return path# if it is   the goal return the path
        else:#if it is not the goal   do
            adjacent_node = graph.get(node, [])
            for (node, cost) in adjacent_node:
                new_path = path.copy()
                new_path.append((node, cost))#adding the neibours with costs
                queue.append(new_path)#add new cities to the queue

print(a_search(graph, 'a', 'j'))








