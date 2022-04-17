from listqueue import *
class stack_cls:
    def __init__(self):
        self.q1 = ListQueue()
        self.q2 = ListQueue()
    def push(self, x):
        self.q1.enqueue(x)
    def pop(self, x):
        while (not self.q1.isEmpty()):
            self.q2.enqueue(self.q1.dequeue())
        