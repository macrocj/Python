'''
Author: ''
Created on '7/29/2018'
Version: 1.0
'''

import time

def consumer(name):
    print("%s 吃包子了！" %name)
    while True:
        baozi = yield
        print("包子[%s]好了，被[%s]吃了！" %(baozi, name))

'''
c=consumer("jeff")
c.__next__()

b1 = "韭菜馅"
c.__next__()
c.send(b1)
'''
def producer(name):
    c = consumer('A')
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子了")
    for i in range(10):
        time.sleep(1)
        print("%s做了两个包子！" %name)
        c.send(i)
        c2.send(i)


producer("Alex")

