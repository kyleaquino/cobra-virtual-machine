import parse

#OP_PRINT = "PRNT"
#OP_ADD = "ADD" 
#OP_SUB = "SUB"
#OP_MUL = "MUL"
#OP_DIV = "DIV"
#OP_OUT = "OUT"
#OP_MOD = "MOD"
#OP_ASG = "ASGN"
#OP_FOR = "FOR"
#OP_SCN = "SCN"

OP_OUT = "00"
OP_SCN = "01"
OP_ADD = "02" 
OP_SUB = "03"
OP_MUL = "04"
OP_DIV = "05"
OP_MOD = "06"
OP_ASG = "07"
OP_FOR = "08"
OP_IF = "09"
OP_ELSE = "10"
OP_ELF = "11"
OP_WHILE = "12"

def execute_program(l):
	loop = 1
	i = 0
	while loop:
                split = l[i].split(">>")
                
		instruction = split[0]
		
                if instruction == split[-1]:
			loop = 0
		elif instruction== OP_ADD:
			parse.do_ADD(split)
		elif instruction== OP_SUB:
			parse.do_SUB(split)
		elif instruction== OP_MUL:
			parse.do_MUL(split)
		elif instruction== OP_DIV:
			parse.do_DIV(split)
		elif instruction== OP_OUT:
			parse.do_OUT(split)
		elif instruction== OP_MOD:
			parse.do_MOD(split)
		elif instruction== OP_FOR:
			parse.do_FOR(split)
		elif instruction== OP_SCN:
			parse.do_SCN(split)
		else:
                        parse.do_ASG(split)
                        
		i += 1
