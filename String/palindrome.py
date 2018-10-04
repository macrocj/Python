#Author: JC
#Date: 8/7/2018
#Version: 1.0

def is_palindrome(s):
    # i moves forward, and j moves backward.
    i, j = 0, len(s)-1
    while i<j:
        # i adn j both skip non-alphanumeric characters
        while not s[i].isalnum() and i <j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        return True

def is_palindrome_pythonic(s):
    return all(a==b
               for a,b in zip(
                    map(str.lower, filter(str.isalnum, s)),
                    map(str.lower, filter(str.isalnum, reversed(s))
    )))

s =  'Able was I, ere I saw Elba'

print(is_palindrome(s))
print(is_palindrome_pythonic(s))