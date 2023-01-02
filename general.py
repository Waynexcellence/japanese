import string
import colorama
import random
import sys
import os
import shutil

max = 10
size_paper = 60
size_description = 60
size_answer = 60
size_question = 120

def strlen( string , limit ):
    for x in range(int(limit/2)):
        if string[x] == '\0':
            return int(x)
    return int(limit/2)

def Connect_To_Paper():
    fd = open( "Paper" , "r+" )
    buf = fd.read(max)
    fd.seek(0)
    return fd , int(fd.read(strlen(buf,max*2)))

def connect_to_paper( paper_name ):
    fd = open( paper_name , "r+" )
    buf = fd.read(max)
    fd.seek(0)
    return fd , int(fd.read(strlen(buf,max*2)))

def show_Paper( fd , num ):
    if num == 0:
        print("\033[1;33;40m目前沒有考卷\033[0m")
        return 
    print("\033[1;33;40m目前考卷:\033[0m")
    for x in range(num):
        fd.seek((1+x)*size_paper)
        paper_name = fd.read((int)(size_paper/2))
        print("\033[1;33;40m[%d] %s" %(x,paper_name) )
print("")

def show_paper( fd , num ):
    if num == 0:
        print("\033[1;33;40m此考卷目前沒有題目\033[0m")
        return
    print("\033[1;33;40m目前題目:\033[0m")
    for x in range(num):
        fd.seek((1+x)*size_question)
        description = fd.read((int)(size_description/2))
        position = fd.tell()
        fd.seek((1+x)*size_question+size_description)
        space = (" ")*(fd.tell()-position)
        answer = fd.read((int)(size_answer/2))
        print("\033[1;33;40m[%d] \033[1;32;40m題目:%s %s\033[1;36;40m解答:%s\033[0m" %(x,description,space,answer) )
    print("")

def write_thing( fd , position , thing , limit ):
    space = '\0'*limit
    fd.seek(position)
    fd.write(space)
    fd.seek(position)
    fd.write(thing)

def update_num( fd , num ):
    space = '\0'*max
    fd.seek(0)
    fd.write(space)
    fd.seek(0)
    fd.write(str(num))

