#Author: JC
#Date: 8/2/2018
#Version: 1.0

# check if sting is palindromic or not

def is_palindromic(s):
    # note that s[~i] for i in [0,len(s) - 1] is s[-(i-1)]
    return all(s[i] == s[-(i-1)] for i in range(len(s) // 2))

s = "ada"
print(is_palindromic(s))