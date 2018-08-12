#Author: JC
#Date: 8/2/2018
#Version: 1.0

#### self try
import time
def decorate(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        func(*args, **kwargs)
        end = time.time()
        print("preocessing time is ", end - start)
    return wrapper
@decorate
def string_to_integer(s):
    result = 0
    time.sleep(1)
    for i in range(len(s)):
        if i!= 0:
            result = result*10+ int(s[i])
        else:
            result = (result + int(s[i]))

s = "3424324324242424242987567898764242432334535252533543434321"
#string_to_integer(s)
######
import functools,string
@decorate
def string_int2(s):
    time.sleep(1)
    return functools.reduce(
        lambda running_sum, c: running_sum*10 + string.digits.index(c),
        s[s[0] == "-":],0) * (-1 if s[0] == "-" else 1)

#string_int2(s)

def int_to_string(x):
    if_negative = False
    if x< 0:
        x, is_negative = -x, True
    s= []
    while True:
        s.append(chr(ord('0') + x % 10))
        print(s)
        x //= 10
        print(x)
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(s))

x = 2323
print(int_to_string(x))

def s(x):
    s=[]
    while True:
        s.append(chr(ord('0' + x%10)))
        x //= 10