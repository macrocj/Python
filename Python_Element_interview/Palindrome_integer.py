'''
Author: ''
Created on '7/12/2018'
Version: 1.0
'''

#palindrome is word or sequence that read the same backward as forward
#like 2147447412
import math

#self try
'''
def is_palindrome_number(x):
    if int(x) <= 0:
        return False
        print("The integer you entered is not vaild")
    else:
        length = len(x)
        while(length>0):
            if x%10 == x%(10**(length-1)):
                x = (x - 10**(length-1))//10
                length -= 2
            else:
                False
                print("The integer you entered is not palindrome")

is_palindrome_number(1221)
'''
def is_palindrome_number(x):
    if int(x) <= 0:
        print("\nInteger cannot be a nagative!!!")
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits -1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            print("\nThe integer you entered is not palindrome")
            return False
        print(num_digits)
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    print("You entered a palindrome integer!!!")
    return True

is_palindrome_number(-123456879)


def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)+1)
    msd_mask = 10 ** (num_digits-1)
    for i in range(num_digits // 2):
        if x % 10 != x // msd_mask:
            print("\nThe integer is not palindrome !!!")
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    print("\nThe Interger you enter is palindrome!!!!")
    return True

is_palindrome_number(12122121)
