from practice3_linkedstack import *

def check_func():
    w = input()
    check_sum = 0
    check_list = ""
    check_w = LinkedStack()
    a = w.index("$")
    for i in range(a + 1):
        if w[i] == "$":
            for k in range(i+1, len(w)):
                check_list += w[k]
        else:
            check_w.push(w[i])
    for z in range(0, len(check_list)):
        check_w.printStack()
        if check_list[z] == check_w.pop():
            check_sum += 1
    if check_sum == len(check_list):
        print("True")
    else:
        print("False")
check_func()