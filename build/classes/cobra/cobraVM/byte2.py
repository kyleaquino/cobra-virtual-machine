import sys
import lexer 

bytecode = "END","OUT","FOR","SCN"
bytecode2 = "ADD","SUB","MUL","DIV","MOD"

def main(argv):
    source = read(argv[1])
    byte = bc(source)
    write(byte,argv[1])
    return byte

def read(src):
    f = open(src)
    lines = f.read().split("\n")
    f.close()
    return lines

def bc(source):
    str = ""
    str2 = ""
    for i in source:
        i = i.split(">>")
        if i[0] in bytecode:
            if i[0] == "END":
                str += "00" + "\n"
            elif i[0] == "OUT": 
                str += "01>>"
                if i[1] in bytecode2:
                    if i[1] == "ADD":
                        str += "04>>" + i[2]+"\n"
                    elif i[1] == "SUB":
                        str += "05>>" + i[2]+"\n"
                    elif i[1] == "MUL":
                        str += "06>>" + i[2]+"\n"
                    elif i[1] == "DIV":
                        str += "07>>" + i[2]+"\n"
                    elif i[1] == "MOD":
                        str += "08>>" + i[2]+"\n"
                else:
                    str += i[1]+"\n"
            elif i[0] == "FOR":
                str += "02>>" + i[1]+ ">>"
                if i[2] == "OUT":
                    str += "01>>" + i[3]+"\n"
            elif i[0] == "SCN":
                    str += "03>>" + i[1]+"\n"
        else :
            if i[1] in bytecode2:
                #print i[2]
                str += i[0] + ">>"
                if i[1] == "ADD":
                    str += "04>>" + i[2]+"\n"
                elif i[1] == "SUB":
                    str += "05>>" + i[2]+"\n"
                elif i[1] == "MUL":
                    str += "06>>" + i[2]+"\n"
                elif i[1] == "DIV":
                    str += "07>>" + i[2]+"\n"
                elif i[1] == "MOD":
                    str += "08>>" + i[2]+"\n"
            else:
                str += i[0] + ">>" + i[1] + "\n"
    print str
    return str
    
def write(byte,argv):
    argv = argv.replace(".vm","")
    f = open(argv+".byc","w+")
    f.write(byte)
    f.close()

if __name__ == '__main__':
    main(sys.argv)
