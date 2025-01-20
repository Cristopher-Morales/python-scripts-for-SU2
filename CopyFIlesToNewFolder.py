#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:49:36 2025

@author: cristopher Morales Ubal
"""

import os
import shutil
current_dir=os.getcwd()

def move_directory():
    SU2_dir=current_dir+"/codes/SU2"
    files =[]
    path_file = input("enter path to file or enter 0 to stop:")
    while (path_file != "0"):
        files.append(SU2_dir+"/"+path_file)
        path_file=input("enter path to file or enter 0 to stop:")
    return files

def copy_files(files):
    print("by default new directory will be created in home if no path is given in the option below")
    path_new_dir=input("insert path where new directory will be created:")
    if not path_new_dir: path_new_dir = current_dir
    print("new directory will be created in the following directory: "+path_new_dir)
    directory_name=input("insert name new directory where you want to copy your files:")
    try:
        os.mkdir(path_new_dir+"/"+directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    for file in files:
        try:
            shutil.copy2(file,path_new_dir+"/"+directory_name)
        except:
            shutil.rmtree(path_new_dir+"/"+directory_name)
            print("new directory has been deleted after failure to copy files. CHECK path of the files")

files = move_directory()
copy_files(files)