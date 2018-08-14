#Author: JC
#Date: 8/11/2018
#Version: 1.0

def look_and_say(n):
    def next_number(s):
        result, i = [], 0
        while i< len(s):
            count = 1
            while i+ 1< len(s) and s[i] == s[i+1]:
                i+= 1
                count +=1
            result.append((str(count) + s[i]))
            i += 1
        return ''.join(result)
    s = '1'
    for _ in range(1,n):
        s = next_number(s)
    return s
#print(look_and_say(5))


def self_try(n):

    def nextnum(s):
        result, i = [], 0
        while i<len(s):
            count = 1
            while i+1< len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            result.append(str(count)+s[i])
            i += 1
        s =''.join(result)
        return s
    s = '1'
    for _ in range(1,n):
        s = nextnum(s)
    return s
#print(self_try(6))

# Pythonic solution uses the power of itertools.groupby().
import itertools
def look_and_say_pythnoic(n):
    s = '1'
    for _ in range(1,n):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s)
        )
    return s

#print(look_and_say_pythnoic(5))

for key, group in itertools.groupby('11223311332244'):
    print(key,len(list(group)))












