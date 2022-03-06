def find(l, node):
    if l[node]<0:
        return node
    else:
        temp = find(l,l[node])
        l[node]= temp
        return temp


def union(l, a, b, ans):
    ta = a
    tb = b
    a = find(l, a)
    b = find(l, b)
    if a == b:
        pass
    else:
        ans.append([a,b])
        if l[a] == l[b]:
            l[a] = l[a] + l[b]
            l[b] = a
        else:
            if l[a] < l[b]:
                l[a] = l[a] + l[b]
                l[b] = a
            else:
                l[b] = l[a] + l[b]
                l[a] = b


# graph hardcoding
graph = [[1,2,1], [3,4,1], [3,6,2], [6,7,2], [1,3,3], [2,6,4], [4,5,5], [6,5,6], [7,5,7]]
n = 7  # 7 vertices
ans = []
# we need to sort the distances from smaller to larger so we need to use key and lambda function
graph = sorted(graph, key= lambda graph:graph[2])
l = [-1] * (n+1)
for u,v,d in graph:
    union(l,u,v,ans)
for i in ans:
    print(i)
