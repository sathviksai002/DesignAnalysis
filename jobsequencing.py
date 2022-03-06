# the program takes the array of jobs and no of jobs to schedule by the function designed.
def jobscheduling(l, t):
    n = len(l)
    for i in range(n):
        for j in range(n-1-i):
            if l[j][2] < l[j+1][2]:
                l[j],l[j+1] = l[j+1] , l[j]

    res = [False]*t
    job = ['1']*t

    for i in range(len(l)):
        for j in range(min(t-1, l[i][1] - 1), -1, -1):
            if res[j] is False:
                res[j] = True
            job[j] = l[i][0]
            break

    print(job)


arr = [['j1',2,60], ['j2',1,100], ['j3',3,20], ['j4',2,40], ['j5',1,20]]
print("The following sequence of jobs are: ")
jobscheduling(arr, 3)
