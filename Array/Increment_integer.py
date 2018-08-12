############################
#Author: JC
#Date: 7 / 15 / 2018
#Version: 1.0

'''
#self try, not working, stoped at 3 digits number, works if list number less than 999
def plus_one(A):
    for i in reversed(range(len(A))):
        if A[i] == 9:
            A[i] = 0
            if A[i-1] == 9:
                A[i-1]= 0
                A[i-2] = A[i-2]+1
            else:
                A[i-1] = A[i-1]+1
        i -= 1
    print(A)


A = [9,9,9]
plus_one(A)
'''

def plus_one(A):
    A[-1] += 1
    for i in reversed((range(1,len(A)))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # there is a carry-out, so we need one more digit to store the result.
        # A lic way to do this is to append a 0 at the end of array
        # and update the first entry to 1.
        A[0] = 1
        A.append(0)
    print(A)
    return A
A = [9,9,9]
plus_one(A)


def plus_one_self_try(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    print(A)
    return A

A = [9,9,9,9,9,9]
plus_one_self_try(A)