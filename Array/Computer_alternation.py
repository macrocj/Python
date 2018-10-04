#Author: JC
#Date: 7/19/2018
#Version: 1.0

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2]= sorted(A[i:i+2], reverse = i%2)
        print(A[i:i+2])
    print(A)
A=[7,3,5,4,6,2,9,1]
rearrange(A)