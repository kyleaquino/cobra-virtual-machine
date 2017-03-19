import os

def read(src):                              # Read source code and return its string
    file = open(src)
    lines = file.read()
    lines = lines.replace("\n"," ")
    lines = lines.replace(" ","")
    file.close()
    return lines

def write(filename,lines):                  # Write bytecode lines to bytefile
    fileName = fileName.replace(".cob",".byc")
    file = open(fileName,"w+")
    file.write(lines)
    file.close()
