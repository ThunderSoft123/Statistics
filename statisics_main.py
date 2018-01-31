import sys
import os
from time import time
from os.path import join, abspath, dirname

length = len(sys.argv)
# coding = utf-8
def statistics_file_line(file_arg):
    if file_arg == "." :
        return 0
    if file_arg == ".." :
        return 0
    file_name = file_arg
    file_arg = open(file_arg,"r")
    number = 0
    for line in file_arg.readlines():
        line = line.strip()
        if line.find('\n'):
            number+=1
    file_arg.close()
    print ('%s file line = %d' % (file_name,number)) #print ever file's lines
    return number
def statistics_file(file_name):
    total_line = 0
    temp_name = file_name
    if os.path.isdir(temp_name):
        files = os.listdir(temp_name)
        temp_name_name = temp_name
        for file in files:
            temp_name = temp_name_name + "/" + file
            if os.path.isdir(temp_name):
                total_line += statistics_file(temp_name)
            else :
                total_line += statistics_file_line(temp_name)
        return total_line
    else :
        return statistics_file_line(temp_name)

#path = "source"
#files = os.listdir(path)
#s = []
#for file in files:
#     if not os.path.isdir(file):
#          f = open(path+"/"+file)
#          iter_f = iter(f)
#          str = ""
#          for line in iter_f:
#              str = str + line
#          s.append(str)
#print(s)

total_line = 0

if  length == 1:
    print "format is error \n"
    print "correct format ./xx.py xxxx xxx xxx"
else :
    number = 1
#    if os.path.isdir(sys.argv[1]):
#        print "is Dir"
    for number in range(1,length):
        total_line +=statistics_file(sys.argv[number])
print "the total_line is :", total_line
#files = os.listdir(sys.argv[1])
#for file in files:
#    print "path:",file
