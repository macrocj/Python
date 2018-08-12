#Author: JC
#Date: 8/9/2018
#Version: 1.0
#
# Assume s is a string encoded as bytearray !!!!!!!!!!!!
#
def reverse_words(s):
    # First, reverse the whole string
    s=bytearray(s,'utf-8')
    s.reverse()

    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish],s[start]
            start, finish = start + 1, finish - 1
    start = 0
    while True:
        finish = s.find(b' ', start)
        if finish < 0:
            break
        # Reverses each word in the string.
        reverse_range(s,start,finish -1)
        # start = finish index plus space between two word
        start = finish + 1
    # Reverses the last word.
    reverse_range(s, start, len(s) - 1)
    # Convert Bytearrary back to string
    return str(s,encoding='utf-8')

s= "Cadlic is costly"
print(reverse_words(s))
def re(s):
    s.reverse()
    def rev(s,start,finish):
        s[start], s[finish] = s[finish],s[start]
        start, finish = start + 1, finish -1
    start = 0
    while True:
        finish = s.find(b" ", start)
        if finish < 0:
            break
        rev(s,start, finish-1)
        start = finish + 1
    rev(s, start, len(s)-1)