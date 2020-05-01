#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import csv


def get_file_list(folder):    
    ''' Get file list in path and reture with list
        Input:folder
        Output:list[]
    '''
    list = []
    if os.path.isdir(folder):
        for row in os.listdir(folder):
            if os.path.isfile(folder+"\\" + row):
                list.append(row)
    else:
        pass
    return list

def open_file(file_name):
    ''' Open file and return file contax as strin max size is 2048 Byte 
        Input:file_name
        Output:reutren str
    '''
    try:
        file_obj = open(file_name,"r")
        return file_obj.readlines()
    except IOError:
        return ""



path=r'C:\Tars\Trash'
os.chdir=sys.path[0]
file_name1=get_file_list(path)
print(file_name1)
str=open_file(path + "\\" + file_name1[2])
print("")
print(str[0])
print(str[1])
print(str[2])
print(str[3])







