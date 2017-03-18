import os

def read(src):
    file = open(src)
    lines = file.read()
    lines = lines.replace("\n"," ")
    lines = lines.replace(" ","")
    file.close()
    return lines

def write(lines):
    file = open(fileName,"a")
    file.write(lines)
    file.close()
