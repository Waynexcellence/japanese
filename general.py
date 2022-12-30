import string
import colorama
import random
import sys

size_question = 250
size_description = 50

def init():
    f = open( 'question.txt' , "r+" )
    buf = f.read(10)
    length = len(buf)
    for x in range(length):
        if buf[x]=='\0':
            length = x
            break
    temp = buf[:length]
    num = int(temp)
    return f , num
