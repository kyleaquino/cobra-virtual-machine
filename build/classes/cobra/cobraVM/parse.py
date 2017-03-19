import byte

var = []
val = []

def do_OUT(split):
        st=""
        if split[1] in var:
            var_index = var.index(split[1])
            st+= val[var_index]
        elif split[1]=="ALL":
                for i in var:
                        print i +"="+str(val[var.index(i)])
        else:    
            print str(split[1])
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
                ans+=x
        #print ans
        return ans
        
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
                ans-=x
        #print ans
        return ans

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
        #print ans
        return ans

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
        #print ans
        return ans
    
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
        #print ans
        return ans

def do_ASG(split):
        global var
        global val
        func = "04","05","06","07","01","08"
        asg = 0
        token = split
        if token[0] in var:
                if token[1] in var:
                        tmp = var.index(token[1])
                        val[var.index(token[0])]=val[tmp]
                else:
                        #print str(token[0])+":token[0]"
                        val[var.index(token[0])]=token[1]
        else:
                if token[1] in func:
                        string = token[1:]
                        string = str('>>'.join(string))
                        string = string.split()
                        string.append("00")
                        #print "this is asgn:"+str(string)
                        asg = byte.execute_program(string)
                        #print "asg:" + str(asg)
                        var.append(token[0])
                        val.append(str(asg))
                elif token[1].isdigit():
                        var.append(token[0])
                        val.append(token[1])
        #print var
        #print val
                        
def do_FOR(split):
        count = int(split[1])
        loop = 0
        string=""
        string +=str(split[2])+">>"+str(split[3])
        string = string.split("\n")
        string.append("END")
        #string.append(split[2])
        #string.append(split[3])
        #print string
        for x in range(count):
                byte.execute_program(string)
def do_SCN(split):
        global var,val
        var.append(split[1])
        String = raw_input("String: ")
        val.append(String)

