import sys

var = []
val = []

OP_PRINT = "PRNT"
OP_ADD = "ADD" 
OP_SUB = "SUB"
OP_MUL = "MUL"
OP_DIV = "DIV"
OP_OUT = "OUT"
OP_MOD = "MOD"
OP_ASG = "ASGN"

def load_program(argv):
	f = open(argv)
	lines = f.read().replace("\n"," ")
	lines = lines.split()
	print lines
	f.close()
	return lines

def execute_program(l):
	loop = 1
	i = 0
	while loop:
                split = l[i].split(">>")
                
		instruction = split[0]
		
                if instruction == split[-1]:
			loop = 0
		elif instruction== OP_ADD:
			do_ADD(split)
		elif instruction== OP_SUB:
			do_SUB(split)
		elif instruction== OP_MUL:
			do_MUL(split)
		elif instruction== OP_DIV:
			do_DIV(split)
		elif instruction== OP_OUT:
			do_OUT(split)
		elif instruction== OP_MOD:
			do_MOD(split)
		else:
                        do_ASG(split)
                        
		i += 1



def do_OUT(split):
        st=""
        if split[1] in var:
            var_index = var.index(split[1])
            st+= val[var_index]
        else:    
            st+=split[1]
        print st
        
def do_ADD(split):
    ans = 0
    split[1]=split[1].split(",")
    split[1]=map(int,split[1])
    for x in split[1]:
        ans+=x
    print ans
        
def do_SUB(split):
    ans = 0
    split[1]=split[1].split(",")
    split[1]=map(int,split[1])
    for x in split[1]:
        ans=ans-x
    print ans

def do_MUL(split):
    ans = 1
    split[1]=split[1].split(",")
    split[1]=map(int,split[1])
    for x in split[1]:
        ans=ans*x
    print ans

def do_DIV(split):
    ans = 1.0
    split[1]=split[1].split(",")
    split[1]=map(int,split[1])
    for x in split[1]:
        ans=ans/x
    print ans
    
def do_MOD(split):
    ans = 1
    split[1]=split[1].split(",")
    split[1]=map(int,split[1])
    for x in split[1]:
        ans=ans%x
    print ans

def do_ASG(split):
    global var
    global val
    token = split
    print token
    var.append(token[0])
    val.append(token[1])


def run_program(argv):
	l = load_program(argv)
	execute_program(l)

def main(argv):
	run_program(argv[1])
	return 0

def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)
