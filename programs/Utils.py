#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#all utils are here
import os
import re
import sys

from .BinaryTree import NodeNotFoundError
from .BinaryTree import BinaryTree

sys.setrecursionlimit(99999)

RE_ONE_LETTER = r"^[a-z]{1}$"
RE_ALL_CHAR = r"[a-zA-Z]+"
RE_BINARY_STR = r"^[0-1]+$"

LOWER_CASE_START = ord('a')
LOWER_CASE_END   = ord('z') + 1
LOWER_LETTERS = "abcdefghijklmnopqestuvwxyz"

#morse code config
MORSE_CODE_DOT  = "1"
MORSE_CODE_DASH = "111"
MORSE_CODE_SEP  = "0"
MORSE_CODE_CSEP = "000"

MORSE_CODE_A = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH 
MORSE_CODE_B = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_C = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_D = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT 
MORSE_CODE_E = MORSE_CODE_DOT
MORSE_CODE_F = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT 
MORSE_CODE_G = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_H = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_I = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_J = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_K = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_L = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT 
MORSE_CODE_M = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_N = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_O = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH 
MORSE_CODE_P = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_Q = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_R = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT
MORSE_CODE_S = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT 
MORSE_CODE_T = MORSE_CODE_DASH
MORSE_CODE_U = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_V = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_W = MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_X = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH
MORSE_CODE_Y = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH 
MORSE_CODE_Z = MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DASH + MORSE_CODE_SEP + MORSE_CODE_DOT  + MORSE_CODE_SEP + MORSE_CODE_DOT

MDICT = {
        'a':MORSE_CODE_A,
        'b':MORSE_CODE_B,
        'c':MORSE_CODE_C,
        'd':MORSE_CODE_D,
        'e':MORSE_CODE_E,
        'f':MORSE_CODE_F,
        'g':MORSE_CODE_G,
        'h':MORSE_CODE_H,
        'i':MORSE_CODE_I,
        'j':MORSE_CODE_J,
        'k':MORSE_CODE_K,
        'l':MORSE_CODE_L,
        'm':MORSE_CODE_M,
        'n':MORSE_CODE_N,
        'o':MORSE_CODE_O,
        'p':MORSE_CODE_P,
        'q':MORSE_CODE_Q,
        'r':MORSE_CODE_R,
        's':MORSE_CODE_S,
        't':MORSE_CODE_T,
        'u':MORSE_CODE_U,
        'v':MORSE_CODE_V,
        'w':MORSE_CODE_W,
        'x':MORSE_CODE_X,
        'y':MORSE_CODE_Y,
        'z':MORSE_CODE_Z
        }

MDICTR ={
        MORSE_CODE_A : 'a',
        MORSE_CODE_B : 'b',
        MORSE_CODE_C : 'c',
        MORSE_CODE_D : 'd',
        MORSE_CODE_E : 'e',
        MORSE_CODE_F : 'f',
        MORSE_CODE_G : 'g',
        MORSE_CODE_H : 'h',
        MORSE_CODE_I : 'i',
        MORSE_CODE_J : 'j',
        MORSE_CODE_K : 'k',
        MORSE_CODE_L : 'l',
        MORSE_CODE_M : 'm',
        MORSE_CODE_N : 'n',
        MORSE_CODE_O : 'o',
        MORSE_CODE_P : 'p',
        MORSE_CODE_Q : 'q',
        MORSE_CODE_R : 'r',
        MORSE_CODE_S : 's',
        MORSE_CODE_T : 't',
        MORSE_CODE_U : 'u',
        MORSE_CODE_V : 'v',
        MORSE_CODE_W : 'w',
        MORSE_CODE_X : 'x',
        MORSE_CODE_Y : 'y',
        MORSE_CODE_Z : 'z'
        }
        
def c2mc(c):
    return MDICT[c.lower()]

def i28b(i):
    bstr = bin(i)[2:]
    ret = ""
    ret = "0" * (8 - len(bstr)) + bstr
    #return ret
    return bstr

def c2b(c):
    i = ord(c)
    return bin(i)[2:]

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
    
     
    #return i28b(ord(letter)) == bstr
    return True


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
    
        elif 'print' == cmds[0]:
            if len(cmds) != 1:
                wrong_cmd_helper()
                command_find_item_bstr_helper()
            else:
                binary_tree.find_all()
    
        elif 'quit' == cmds[0]:
            if len(cmds) != 1:
                wrong_cmd_helper()
                command_quit_helper()
            else:
                print("Bye Bye Beautiful !!\r")
                exit(0)
                


def command_quit_helper():
    print("if you wanna quit just input as follow\r" )
    print("quit \r")

def command_find_item_bstr_helper():
    print("find all in the binary tree use under command \r")
    print("find \r")

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


def encode_str_to_ascii(content):
    
    ret = ""
    tree = BinaryTree()
    for i,v in enumerate(iter(content)):
        ret += c2b(v)
        tree.add(v, iter(ret))
    return ret, tree
        

def morse_encode(content):
    ret = ""
    content = parse_str_to_lowercase(content)
    for i,e in enumerate(iter(content)):
        ret += (c2mc(e) + MORSE_CODE_CSEP)
    return ret

def morse_decode(content):
    ret = ""
    morse_c_list = content.split(MORSE_CODE_CSEP)[:-1]
    for i in morse_c_list:    
        ret += MDICTR[i.strip()]

    return ret 
