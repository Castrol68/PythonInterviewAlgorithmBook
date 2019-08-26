#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 20:46
# @Author  : Eric Wang
# @File    : 1_9_mergeTwoNodeList.py

from myPackage.printNodeList import printNodeList
from myPackage.nodeClass import Node

# class Node():
#
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def merge(head1, head2):

    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1

    cur1 = head1.next  # 链表1的指针
    cur2 = head2.next  # 链表2的指针
    # head = None  # 合并链表的头节点
    # cur = None  # 合并后的链表在尾节点

    if cur1.val > cur2.val:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next

    while cur1 is not None and cur2 is not None:
        if cur1.val < cur2.val:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    # 遍历完一个链表之后，处理剩余的链表
    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2

    return head


def ConstructList(start):
    i = start
    head = Node()  # 头节点的结构
    head.next = None
    # tmp = None
    cur = head
    while i < 7:
        tmp = Node()  # 新建节点及其结构
        tmp.val = i
        tmp.next = None
        cur.next = tmp  # 将新建节点连接起来
        cur = tmp
        i += 2

    return head


if __name__ == "__main__":
    head1 = ConstructList(1)
    head2 = ConstructList(2)

    print("head1:", end="")
    printNodeList(head1)
    print("head2:", end="")
    printNodeList(head2)
    print("合并之后的链表:", end="")
    merged = merge(head1, head2)
    printNodeList(merged)
