#Author: JC
#Date: 8/13/2018
#Version: 1.0

def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else: # c is letter of alphabet.
            result.append(c * count) # Appends count copies of c to result
            count = 0
    return ''.join(result)

def encoding(s):
    result, count = [], 0
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i]!= s[i-1]:
            # Found new character so weite the conut of previous character
            result.append(str(count) + s[i-1])
            count = 1
        else: # s[i] == s[i-1]
            count += 1
    return ''.join(result)

s1 = 'aaaabcccaa'
s2 = '3d4f2e'
print(decoding(s2))
print(encoding(s1))