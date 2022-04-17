from itertools import filterfalse
from listqueue import *
def check(w):
    w_check = ListQueue()
    cnt = 0
    idx = w.index("$")    
    for i in range(idx):
        w_check.enqueue(w[i])
    for k in range(idx + 1, len(w)):
        if w_check.dequeue() == w[k]:
            cnt += 1
    if cnt == idx:
        print("True")
    else:
        print("False")
check(input())