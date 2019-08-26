#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 15:41
# @Author  : Eric Wang
# @File    : 1_5_findLastK.py


class Node():

    def __init__(self, x=None):
        self.val = x
        self.next = None


def findLastK(head, k):
    if head is None or head.next is None:
        return head

    # slow = myPackage()
    # fast = myPackage()
    slow = head.next
    fast = head.next

    i = 0
    while i < k and fast.next is not None:  # 快指针先行k步
        fast = fast.next
        i += 1
    if i < k:
        return None

    while fast is not None:  # 快慢指针同步前进
        slow = slow.next
        fast = fast.next

    return slow


def constructList():
    # 创建头节点
    i = 1
    head = Node()
    head.next = None
    # tmp = None
    cur = head

    # 构建一个链表
    while i < 10:
        tmp = Node()
        tmp.val = input("input N nums:")
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    return head


def printListNode(head):
    cur = head.next
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":
    myNodeList = constructList()
    # result = None
    print("链表：", end="")

    printListNode(myNodeList)

    k = int(input("input k:"))
    result = findLastK(myNodeList, k)
    # print(result.val)

    if result is not None:
        print("链表倒数第%d个元素为：%s" % (k, result.val))
