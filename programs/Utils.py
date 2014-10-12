#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#all utils are here
import os
import re
from .BinaryTree import NodeNotFoundError

RE_ONE_LETTER = r"^[a-z]{1}$"
RE_ALL_CHAR = r"[a-zA-Z]+"
RE_BINARY_STR = r"^[0-1]{8}$"

LOWER_CASE_START = ord('a')
LOWER_CASE_END   = ord('z') + 1
LOWER_LETTERS = "abcdefghijklmnopqestuvwxyz"



def i28b(i):
    bstr = bin(i)[2:]
    ret = ""
    ret = "0" * (8 - len(bstr)) + bstr
    return ret

def test_a_letter(letter):
    pattern = re.compile(RE_ONE_LETTER)
    mch = re.match(pattern, letter)
    if mch is not None:
        return True
    else:
        return False

def test_a_binary_str(bstr):
    pattern = re.compile(RE_BINARY_STR)
    mch = re.match(pattern, bstr)
    if mch is not None:
        return True
    else:
        return False

def check_letter_match_bstr(letter, bstr):
    
    if not test_a_letter(letter):
        return False 

    if not test_a_binary_str(bstr):
        return False
    
     
    return i28b(ord(letter)) == bstr


def wrong_cmd_helper():
    print("command input incorrect try agin ! \r")
    

def parse_cmd_helper(method):
    cmd = input()
    return command_parser(cmd, method)


def re_input(method):
    print("pring a command please ")
    cmds = input()
    command_parser(cmds, method)


def command_parser(binary_tree):


    while True:
        input_command = input("please input command\r\n")
    
        cmds = input_command.split(" ")

        if 'add' == cmds[0]:
            if len(cmds) != 3  or  not check_letter_match_bstr(cmds[1], cmds[2]):
                wrong_cmd_helper()
                command_add_item_bstr_helper()
            else:
                print("add successful")
                binary_tree.add(cmds[1], iter(cmds[2]))
                
        elif 'get' ==cmds[0]:
            if len(cmds) != 2 or not test_a_binary_str(cmds[1]):
                wrong_cmd_helper()
                command_get_item_bstr_helper()
            else:
                ret = ""
                try:
                    ret = binary_tree.get(cmds[1])
                
                except NodeNotFoundError as e:
                    print("node not found")
                else:
                    print("result:\r")
                    print(ret)

    
def command_add_item_bstr_helper():
    print("add item and binary to the tree use under command \r")
    print("add item binary_str\r")
    
def command_get_item_bstr_helper():
    print("get item from a binary tr use command as follow \r")
    print("get binary str")


def letters_count(content):
    if content is None:
        print("content is none !")
        exit(5)

    ret = {}
    for i ,v in enumerate(LOWER_LETTERS):
        ret[v] = content.count(v)
    
    return sorted(ret.items(), key=lambda i:-i[1])
    


def check_str_char(content):
    if content is None:
        print("content is none and can not parse it")
        exit(4)

    pattern = re.compile(RE_ALL_CHAR)
    mch = re.match(pattern, content)
    if mch is not None:
        return mch.group()
    else:
        print("no match found ")
        return None

def parse_str_to_lowercase(content):
    if content is None:
        print("content is none cannot parse it")
        exit(3)
    pattern = re.compile(RE_ALL_CHAR)
    match = re.findall(pattern, content)
    ret = ""
    if match is not None:
        for i,e in enumerate(match):
           ret += e.lower()
        return ret
    else:
        return None


def write_to_file(filename):

    if os.path.exists(filename):
        choice = input("output file exists if you want to over write it input y/Y else exit\r\n")
        print(choice)
        if 'Y' != choice and 'y' != choice:
            exit(2)
    
    file_handler = open(filename, 'w')
    return file_handler

def read_from_filename(filename):
    content = None
    try:
        with open(filename) as file:
            content = file.read()

    except IOError as e:
        print("file do not found or other mistake happened")
        return None
    else:
        return content
