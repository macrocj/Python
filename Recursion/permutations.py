#Author: JC
#Date: 7/24/2018
#Version: 1.0

def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return
        # Try every possibility for A{i}
        for j in range(i,len(A)):
            A[i], A[j] = A[j], A[i]
            temp1 = A
            # Generate all permuationa for A[ i + 1:]
            directed_permutations(i+ 1)
            temp2 = A
            A[i], A[j] = A[j], A[i]
            temp3 = A
    result = []
    directed_permutations(0)
    print(result)
    return result

A= [3,2,1]
permutations(A)

def permutations2(A):
    result = []
    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break
    return result