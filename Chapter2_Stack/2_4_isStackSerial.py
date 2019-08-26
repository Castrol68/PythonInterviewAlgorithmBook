#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 20:14
# @Author  : Eric Wang
# @File    : 2_4_isStackSerial.py


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


def isStackSerial(push, pop):
    """
    :param push: 入栈序列
    :param pop: 出栈序列
    :return: Bool
    """
    if push == None or pop == None:
        return False
    pushLen = len(push)
    popLen = len(pop)
    if pushLen != popLen:
        return False
    pushIndex = 0
    popIndex = 0
    stack = MyStack()

    while pushIndex < pushLen:
        stack.push(push[pushIndex])
        pushIndex += 1
        while not stack.isEmpty() and stack.top == pop[popIndex]:
            stack.pop()
            popIndex += 1

    return stack.isEmpty() and popIndex == popLen


if __name__ == "__main__":
    push = "12345"
    pop = "32541"

    if isStackSerial(push, pop):
        print(pop + "是" + push + "的出栈序列。")
    else:
        print(pop + "是" + push + "的出栈序列。")
