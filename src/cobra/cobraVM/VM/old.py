import sys
import os
import re

#Bytecode database
bytecode = {"PRINT":"PRINT","+":"ADD","-":"SUB","*":"MUL","/":"DIV","=":"EQUALS","\"":"DOUBLEQUOTE"}
#Variable Memory
variable={}

def main(argv):
    source = read(argv[1])           # Pass string of source file to variable source
    token = lexer(source)            # Tokenize the string through lexer function
    bytecode = parser(token,argv[1]) # Generate bytecode file
    interpreter(bytecode)            # Execute program using the bytecode file
    return 0

def lexer(lines):
    return re.findall("\s*(\d+|\w+|.)", lines) # Splits the string into possible expressions

def parser(token,argv):
    argv = argv.replace(".cob",".byc") # Prepare name of bytefile
    for tok in token:                  # For Loop Tokens
        if tok in bytecode:            # Check if the current token is a keyword
            write(bytecode.get(tok)+"\n",argv)  # Convert keyword source code to bytecode line by line
        else:
            write(tok+"\n",argv)       # Directly Write non-keyword source code to the bytefile line by line
    write("END",argv)                  # Write END at the end of the bytefile
    return argv                        # Return filename of bytefile

def interpreter(byte):
    loop = True                        # Loop Variable
    index = 0                          # Loop Index Variable
    byc = read(byte)                   # Read bytecode
    byc = byc.split(" ")               # Split the string bytecode
    while loop:                        # Run bytefile line by line
        instruction = byc[index]       # Copy line to instruction
        if instruction == "END":       # Stop loop if it reaches the end of file
            loop = False
        elif instruction == "PRINT":   # PRINT FUNCTION
            do_PRINT(byc,index)        # Pass the bytestack and the current index to do_PRINT
        #elif instruction == "ADD":

        #elif instruction == "SUB:

            #elif instruction == "MUL":

            #elif instruction == "DIV":

            #elif instruction == "EQUAL":
        index+=1

    os.remove(byte)                     #Deletes Bytecode File
    return 0

def do_PRINT(byc,i):                    # PRINT FUNCTION
    if byc[i+1]=="DOUBLEQUOTE":         # Check if the next index is a string quote
        print get_quoteString(byc,i+1)  # Pass the bytestack and the next index after DOUBLEQUOTE
    #else                               # (incomplete) for saved variable printing
    return 0

def do_ADD(byc,i):
    return int(byc[i-1])+int(byc[i+1])

def do_SUB(byc,i):
    return int(byc[i-1])-int(byc[i+1])

def do_MUL(byc,i):
    return int(byc[i-1])*int(byc[i+1])

def do_DIV(byc,i):
    int(byc[i-1])/int(byc[i+1])

def do_VAR(var):                        # SAVE VARIABLE FUNCTION
    variable.update({var:None})
    print variable
    return 0

def get_VAR(var):                       # GET VARIABLE FUNCTION
    return variable.get(var)

def get_quoteString(byte, index):       # Get string enclosed by DOUBLEQUOTE
    i = index + 1
    quoteString = ""
    while byte[i]!="DOUBLEQUOTE":
        quoteString = quoteString+" "+byte[i]
        i+=1
    return quoteString

def read(src):
    f = open(src)
    lines = f.read()
    lines = lines.replace("\n"," ")
    f.close()
    return lines

def write(byte,argv):
    f = open(argv,"a")
    f.write(byte)
    f.close()

def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)
