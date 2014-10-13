#!/usr/bin/env python
#-*- coding: utf-8 -*-

# author : younger shen
# email  : younger.x.shen@gmail.com

#all of the test case are here
import os
from programs.FileProcessor import FileProcessor
from programs.BinaryTreeInterface import BinaryTreeInterface
BASEDIR = os.getcwd()

#
#
#   this proc contains basic questions and extra bonus 1 
#
#   
def test_task_1_1_vaild_inputs(filename):
    
    print("test for  task 1-1 vaild inputs")
    count = FileProcessor.read_file_and_count_chars(filename)
    if count is not None:
        print("the input file contains %d chars" % count)


def test_task_1_1_invaild_inputs(filename):
    print("test for task 1-1 invaild inputs")
    count = FileProcessor.read_file_and_count_chars(filename)
    if count is not None:
        print("the input file contains %d chars" % count)

def test_task_1_2_vaild_inputs(input_filename, output_filename):
    print("test for task 1-2 vaild inputs")
    FileProcessor.read_and_write_file_processor(input_filename, output_filename)

def test_task_1_2_invaild_inputs(input_filename, output_filename):
    print("test for task 1-2 invaild inputs")
    FileProcessor.read_and_write_file_processor(input_filename, output_filename)


def test_task_1_3_valid_inputs(input_filename):
    print("test for task 1-3 valid inputs")
    FileProcessor.str_analysize(input_filename)

def test_task_1_3_invaild_inputs(input_filename):
    print("test for task 1-3 invaild inputs")
    FileProcessor.str_analysize(input_filename)

def test_task_2_1_valid_inputs():

    print("test for task 2-1 vaild inputs")
    interface = BinaryTreeInterface()
    interface.main_menu()

def test_task_2_1_invaild_inputs():
    #nothing to test , just test in the menu it self please
    pass
 
def test_task_3_1_vaild_inputs(input_filename, output_filename):
    print("test for task 3-1 vaild inputs \r")
    FileProcessor.encode_ascii(input_filename, output_filename)
   
def test_task_3_1_invaild_inputs(input_filename, output_filename):
    print("test for task 3-1 vaild inputs \r")
    FileProcessor.encode_ascii(input_filename, output_filename)

def test_task_3_2_vaild_inputs(input_filename, output_filename):
    print("test for task 3-2 valid inputs \r")
    tree = FileProcessor.encode_ascii(input_filename, output_filename)
    
    if tree is not None:
        print("get a tree")
        exit(0)
    else:
        print("some thing went wrong , do not build up a tree")
        exit(6)

def test_task_3_2_invaild_inputs(input_filename, output_filename):
    print("test for task 3-2 invaild inputs \r")
    tree = FileProcessor.encode_ascii(input_filename, output_filename)


def test_task_3_3_vaild_inputs(input_filename, output_filename):
    print("test for task 3-3 vaild inputs\r")
    tree = FileProcessor.encode_ascii(BASEDIR + "/test/out.txt", BASEDIR + "/test/ascii.txt")
    FileProcessor.reverse_tree_to_str(tree, input_filename, output_filename)

def test_task_3_3_invaild_inputs(input_filename, output_filename):
    print("test for task 3-3 invaild inputs \r")
    tree = FileProcessor.encode_ascii(BASEDIR + "/test/out.txt", BASEDIR + "/test/ascii.txt")
    FileProcessor.reverse_tree_to_str(tree, input_filename, output_filename)
def test_bonus_1_1_valid_inputs(input_filename, output_filename):
    print("test for bonus task 1-1 valid inputs \r")
    FileProcessor.morse_code_encode(input_filename, output_filename)
    FileProcessor.morse_code_decode(BASEDIR + "/test/morse.txt", BASEDIR + "/test/morse_de.txt")

def test_bonus_1_1_invalid_inputs(input_filename , output_filename):
    print("test for bonus task 1-1 invalid inputs \r")
    FileProcessor.morse_code_encode(input_filename, output_filename)
    FileProcessor.morse_code_decode(input_filename , output_filename)


def main():

    #task bonus
    #test_bonus_1_1_valid_inputs(BASEDIR + "/test/gpl.txt", BASEDIR + "/test/morse.txt")
    test_bonus_1_1_invalid_inputs("sfsdf", "sfsdf")
    #task 1-1
    #test_task_1_1_vaild_inputs(os.getcwd() + '/test/gpl_2.txt')
    #test_task_1_1_invaild_inputs("2.txt")

    #task 1-2
    #test_task_1_2_vaild_inputs(BASEDIR + '/test/gpl_2.txt', BASEDIR + '/test/out.txt' )
    #test_task_1_2_invaild_inputs("sfs","sdfsdf")
    

    #task 1-3
    #test_task_1_3_valid_inputs(BASEDIR + "/test/out.txt")
    #test_task_1_3_invaild_inputs("sdf")

    #task 2-1
    #test_task_2_1_valid_inputs()
    #task 3-1
    #test_task_3_1_vaild_inputs(BASEDIR + "/test/out.txt", BASEDIR + "/test/ascii.txt")
    #test_task_3_1_invaild_inputs("sdfsf", "sfdsf")

    #task 3-2
    #test_task_3_2_vaild_inputs(BASEDIR  + "/test/out.txt", BASEDIR + "/test/ascii.txt")
    #test_task_3_2_invaild_inputs("sdfsf", "sfsfd") 
    #test 3-3

    #test_task_3_3_vaild_inputs(BASEDIR + "/test/ascii.txt", BASEDIR + "/test/output2.txt")
    #test_task_3_3_vaild_inputs("sdf" , "sdf")
if __name__ == '__main__':
    main()
