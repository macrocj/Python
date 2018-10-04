############################
#Author: JC
#Date: 7 / 15 / 2018
#Version: 1.0
##############################
'''
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    #First pass; group elements smaller than pivot
    for i in range(len(A)):
        #look for a smaller element.
        for j in range(i+1, len(A)):
            print("before change %s" %A)
            if A[j] < pivot:
                A[i],A[j] = A[j],A[i]
                print("changed %s\n" %A)
                break


    #Second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        #look for a larger element. Stop when we reach an element less than
        #pivot, since frist pass has moved them to the start of A.
        for j in reversed(range(i)):
            print("Larger p before change %s" %A, "i = %s" %i, "j = %s" %j)
            if A[j] > pivot:
                A[i],A[j] = A[j],A[i]
                print("i = %s "%i,"and j = %s" %j)
                print("Larger P after change %s" %A)
                break
    print(A)
A = [0,1,3,0,2,1,1]
dutch_flag_partition(1,A)

def flag_try(p_index, A):
    p_value = A[p_index]
    #compare smaller number with index
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < p_value:
                A[i],A[j] = A[j],A[i]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > p_value:
                A[i], A[j] = A[j], A[i]
                break
    print(A)
S = [2,3,6,7,1,3,6,9]
flag_try(2,S)


#improved time complexity verison
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    #First pass; group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i],A[smaller] = A[smaller],A[i]
            smaller += 1

    #Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i]> pivot:
            A[i],A[larger] = A[larger],A[i]
            larger -=1
    print(A)
A = [0,1,3,0,2,1,1]
dutch_flag_partition(1,A)
'''
def flag_try2(p_index,A):
    p_value = A[p_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < p_value:
            A[i],A[smaller] = A[smaller],A[i]
            smaller += 1
    larger = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] > p_value:
            A[i],A[larger] = A[larger],A[i]
            larger -+ 1
    print(A)
B = [1,6,3,5,8,3,8,0]
flag_try2(2,B)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    #keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]

    smaller, equal, larger = 0, 0, len(A)
    #print(smaller, equal, larger)
    # keep iterating as long as there is an unclassified element
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller],A[equal] = A[equal],A[smaller]
            smaller, equal = smaller + 1, equal + 1
            print("A[equal] = %s" %A[equal])
            print("smaller iterate is %s" %A)
        elif A[equal] == pivot:
            equal += 1
        else: #A[equal] > pivot
            larger -= 1
            A[equal],A[larger] = A[larger],A[equal]
            print("larger iterate is %s" %A)
    print(A)

x = [-3,0,-1,1,1,3,-5,7,4,2]
dutch_flag_partition(1,x)

