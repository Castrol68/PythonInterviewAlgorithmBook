#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/23 21:59   
# @Author  : Eric Wang         
# @File    : 2_1_stackClass_fromNodeList.py        

from myPackage.nodeClass import Node

class MyStack():
    def __init__(self):
        self.val = None
        self.next = None

    def isEmpty(self):
        if self.next is None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.next
        while p is not None:
            p = p.next
            size += 1

        return size

    def push(self, item):
        p = Node()
        p.val = item
        p.next = self.next # 插到头节点后面，第一节点的前面
        self.next = p

    def pop(self):
        tmp = self.next # 要删除的节点
        if tmp is not None:
            self.next = tmp.next
            print("出栈成功！")
            return tmp.val
        print("栈已空。")
        if tmp is None:
            return None

    def top(self):
        if self.next is not None:
            return self.next.val
        print("")
        return None

if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(3)
    print("栈顶元素：%s" % str(myStack.top()))

    print("栈的大小为：%s" % str(myStack.size()))

    myStack.pop()
    # print("出栈成功！")
    myStack.pop()

