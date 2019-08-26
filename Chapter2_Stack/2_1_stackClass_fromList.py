#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/23 21:49   
# @Author  : Eric Wang         
# @File    : 2_1_stackClass_fromList.py

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


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(3)
    print("栈顶元素：%s" % str(myStack.top()))

    print("栈的大小为：%s" % str(myStack.size()))

    if myStack.pop():
        print("出栈成功！")