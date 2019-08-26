#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/23 21:30   
# @Author  : Eric Wang         
# @File    : 1_10_removeNodeBypNext.py        

from myPackage.constructNodeList import constructList
from myPackage.printNodeList import printNodeList

def removeNodeP(p):
    if p is None or p.next is None:
        return False

    p.val = p.next.val
    # tmp = p.next
    # p.next = tmp.next
    p.next = p.next.next

    return True

if __name__ == '__main__':
    head = constructList(1, 1)
    print("删除之前：", end="")
    printNodeList(head)

    removeNodeP(head)

    print("删除之后：", end="")
    printNodeList(head)
