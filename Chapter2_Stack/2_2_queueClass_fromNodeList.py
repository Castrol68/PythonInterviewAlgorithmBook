#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/23 22:24   
# @Author  : Eric Wang         
# @File    : 2_2_queueClass_fromNodeList.py        

from myPackage.nodeClass import Node

class MyQueue():
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def isEmpty(self):
        if self.pHead is None:
            return None
        else:
            return False

    def size(self):
        size = 0
        p = self.pHead
        while p is not None:
            p = p.next
            size += 1

        return size

    def addQueue(self, ele):
        # 添加到队尾
        p = Node()
        p.val = ele
        p.next = None

        if self.pHead is None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.next = p
            self.pEnd = p

    def delQueue(self):
        if self.pHead is None:
            print("队列为空，出队失败。")
        self.pHead = self.pHead.next
        if self.pHead is None:
            self.pEnd = None

    def getFront(self):
        if self.pHead is None:
            print("队列为空，获取首元素失败。")
            return None
        return self.pHead.val

    def getBack(self):
        if self.pEnd is None:
            print("队列为空，获取尾元素失败。")
            return None
        return self.pEnd.val


if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.addQueue(5)
    myQueue.addQueue(9)
    print("队头元素为：%s" % str(myQueue.getFront()))
    print("队列大小为：%s" % str(myQueue.size()))
    print("队尾元素为：%s" % str(myQueue.getBack()))