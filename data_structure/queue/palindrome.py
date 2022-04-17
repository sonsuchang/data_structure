import sys
import os
currpath = os.getcwd()
currpath = currpath + "\data_structure"
sys.path.append(currpath)

from stack.ListStack import *
from listqueue import *

def isPalindrome(A) -> bool:
    s = ListStack()
    q = ListQueue()
    for i in range(len(A)):
        s.push(A[i])
        q.enqueue(A[i])
    while(not q.isEmpty()) and s.pop() == q.dequeue():
        {}
    if q.isEmpty():
        return True
    else:
        return False

def main():
    print("Palindrome Check!")
    str = 'lioninoil'
    t = isPalindrome(str)
    print(str, " is Palindrome?: ", t)

if __name__ == "__main__":
    main()