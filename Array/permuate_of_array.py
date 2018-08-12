#Author: JC
#Date: 7/23/2018
#Version: 1.0

import time

def timeout(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("The processing time is using ", end - start)
    return wrapper

@timeout
def apply_permutation(perm, A):
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]
    print(perm, A)

A = [1,3,0,2]
apply_permutation([2,0,3,1 ],A)

@timeout
def apply_permutation_adv(perm, A):
    def cyclic_permutation(start, perm, A):
        i, temp = start, A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break
    for i in range(len(A)):
        j = perm[i]
        while j!= i:
            if j < i:
                break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)
            print(perm, "output is ", A)

A = [1,3,0,2]
apply_permutation_adv([2,0,3,1 ],A)

def try_permutation(perm,A):
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]