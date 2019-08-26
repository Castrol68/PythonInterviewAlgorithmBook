#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 16:42
# @Author  : Eric Wang
# @File    : 1_6_findLoopNode.py

from myPackage.nodeClass import Node
from myPackage.constructNodeList import constructList


def has_loop(head):
    if head is None or head.next is None:
        return

    slow = fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow
    return


def hasLoop(head) -> bool:
    if head is None or head.next is None:
        return False

    cur = head.next
    flag = Node()
    while cur:
        if cur.next is flag:
            return True
        temp = cur.next
        cur.next = flag
        cur = temp

    return False


def findLoopNode(head, meetNode):
    first = head.next
    second = meetNode
    while first != second:
        first = first.next
        second = second.next

    return first


if __name__ == "__main__":
    head = constructList()
    meetNode = has_loop(head)
    loopNode = None

    if meetNode != None:
        print("有环")
        loopNode = findLoopNode(head, meetNode)
        print("环的入口点为：" + str(loopNode.val))
    else:
        print("无环")
