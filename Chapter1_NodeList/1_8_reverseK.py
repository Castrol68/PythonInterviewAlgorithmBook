#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/22 22:13   
# @Author  : Eric Wang         
# @File    : 1_8_reverseK.py

# from myPackage.nodeClass import Node
from myPackage.constructNodeList import constructList
from myPackage.printNodeList import printNodeList
from myPackage.reverse import reverse1


def reverseK(head, k):
    if head is None or head.next is None or k < 2:
        return

    i = 1
    pre = head
    begin = head.next
    # end = None
    # pNext = None

    while begin is not None:
        end = begin

        while i < k:
            if end.next is not None:
                end = end.next
            else:
                return
            i += 1

        pNext = end.next
        end.next = None
        pre.next = reverse1(begin)
        begin.next = pNext
        pre = begin
        begin = pNext
        i = 1


if __name__ == '__main__':
    head = constructList()

    print("顺序输出：")
    printNodeList(head)

    reverseK(head, 3)

    print("逆序输出：")
    printNodeList(head)
