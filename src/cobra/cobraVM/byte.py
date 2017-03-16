import parse


OP_ADD = "04" 
OP_SUB = "05"
OP_MUL = "06"
OP_DIV = "07"
OP_OUT = "01"
OP_MOD = "08"
#OP_ASG = "ASGN"
OP_FOR = "02"
OP_SCN = "03"


func = "04","05","06","07","01","08","02","03"

def execute_program(l):
	loop = 1
	i = 0
	tmp = 0
	while loop:
                #print "BEFORE:"+str(l[i])
                split = l[i].split(">>")
                #print "SPLIT:"+str(split)
		instruction = split[0]
		#print str(split) +":instructions"
                if instruction == split[-1]:
			loop = 0
		elif instruction== OP_ADD:
			tmp=parse.do_ADD(split)
		elif instruction== OP_SUB:
			tmp=parse.do_SUB(split)
		elif instruction== OP_MUL:
			tmp=parse.do_MUL(split)
		elif instruction== OP_DIV:
			tmp=parse.do_DIV(split)
		elif instruction== OP_OUT:
			tmp=parse.do_OUT(split)
		elif instruction== OP_MOD:
			tmp=parse.do_MOD(split)
		elif instruction== OP_FOR:
			parse.do_FOR(split)
		elif instruction== OP_SCN:
			parse.do_SCN(split)
		else:
                        parse.do_ASG(split)
                        
		i += 1
        return tmp
