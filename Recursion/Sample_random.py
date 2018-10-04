#Author: JC
#Date: 7/26/2018
#Version: 1.0
import random
def random_sampling(K,A):
    for i in range(K):
        # Generate a random index in [i, len(A)-1]
        r = random.randint(i, len(A) - 1)
        A[i],A[r] = A[r],A[i]
    return A

A=[2,4,3,5,1,6,4]
print(random_sampling(7,A))

def random_sample(K,A):
    for i in range(K):
        r = random.randint(i,len(K)-1)
        A[i], A[r] = A[r], A[i]
    return A