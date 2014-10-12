#!/usr/bin/env python
#-*- coding: utf-8 -*-

# author : younger shen
# email  : younger.x.shen@gmail.com

#all of the test case are here
import os
from programs.FileProcessor import FileProcessor
from programs.BinaryTreeInterface import BinaryTreeInterface
BASEDIR = os.getcwd()


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
    print("test for test 1-3 invaild inputs")
    FileProcessor.str_analysize(input_filename)

def test_task_2_1_valid_inputs():

    interface = BinaryTreeInterface()
    interface.main_menu()

def main():
    #task 1-1
    #test_task_1_1_vaild_inputs(os.getcwd() + '/test/gpl.txt')
    #test_task_1_1_invaild_inputs("2.txt")

    #task 1-2
    #test_task_1_2_vaild_inputs(BASEDIR + '/test/gpl.txt', BASEDIR + '/test/out.txt' )
    #test_task_1_2_invaild_inputs("sfs","sdfsdf")
    

    #task 1-3
    #test_task_1_3_valid_inputs(BASEDIR + "/test/out.txt")
    #test_task_1_3_invaild_inputs("sdf")

    #task 2-1
    test_task_2_1_valid_inputs()


if __name__ == '__main__':
    main()
