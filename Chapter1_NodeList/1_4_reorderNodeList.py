#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/21 22:17   
# @Author  : Eric Wang         
# @File    : 1_4_reorderNodeList.py        

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None


def findMiddleNode(head):
    if head is None or head.next is None:
        return head

    fast = Node(0) # 快指针每次向前移动2步，
    slow = Node(0) # 慢指针每次向前移动1步，当快指针移动到表尾时，满指针刚好指向中间节点
    slowPre = Node(0)

    while fast is not None or fast.next is not None: #\
            # or fast.next.next is not None:
        slowPre = slow
        slow = slow.next
        fast = fast.next
        fast = fast.next

    slowPre.next = None # 从中间断开链表

    return slow

def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    # next = cur.next
    pre.next = None

    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre

def reorder(head):
    if head is None or head.next is None:#
        #or head.next.next is None:
        return

    cur1 = head.next
    mid = findMiddleNode(head.next)
    cur2 = reverse(mid)
    tmp = None

    while cur1.next is not None:
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp
        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp

    cur1.next = cur2
    cur2.next = None

if __name__ == '__main__':
    i = 1
    head = Node(i)
    head.next = None
    tmp = None
    cur = head

    while i < 9:
        tmp = Node(i)
        tmp.val = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("排序之前:", end='')
    cur = head.next
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print()

    reorder(head)

    print("排序之后:", end='')
    cur = head.next
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
