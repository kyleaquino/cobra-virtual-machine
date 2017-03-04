import sys
import parser

OP_EOP = "END"
OP_PRINT = "PRNT"
OP_ADD = "ADD"
OP_SUB = "SUB"
OP_MUL = "MUL"
OP_DIV = "DIV"
OP_OUT = "OUT"
OP_MOD = "MOD"
OP_ASG = "ASGN"

def execute_program(l):
	loop = 1
	i = 0
	while loop:
                split = l[i].split(">>")
                
		instruction = split[0]
		print split[0]
                if instruction == OP_EOP:
			loop = 0
		elif instruction== OP_ADD:
			parser.do_ADD(split)
		elif instruction== OP_SUB:
			parser.do_SUB(split)
		elif instruction== OP_MUL:
			parser.do_MUL(split)
		elif instruction== OP_DIV:
			parser.do_DIV(split)
		elif instruction== OP_OUT:
			parser.do_OUT(split)
		elif instruction== OP_MOD:
			parser.do_MOD(split)
		elif instruction== OP_ASG:
			parser.do_ASG(split)	
		i += 1

