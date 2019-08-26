#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 20:49
# @Author  : Eric Wang
# @File    : 2_5_minEleInO1.py


class MyStack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
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
        self.eleStack = MyStack()
        self.minStack = MyStack()

    def push(self, data):
        self.eleStack.push(data)
        if self.minStack.isEmpty():
            self.minStack.push(data)
        else:
            if data < self.minStack.top():
                self.minStack.push(data)

    def pop(self):
        topData = self.eleStack.top()
        self.eleStack.pop()
        if topData == self.mins():
            self.minStack.pop()
        return topData

    def mins(self):
        if self.minStack.isEmpty():
            return 2 ** 32
        else:
            return self.minStack.top()


if __name__ == "__main__":
    stack = stack()
    stack.push(5)
    print("栈中最小值为：" + str(stack.mins()))
    stack.push(6)
    print("栈中最小值为：" + str(stack.mins()))
    stack.push(2)
    print("栈中最小值为：" + str(stack.mins()))
    stack.pop()
    print("栈中最小值为：" + str(stack.mins()))
