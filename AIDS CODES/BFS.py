from queue import Queue
# the adjacent list changes from graph to graph
adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G"]
}

# BFS CODE

visited = {}               # we will keep track of all the nodes we visit
level = {}              # to keep track of the level while traversing we use this
parent = {}           # we use parent empty dictionary to calculate the distance from source or parent node
bfs_traversal_ouput = []     # we use an empty list to store the order of nodes
queue = Queue()           # create an empty queue

for node in adj_list.keys():           # the initialisation part of all the nodes present in the graph to activate
    visited[node] = False
    parent[node] = None
    level[node] = -1

# algorithm part
s = "A"              # source node
visited[s] = True
level[s] = 0
queue.put(s)         # we place the source node in the queue

# we iterate a and add elements to the queue until its empty

while not queue.empty():               # our algorithm is to pop the leftmost element of the queue
    u = queue.get()           # it will pop the first element of the queue
    bfs_traversal_ouput.append(u)

    for v in adj_list[u]:             # we need to explore all the adjacent vertex of u
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)

print(bfs_traversal_ouput)          # the order which we will visit.
print(level)                # to know the shortest distance from the source vertex

# Shortest path of from any node from source node
v = "D"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()          # we get the path in the reversed order from parent so we use reverse
print(path)

