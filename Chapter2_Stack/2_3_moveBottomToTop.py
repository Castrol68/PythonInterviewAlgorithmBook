#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/26 20:00   
# @Author  : Eric Wang         
# @File    : 2_3_moveBottomToTop.py        


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

def moveBottomToTop(s):
    if s.isEmpty():
        return
    top1 = s.top()
    s.pop()
    if not s.isEmpty():
        moveBottomToTop(s)

        top2 = s.top()
        s.pop()
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)


def reverse_stack(s):
    # 将栈底元素移动到栈顶
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top = s.top()
    s.pop()
    s.push(top)


if __name__ == '__main__':
    s = MyStack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    reverse_stack(s)
    print("翻转之后栈的顺序为：")
    while not s.isEmpty():
        print(s.top())
        s.pop()