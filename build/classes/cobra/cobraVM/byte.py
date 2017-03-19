import parse


OP_ADD = "04" 
OP_SUB = "05"
OP_MUL = "06"
OP_DIV = "07"
OP_OUT = "01"
OP_MOD = "08"
OP_FOR = "02"
OP_SCN = "03"
OP_IFF = "09"
OP_WHL = "10"


func = "04","05","06","07","01","08","02","03","09","10"

def execute_program(l):
	loop = 1
	i = 0
	tmp = 0
	forloop = 1
	ifloop = 1
	forstring=""
	ifstring=""
	whl = 0
	while loop:
                split = l[i].split(">>")
		instruction = split[0]
                if instruction == split[-1]:
			loop = 0
		elif instruction== OP_ADD:
			tmp=parse.do_ADD(split,i)
		elif instruction== OP_IFF:
                        i += 1
                        whl=i
                        while ifloop:
                                ifsplit=l[i]
                                if ifsplit== "<<":
                                        ifloop = 0
                                else:
                                        ifstring += str(ifsplit)+"\n"
                                
                                i+=1
                        i-=1
                        parse.do_IF(split,ifstring,whl)
		elif instruction== OP_SUB:
			tmp=parse.do_SUB(split,i)
		elif instruction== OP_MUL:
			tmp=parse.do_MUL(split,i)
		elif instruction== OP_DIV:
			tmp=parse.do_DIV(split,i)
		elif instruction== OP_OUT:
			tmp=parse.do_OUT(split,i)
		elif instruction== OP_MOD:
			tmp=parse.do_MOD(split,i)
		elif instruction== OP_FOR:
                        i += 1
                        while forloop:
                                forsplit=l[i]
                                if forsplit== "<<":
                                        forloop = 0
                                else:
                                        forstring += str(forsplit)+"\n"
                                
                                i+=1
                        i-=1
			parse.do_FOR(split,forstring,i)
		elif instruction== OP_SCN:
			parse.do_SCN(split,i)
		elif instruction not in func:
                        parse.do_ASG(split,i)
                        
		i += 1
        return tmp
