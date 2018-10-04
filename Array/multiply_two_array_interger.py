#Author: JC
#Date: 7/17/2018
#Version: 1.0

def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            print(result)
            result[i + j] += result[i + j + 1] // 10
            print(result)
            result[i +j + 1] %= 10
            print(result)
        #print("the round of i %s " %result)
    # remove the leading zeroes.
    result = result[next((i for i, x in enumerate(result)
                          if x!= 0), len(result)):] or [0]
    #print(result[0], result[1:],"\n",[result[0]] + result[1:])
    return [sign * result[0]] + result[1:]

num1= [1,2,3,4]
num2 = [4,5,6,7]

#multiply(num1,num2)

def try_multiply(num1, num2):
    sign = -1 if num1[0] < 0 or num2[0] < 0 else 1
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    result = result[1:] or [0]
    s = next((i for i, x in enumerate(result) if x!= 0), len(result))
    print(s)
    for i,x in enumerate(result):
        print(i,x)
    return [result[0] * sign] + result[1:]
#x= try_multiply(num1,num2)
#print(x)

def try_multiple2(num1,num2):
    A = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            A[i + j + 1] += num1[i]*num2[j]
            A[i + j ] += A[i + j + 1] // 10
            A[i + j + 1] %= 10
    index = 0
    for s in range(1,len(A)):
        if A[s-1] != 0:
            break
        else:
            if A[s-1] == 0:
                index += 1
    return A[index:]

x=try_multiple2(num1,num2)
print(x)