#Author: JC
#Date: 8/5/2018
#Version: 1.0
import string,functools
def selfTry(col):  #only work on few number
    s = string.ascii_uppercase

    for i, n in enumerate(s, start=1):
        if i == col:
            if col<=26 and col!=0:
                result = s[i-1]
                return result
        if i not in range(1,27):
            result = s[((col // 26)-1)]+s[(col%26-1)]
            #print(s[((col // 26)-1)]+s[(col%26)])
            return result

def colnum_string(n):  #worked
    stringlist = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        stringlist = chr(65 + remainder) + stringlist
    return stringlist

def ss_decode_col_id(col): #reduce not working
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col,0)

print(selfTry(28))
#print(colnum_string(70288))
#print(ss_decode_col_id(26))