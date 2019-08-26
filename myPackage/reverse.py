#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/22 22:26   
# @Author  : Eric Wang         
# @File    : reverse.py        

def reverse1(head):
    # 就地逆序
    # 判断链表是否为空
    if head is None or head.next is None:
        return

    # pre = None  # 前驱节点
    # cur = None  # 当前节点
    # nxt = None  # 后继节点

    # 将链表首节点变成尾节点
    cur = head.next
    nxt = cur.next
    cur.next = None
    pre = cur  # 向后移动
    cur = nxt

    # 使得当前遍历到的节点cur指向其前驱节点
    while cur.next is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur  # 向后移动
        cur = nxt

    # 链表最后一个节点指向倒数第二个节点
    cur.next = pre
    # 链表的头节点指向原来链表的尾节点
    head.next = cur