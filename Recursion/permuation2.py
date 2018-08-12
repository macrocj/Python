#Author: JC
#Date: 7/24/2018
#Version: 1.0

def perm(A):
    if len(A) == 0:
        return []
    elif len(A) == 1:
        return [A]
    else:
        l = []
        for i in range(len(A)):
            x = A[i]
            x_next = A[:i] + A[i+1:]
            for p in perm(x_next):
                l.append([x] + p)
        return l

data = [1,2,3]
for p in perm(data):
    print(p)