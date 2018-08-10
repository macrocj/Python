'''
Author: ''
Created on '7/12/2018'
Version: 1.0
'''
#scrpt ask for a integer and return reverse integer
#input is 234 then result is 432
'''
def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x< 0 else result
'''

number = int(input("Please enter a number"))
reverse = 0
while (number > 0):
    reminder = number % 10
    print("reminder is", reminder)
    reverse = (reverse * 10) + reminder
    print("number %s of reverse round" %number, reverse)
    number = number // 10
    print(number)

print("\nReverse of entered number is = %d" % reverse)







number = int(input("Please enter a iterger number"))
reverse = 0
while(number>0):
    reminder = number % 10
    reverse = (reverse * 10) + reminder
    number = number //10
print("The reverse number is %s" %reverse)



