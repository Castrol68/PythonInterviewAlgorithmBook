#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/26 21:05   
# @Author  : Eric Wang         
# @File    : 2_6_2stackForQueue.py        

class MyStack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("Stack is None.")
            return None

    def push(self, item):
        return self.items.append(item)


class stack():
    def __init__(self):
        self.A = MyStack()
        self.B = MyStack()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.isEmpty():
            while not self.A.isEmpty():
                self.B.push(self.A.top())
                self.A.pop()

        first = self.B.top()
        self.B.pop()
        return first

if __name__ == '__main__':
    stack = stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("队列首元素为：" + str(stack.pop()))
    print("队列首元素为：" + str(stack.pop()))
    print("队列首元素为：" + str(stack.pop()))