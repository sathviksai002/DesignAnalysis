adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["A", "F"],
    "D": [],
    "E": ["B", "F"],
    "F": ["C", "F"]
}

# Required Array and Dictionary
color = {}  # we keep track of the nodes if visited or not. W=not visited(initially), G=first explore B=fully explored
parent = {}   # keep track of parent
trav_time = {}   # when a node is first visited and when a node is fully visited [start,end]
dfs_traversal_output = []   # to store the output

# initialise
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

# DFS algorithm it is a recurisve algorithm so we need function
time = 0        # we need time so that we can understand whenever a node is visiting another node


def dfs_util(u):                           # recursive function
    global time                         # global usage of time
    color[u] = "G"                    # assign the first node as grey as it is just visited
    trav_time[u][0] = time             # initial time of the visited node. for start time we use [0]
    dfs_traversal_output.append(u)          # append the nodes to the list of output

    for v in adj_list[u]:                 # getting all the adjacent nodes for a source node being iterated
        if color[v] == "W":            # if not visited same as BFS
            parent[v] = u           # we assign the newly iniatited node from newly passes parent
            dfs_util(v)           # we call the function recurisvely
    color[u] = "B"                   # after completing the assinging we put it as B that full visited
    trav_time[u][1] = time           # assing the end time for the fully visited node
    time += 1                        # incrementing time after every recursive operation


dfs_util("A")              # taking the source node as A and passing it into function
print(dfs_traversal_output)
print(parent)
print(trav_time)









