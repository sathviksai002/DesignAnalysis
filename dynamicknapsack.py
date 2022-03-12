# v values of the items- list, w is the weight of the items- list, c is the capacity knapsack - individual component
def knapsack(v, w, C):
    N = len(v)   # to compute the number of items that are present
    m = {}
    for c in range(C+1):
        m[(0,c)] = 0     # we initialise the value functions m(0,c) to 0 each for c
    print(m)

    for i in range(1, N+1): # from starting to all the items considering
        for c in range(C+1):    # considering all the capacity utmost
            if w[i-1] <= c:
                m[(i, c)] = max(m[(i-1, c)], v[i-1] + m[(i-1, c-w[i-1])])
            else:
                m[(i, c)] = m[(i-1, c)]
            # print((m[i,c]))

    return m[(N,C)]


v=[int(x) for x in input().split()]
w=[int(y) for y in input().split()]
C = int(input())
print("The maximum capacity is:", knapsack(v,w,C))
