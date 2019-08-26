#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/22 17:01   
# @Author  : Eric Wang         
# @File    : nodeClass.py

class Node():
    def __init__(self, x = None):
        self.val = x
        self.next = None