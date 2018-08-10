'''
Author: ''
Created on '7/25/2018'
Version: 1.0
'''

import time
import datetime as dt


class Solution(object):

    def timeout(func):
        def wrapper(*args, **kwargs):
            start = dt.datetime.now()
            func(*args, **kwargs)
            end = dt.datetime.now()
            print("Prcessing time is ", (end - start).microseconds)
        return wrapper


    @timeout
    def convert_V1(self, s, numRows):
        """ :type s: str :type numRows: int :rtype: str """
        if numRows == 1 or numRows >= len(s):
          return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
          L[index] += x
          if index == 0:
              step = 1
          elif index == numRows -1:
              step = -1
          index += step

        return ''.join(L)

    #@timeout
    def convert_V2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        arr = [''] * numRows
        index, step = 0, -1
        for c in s:
            arr[index] += c
            if index % (numRows-1) == 0:
                step = - step
            index += step
        return ''.join(arr)



c = Solution()
#print(c.convert_V1("PAYPALISHIRING", 4))
#print(c.convert_V2("PAYPALISHIRING", 4))


def timeout(func):
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()
        func(*args, **kwargs)
        #time.sleep(1)
        end = dt.datetime.now()
        s = end - start
        #print("Prcessing time is ", (end - start).total_seconds()*1000000)
        print("Prcessing time is ", (end - start).microseconds)
    return wrapper



@timeout
def zipzag(A,num):
    if num == 1 or num >= len(A):
        return A
    lst = [""]*num
    index, step = 0,1
    for x in A:
        lst[index] += x
        if index == 0:
            step = 1
        elif index == num -1:
            step = -1
        index += step
    print("".join(lst))
    return "".join(lst)

zipzag("PAYPALISHIRING",4)

