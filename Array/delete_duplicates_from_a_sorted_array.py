#Author: JC
#Date: 7/17/2018
#Version: 1.0

def delete_dup(A):
    if not A:
        return 0
    write_index= 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    print(A)
    return write_index

A = [2,3,5,7,7,11,11,11,11,11,13]
#print(delete_dup(A))

def try_delete_dup(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index -1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index
#print(try_delete_dup((A)))

def remove_dup(A):
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    print(write_index)
    print(A)
print(A)
remove_dup(A)
