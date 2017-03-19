import byte
import lexer

var = []
val = []

def do_OUT(split,loc):  #Prints string or variable
        try:
                st=""
                if split[1] in var:
                    var_index = var.index(split[1])
                    st+= val[var_index]
                elif split[1]=="ALL":  #A keyword in our program used to print all assigned variables and their values
                        for i in var:
                                print i +"="+str(val[var.index(i)])
                else:
                    print str(split[1])
                print st
        except ValueError:
                exit("OUT, Cannot convert from String to Int: " + str(loc+1))
        except:
                exit("OUT, Unexpected Error: " + str(loc+1))

def do_ADD(split,loc):  #Adds variable or integers separated by comma
        try:
                ans = 0
                dis = 0
                c = 0
                split[1]=split[1].split(",")
                if(split[1][0] in var):   # Checks if the first value declared is in the variable, it then assigns it as the first value that will change
                                var_index = var.index(split[1][0])
                                y = val[var_index]
                                y = int(y)
                                ans = y
                else:
                        ans = int(split[1][0])

                for x in split[1][1:]: # Checks if the next declared values are variables with assigned values
                        if(x.isdigit()):
                                x = int(x)
                        if(x in var):
                                var_index = var.index(x)
                                y = val[var_index]
                                y = int(y)
                                x = y
                        ans+=x

                return ans
        except ValueError:
                exit("ADD, Cannot Add String value to Integer: " +str(loc+1))
        except:
                exit("ADD, Unexpected Error: " +str(loc+1))

def do_SUB(split,loc): # Subtracts variable or integers separated by comma
        try:
                ans = 0
                dis = 0
                c = 0
                split[1]=split[1].split(",")
                if(split[1][0] in var):# Checks if the first value declared is in the variable, it then assigns it as the first value that will change
                                var_index = var.index(split[1][0])
                                y = val[var_index]
                                y = int(y)
                                ans = y
                else:
                        ans = int(split[1][0])

                for x in split[1][1:]:  # Checks if the next declared values are variables with assigned values

                        if(x.isdigit()):
                                x = int(x)
                        if(x in var):
                                var_index = var.index(x)
                                y = val[var_index]
                                y = int(y)
                                x = y
                        ans-=x

                return ans
        except ValueError:
                exit("SUB, Cannot Subtract String value to Intger: " +str(loc+1))
        except:
                exit("SUB, Unexpected Error: " +str(loc+1))

def do_MUL(split,loc):  #Multiplies variable or integers separated by comma
        try:
                ans = 0
                dis = 0
                c = 0
                split[1]=split[1].split(",")
                if(split[1][0] in var):  # Checks if the first value declared is in the variable, it then assigns it as the first value that will change
                                var_index = var.index(split[1][0])
                                y = val[var_index]
                                y = int(y)
                                ans = y
                else:
                        ans = int(split[1][0])

                for x in split[1][1:]: # Checks if the next declared values are variables with assigned values
                        if(x.isdigit()):
                                x = int(x)
                        if(x in var):
                                var_index = var.index(x)
                                y = val[var_index]
                                y = int(y)
                                x = y
                        ans*=x

                return ans
        except ValueError:
                exit("MUL, Cannot Multiply String value to Integer: " +str(loc+1))
        except:
                exit("MUL, Unexpected Error: " +str(loc+1))

def do_DIV(split,loc): # Divides the first variable inserted by the user up to the last input by the user separated by comma
        try:
                ans = 0
                dis = 0
                c = 0
                split[1]=split[1].split(",")
                if(split[1][0] in var): # Checks if the first value declared is in the variable, it then assigns it as the first value that will change
                                var_index = var.index(split[1][0])
                                y = val[var_index]
                                y = int(y)
                                ans = y
                else:
                        ans = float(split[1][0])

                for x in split[1][1:]:
                        if(x.isdigit()):
                                x = float(x)
                        if(x in var):
                                var_index = var.index(x)
                                y = val[var_index]
                                y = float(y)
                                x = y
                        ans/=x

                return ans
        except ValueError:
                exit("DIV, Cannot Divige String Value to Integer: " + str(loc+1))
        except:
                exit("DIV, Unexpected Error: " +str(loc+1))

def do_MOD(split,loc):# Finds the remainder of the first variable or integer inserted by the user from the next up to the last value inserted by the user
        try:
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
                for x in split[1][1:]:
                        if(x.isdigit()):
                                x = int(x)
                        if(x in var):
                                var_index = var.index(x)
                                y = val[var_index]
                                y = int(y)
                                x = y
                        ans%=x
                return ans
        except ValueError:
                exit("MOD, Cannot get remainder from String value to integer: " + str(loc+1))
        except:
                exit("MOD, Unexpected Error: " +str(loc+1))

def do_ASG(split,loc):
        try:
                global var
                global val
                func = "04","05","06","07","01","08"
                asg = 0
                token = split
                if token[0] in var:
                        if token[1] in var:
                                tmp = var.index(token[1])
                                val[var.index(token[0])]=val[tmp]
                        elif token[1] in func:
                                string = token[1:]
                                string = str('>>'.join(string))
                                string = string.split()
                                string.append("00")
                                asg = byte.execute_program(string)
                                tmp = var.index(token[0])
                                val[var.index(token[0])]=str(asg)
                        else:
                                val[var.index(token[0])]=token[1]
                else:
                        if token[1] in func:
                                string = token[1:]
                                string = str('>>'.join(string))
                                string = string.split()
                                string.append("00")
                                asg = byte.execute_program(string)
                                var.append(token[0])
                                val.append(str(asg))
                        elif token[1].isdigit():
                                var.append(token[0])
                                val.append(token[1])

        except IndexError:
                exit("Variable, Variable not Found: " + str(loc+1))
        except ValueError:
                exit("Variable, Cannot perform task assigned to variable: " +str(loc+1))
        except:
                exit("Variable Function Error, Please Check line: " +str(loc+1))

def do_FOR(split,stringz,loc):
        try:
                count = int(split[1])
                for x in range(count):
                        lexer.run_program(stringz)
        except ValueError:
                exit("FOR, Check variable assignment: " +str(loc+1))
        except:
                exit("FOR, Unexpected Error: " +str(loc+1))
def do_SCN(split,loc):
        try:
                global var,val
                var.append(split[1])
                String = raw_input()
                val.append(String)
        except:
                exit("SCAN, Unexpected Error: " +str(loc+1))
def do_IF(split,string,loc):
        try:
                ifstring = ""
                tmp = 0
                raw_if = split[1].split(",")
                if raw_if[0] in var:
                        tmp = var.index(raw_if[0])
                        ifstring+= str(val[tmp])+str(raw_if[1])
                        if raw_if[2] in var:
                                tmp = var.index(raw_if[2])
                                ifstring+= str(val[tmp])
                        else:
                                ifstring+= str(raw_if[2])
                else:
                        ifstring+= str(raw_if[0])+str(raw_if[1])
                        if raw_if[2] in var:
                                tmp = var.index(raw_if[2])
                                ifstring+= str(val[tmp])
                        else:
                                ifstring+= str(raw_if[2])
                if eval(ifstring):
                        lexer.run_program(string)

        except:
                exit("IF, Unexpected Error: " +str(loc+1))
