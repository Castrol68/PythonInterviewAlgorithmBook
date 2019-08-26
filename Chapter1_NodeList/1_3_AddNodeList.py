#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/21 21:36   
# @Author  : Eric Wang         
# @File    : 1_3_AddNodeList.py

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None


def add(h1, h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h2

    flag = 0 # 标志位，记录进位
    sums = 0 # 两个节点的和
    p1 = h1.next # 用来遍历h1
    p2 = h2.next # 用来遍历h2
    tmp = None # 指向新建的存储相加节点和的节点
    resultHead = Node(tmp)
    resultHead.next = None
    p = resultHead # 用来指向结果链表最后一个节点
    while p1 is not None and p2 is not None:
        tmp = Node(tmp)
        tmp.next = None
        sums = p1.val + p2.val + flag
        tmp.val = sums % 10
        flag = sums // 10
        p.next = tmp
        p = tmp
        p1 = p1.next
        p2 = p2.next

    # 如果链表h2比h1长，接下来只需要考虑h2剩余节点的值
    if p1 is None:
        while p2 is not None:
            tmp = Node(tmp)
            tmp.next = None
            sums = p2.val + flag
            tmp.val = sums % 10
            flag = sums // 10
            p.next = tmp
            p = tmp
            p2 = p2.next

    # h1比h2长
    if p2 is None:
        while p1 is not None:
            tmp = Node(tmp)
            tmp.next = None
            sums = p1.val + flag
            tmp.val = sums % 10
            flag = sums // 10
            p.next = tmp
            p = tmp
            p1 = p1.next

    # 如果计算完还有进位，则需要添加新的节点
    if flag == 1:
        tmp = Node()
        tmp.next = None
        tmp.val = 1
        p.next = tmp

    return resultHead

if __name__ == "__main__":
    i = 1
    head1 = Node(i)
    head1.next = None
    head2 = Node(i)
    head2.next = None
    tmp = None
    addResult = None
    cur = head1

    while i < 7:
        tmp = Node(i)
        tmp.val = i+2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    cur = head2
    i = 9
    while i > 4:
        tmp = Node(i)
        tmp.val = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i -= 1


    print("head1:", end="")
    cur = head1.next
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print()
    print("head2:", end="")
    cur = head2.next
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print()


    addResult = add(head1, head2)

    print("AddResult:", end="")
    cur = addResult.next
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print()
