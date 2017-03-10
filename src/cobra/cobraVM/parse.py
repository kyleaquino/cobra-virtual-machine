
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
OP_FOR = "FOR"
OP_SCN = "SCN"

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
        dis = 0
        c = 0
        split[1]=split[1].split(",")
        if(split[1][0] in var):
                        var_index = var.index(split[1][0])
                        y = val[var_index]
                        y = int(y)
                        ans = y
        else:
                ans = int(split[1][0])
        print "Answer: "
        print ans
        for x in split[1][1:]:
                print x
                if(x.isdigit()):
                        x = int(x)
                if(x in var):
                        var_index = var.index(x)
                        y = val[var_index]
                        y = int(y)
                        x = y
                ans+=x
        print ans
        
def do_SUB(split):
        ans = 0
        dis = 0
        c = 0
        split[1]=split[1].split(",")
        if(split[1][0] in var):
                        var_index = var.index(split[1][0])
                        y = val[var_index]
                        y = int(y)
                        ans = y
        else:
                ans = int(split[1][0])
        print "Answer: "
        print ans
        for x in split[1][1:]:
                print x
                if(x.isdigit()):
                        x = int(x)
                if(x in var):
                        var_index = var.index(x)
                        y = val[var_index]
                        y = int(y)
                        x = y
                ans-=x
        print ans

def do_MUL(split):
        ans = 0
        dis = 0
        c = 0
        split[1]=split[1].split(",")
        if(split[1][0] in var):
                        var_index = var.index(split[1][0])
                        y = val[var_index]
                        y = int(y)
                        ans = y
        else:
                ans = int(split[1][0])
        #print "Answer: "
        #print ans
        for x in split[1][1:]:
                #print x
                if(x.isdigit()):
                        x = int(x)
                if(x in var):
                        var_index = var.index(x)
                        y = val[var_index]
                        y = int(y)
                        x = y
                ans*=x
        print ans

def do_DIV(split):
        ans = 0
        dis = 0
        c = 0
        split[1]=split[1].split(",")
        if(split[1][0] in var):
                        var_index = var.index(split[1][0])
                        y = val[var_index]
                        y = int(y)
                        ans = y
        else:
                ans = float(split[1][0])
        #print "Answer: "
        #print ans
        for x in split[1][1:]:
                #print x
                if(x.isdigit()):
                        x = float(x)
                if(x in var):
                        var_index = var.index(x)
                        y = val[var_index]
                        y = float(y)
                        x = y
                ans/=x
        print ans
      
    
def do_MOD(split):
        ans = 0
        dis = 0
        c = 0
        split[1]=split[1].split(",")
        if(split[1][0] in var):
                        var_index = var.index(split[1][0])
                        y = val[var_index]
                        y = int(y)
                        ans = y
        else:
                ans = int(split[1][0])
        #print "Answer: "
        #print ans
        for x in split[1][1:]:
                #print x
                if(x.isdigit()):
                        x = int(x)
                if(x in var):
                        var_index = var.index(x)
                        y = val[var_index]
                        y = int(y)
                        x = y
                ans%=x
        print ans

def do_ASG(split):
        global var
        global val
        token = split
        print token
        var.append(token[0])
        val.append(token[1])
def do_FOR(split):
        count = int(split[1])
        loop = 0
        string = []
        string.append(split[2])
        string.append(split[3])
        print string
        for x in range(count):
                instruction = string[0]
                if instruction== OP_ADD:
			do_ADD(string)
		elif instruction== OP_SUB:
			do_SUB(string)
		elif instruction== OP_MUL:
			do_MUL(string)
		elif instruction== OP_DIV:
			do_DIV(string)
		elif instruction== OP_OUT:
			do_OUT(string)
		elif instruction== OP_MOD:
			do_MOD(string)
def do_SCN(split):
        global var,val
        var.append(split[1])
        String = raw_input("String: ")
        val.append(String)

