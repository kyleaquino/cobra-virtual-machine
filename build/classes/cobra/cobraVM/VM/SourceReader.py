import os

def readSource(src): # Read source code and return its string
    file = open(src)
    lines = file.read()
    lines = lines.replace("\n"," ")
    lines = lines.replace(" ","")
    file.close()
    return lines

def readByte(src): # Read byte code and return its list
    byte = readSource(src)
    return byte.split(" ")

def write(filename,lines): # Write bytecode lines to bytefile
    filename = filename.replace(".cob",".byc")
    file = open(filename,"w+")
    file.write("\n".join(lines))
    file.close()
    return filename
