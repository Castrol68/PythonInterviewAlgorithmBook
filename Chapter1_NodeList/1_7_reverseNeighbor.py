#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/22 17:30   
# @Author  : Eric Wang         
# @File    : 1_7_reverseNeighbor.py        

# from myPackage.nodeClass import Node
from myPackage.printNodeList import printNodeList
from myPackage.constructNodeList import constructList


def reverse(head):
    if head is None or head.next is None:
        return

    cur = head.next
    pre = head
    # next_next = None # 当前节点的后继节点的后继节点
    while cur is not None and cur.next is not None:
        next_next = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next_next
        pre = cur
        cur = next_next


if __name__ == '__main__':
    head = constructList()
    # reverse(head)
    # printNodeList(head)

    print("顺序输出：", end='')
    printNodeList(head)

    reverse(head)

    print("逆序输出：",end='')
    printNodeList(head)


