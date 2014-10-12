#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#binary tree data structure from documents

class NodeNotFoundError(Exception):

    def __init__(self, message):
        self.message = message
        super(NodeNotFoundError, self).__init__(self)


    def __unicode__(self):
        return self.message

class TreeNode(object):
    def __init__(self, item, left, right):
        self.item = item 
        self.right = right 
        self.left = left



class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def add(self, item, binary_str_itr):
        self.root = self.add_aux(self.root, item, binary_str_itr)

    def get(self, binary_str):

        current = self.root
        if current is None:
            raise NodeNotFoundError("node not found")
            return

        for i,v in enumerate(iter(binary_str)):
            if v == '0':
                if current.left is None:
                    raise NodeNotFoundError("nod not found")
                    return 
                current = current.left
            elif v == '1':
                if current.right is None:
                    raise NodeNotFoundError("nod not found")
                    return
                current = current.right

        return current.item


    def add_aux(self, current, item, binary_str_itr): 
        if current is None:
            current = TreeNode(None, None, None)
            
        try:
            bit = next(binary_str_itr) 
            if bit == '0':
                current.left = self.add_aux(current.left, item, binary_str_itr) 
            elif bit == '1':
                current.right = self.add_aux(current.right, item, binary_str_itr)
        except StopIteration:
            current.item = item 
               
        return current

    def find_all(self):
