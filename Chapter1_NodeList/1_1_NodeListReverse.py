#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 21:21
# @Author  : Eric Wang
# @File    : 1_1_NodeListReverse.py


class Node():

    def __init__(self, x):
        self.value = x
        self.next = None


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

def reverse2(head):
    '''
    插入法
    :param head:
    :return:
    '''
    # 判断链表是否为空
    if head is not None or head.next is not None:
        return
    cur = None
    next = None
    cur = head.next.next
    head.next.next = None

    while cur is not None:
        nxt = cur.next # 保存后继节点
        cur.next = head.next # 使得当前节点指向当前节点的前一个
        head.next = cur #使得头节点指向当前节点
        cur = nxt # 向后移动


if __name__ == "__main__":
    i = 1
    head = Node(i)
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    while i < 8:
        tmp = Node(i)
        tmp.value = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("Before：", end="")
    cur = head.next
    while cur is not None:
        print(cur.value, end=" ")
        cur = cur.next
    print()

    reverse2(head)

    print("After：", end="")
    cur = head.next
    while cur is not None:
        print(cur.value, end=" ")
        cur = cur.next
