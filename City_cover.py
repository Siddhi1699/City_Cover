'''
the edges of the graph represent roads while the vertices represent the crossroads. The task is to place security
cameras at the crossroads in a way that will let you see the whole city but it is desirable to use as less cameras as
possible in order to save money.
'''
import random
def edges(gr):
    e = []
    for i in gr:
        l = []
        for j in i:
            if j != 0:
                l.append(1)
            else:
                l.append(0)
        e.append(l)
    return e
def check(e1):
    c = []
    for i in range(len(e1)):
        for j in range(len(e1[0])):
            if e1[i][j] == 3 and 3 not in c:
                e1[i] = []
                c.append(3)
                break
    print(c)
    print(e1)
    return c


def generate_e1(e):
    e1 = []
    for i in range(len(e)):
        for j in range(i):
            l = []
            if e[i][j] != 0:
                l.append(i)
                l.append(j)
            if l:
                e1.append(l)
    return e1
def approx_min_cover(gr):
    e = edges(gr)
    e1 = generate_e1(e)
    c = []
    visited = []
    while any(e1):
        x = random.randint(0, len(gr) - 1)
        if x not in visited:
            visited.append(x)
            for i in range(len(e1)):
                for j in range(2):
                    if not any(e1[i]):
                        continue
                    if e1[i][j] == x:
                        e1[i] = []
                        if x not in c:
                            c.append(x)
                        break
    return c


def FindMaxLength(vc,min):
    min_vc=[]
    for j in vc:
        if len(j)<min:
            min=len(j)
    for j in vc:
        if len(j)==min:
           min_vc.append(j)
    return min, min_vc



#gr = [[0, 2, 3, 7], [2, 0, 6, 5], [3, 6, 0, 4], [7, 5, 4, 0]]
'''gr = [[0, 10, 0, 7, 0, 0], [10, 0, 0, 6, 0, 7], [0, 0, 0, 0, 8, 11], [7, 6, 0, 0, 13, 0], [0, 0, 8, 13, 0, 0],
      [0, 7, 11, 0, 0, 0]]'''
gr=[[0,2,0,2,4,0,0,0,0],[2,0,2,4,2,4,0,0,0],[0,2,0,0,4,2,0,0,0],[2,4,0,0,2,0,2,4,0],[4,2,4,2,0,2,4,2,4],[0,4,2,0,2,0,0,4,2],[0,0,0,2,4,0,0,2,0],[0,0,0,4,2,4,2,0,2],[0,0,0,0,4,2,0,2,0],]
vc = []
for _ in range(25):
    c = approx_min_cover(gr)
    c.sort()
    if c not in vc:
        vc.append(c)
min=len(gr)
print("vertex covers are:")
for i in vc:
    print(i)
min_len,min_vc=FindMaxLength(vc,min)
print("Length of Minimum vertex cover for the given city is: ",min_len)
print("Minimum vertex cover is:",*min_vc)
