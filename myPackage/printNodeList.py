#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/22 16:54   
# @Author  : Eric Wang         
# @File    : printNodeList.py        

from myPackage.nodeClass import Node

def printNodeList(head):
    if head is None or head.next is None:
        return head

    cur = head.next
    while cur:
        print(cur.val, end = " ")
        cur = cur.next
    print()
