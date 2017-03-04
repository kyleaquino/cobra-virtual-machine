var = []
val = []

def do_OUT(split):
        st=""
        if split[1] in var:
            var_index = var.index(split[1])
            st+= val[var_index]
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

def do_ASGN(split):
    global var
    global val
    split=split.split(">>")
    var.append(split[1])
    val.append(split[2])
