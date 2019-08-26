#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 21:09
# @Author  : Eric Wang
# @File    : 1_2_RemoveDup.py


class Node():

    def __init__(self, x):
        self.val = x
        self.next = None


def removeDup(head):
    if head is None or head.next is None:
        return

    outerCur = head.next  # 外循环
    # innerCur = None # 内层循环
    # innerPre = None # 内层的前驱节点

    while outerCur is not None:
        innerCur = outerCur.next
        innerPre = outerCur

        while innerCur is not None:
            if outerCur.val == innerCur.val:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next

        outerCur = outerCur.next


if __name__ == "__main__":
    i = 1
    head = Node(i)
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = Node(i)
        if i % 2 == 0:
            tmp.val = i + 1
        elif i % 3 == 0:
            tmp.val = i - 2
        else:
            tmp.val = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("删除之前：", end="")
    cur = head.next
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print()

    removeDup(head)

    print("删除之后：", end="")
    cur = head.next
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print()
