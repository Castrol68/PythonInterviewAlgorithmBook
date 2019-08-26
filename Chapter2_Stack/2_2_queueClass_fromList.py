#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/23 22:14   
# @Author  : Eric Wang         
# @File    : 2_2_queueClass_fromList.py        

class MyQueue():
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def getFront(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.front]

    def getLast(self):
        if self.isEmpty():
            return None
        else:
            return self.arr[self.rear-1]

    def delHead(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列为空，无法删除。")

    def addLast(self, ele):
        self.arr.append(ele)
        self.rear += 1

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.addLast(5)
    myQueue.addLast(9)
    print("队头元素为：%s" % str(myQueue.getFront()))
    print("队列大小为：%s" % str(myQueue.size()))
    print("队尾元素为：%s" % str(myQueue.getLast()))