#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 17:03
# @Author  : Eric Wang
# @File    : constructNodeList.py

from myPackage.nodeClass import Node


def constructList(start, step):
    # 创建头节点
    i = start
    head = Node()
    head.next = None
    # tmp = None
    cur = head

    # 构建一个链表
    while i < 10:
        tmp = Node()
        tmp.val = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += step

    return head
