#!/usr/bin/env python
#-*- coding: utf-8 -*-

# author : younger shen
# email  : younger.x.shen@gmail.com

#binary tree interface

from .BinaryTree import BinaryTree
from .Utils import command_add_item_bstr_helper
from .Utils import command_parser



class BinaryTreeInterface(object):

    def __init__(self):
        self.binary_tree = BinaryTree()

    def main_menu(self):
        command_parser(self.binary_tree)

    def add_item(self, item, binary_str):

        #cmd = command_add_item_bstr_helper(self.binary_tree.add)
        #if cmd is not None:
        #    print(cmd)

        #ret = command_parser()
        pass

    def get_item(self, binary_str):
        pass
        #cmd = command_get_item_bstr_helper(self.binary_tree.get) 
