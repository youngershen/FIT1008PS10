#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from .Utils import read_from_filename
from .Utils import write_to_file
from .Utils import parse_str_to_lowercase
from .Utils import check_str_char
from .Utils import letters_count

class FileProcessor(object):
    
    def __init__(self):
       super(FileProcessor, self).__init__(self)


    @staticmethod
    def read_file_and_count_chars(file_name):
        """
        
        this method implement the Task 1-1
        
        """
        content = read_from_filename(file_name)
        if content is not None:
            return len(content)
        else:
            return None
                    

        
    @staticmethod
    def read_and_write_file_processor(input_file, output_file):
        input = read_from_filename(input_file)
        if input is None:
           exit(1)
       
        output = write_to_file(output_file)
        ret = parse_str_to_lowercase(input) 
        if ret is not None:
            output.write(ret)

    @staticmethod
    def str_analysize(input_filename):
        content = read_from_filename(input_filename)
        if content is  None:
            exit(4)
        else:
            ret = check_str_char(content)
            count_dict = letters_count(ret)
            print(count_dict)

