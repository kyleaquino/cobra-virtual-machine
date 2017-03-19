# For Refactoring elements inside string quote
bytecode = {
    "PLUS":"+",
    "MINUS":"-",
    "TIMES":"*",
    "DIVIDE":"/",
    "EQUALS":"=",
    "NOTEQUALS":"!=",
    "GREATEREQUALS":">=",
    "LESSEREQUALS":"<=",
    "ISEQUALS":"==",
    "SEMICOLON":";",
    "STARTBR":"{",
    "ENDBR":"}",
    "STARTPAR":"(",
    "ENDPAR":")",
    "VAR":"var",
    "PRINT":"print",
    "SCAN":"scan",
    "IF":"if",
    "ELSEIF":"elif",
    "else":"ELSE",
    "WHILE":"while",
    "FOR":"for"
    }

#Input/Output Keywords
io = [
    "PRINT",
    "SCAN",
    ]

arithmeticOperator = [
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "EQUALS",
    ]

logicalOperator = [
    "NOTEQUALS",
    "GREATEREQUALS",
    "LESSEREQUALS",
    "ISEQUALS",
    ]

conditionalOperator = [
    "IF",
    "ELSEIF",
    "ELSE",
    ]

seperator = [
    "STARTBR",
    "ENDBR",
    "STARTPAR",
    "ENDPAR",
    ]

loops = [
    "WHILE",
    "FOR"
    ]

semicolon = "SEMICOLON"
quote = "QUOTE"
var = "VAR"

restricted_keyword_var = io + loops + conditionalOperator + logicalOperator + seperator

def parse(source,tokens):
    tokens = tokens.split();
    checkTokens(tokens)
    return generateBytecode(tokens)

def checkTokens(tokens):

    if quote in tokens:                     # If there is a String Quote, Revert mistaken keyword conversion
        tokens = refactor_quote(tokens)

    for i,tok in enumerate(tokens):
        if tok == var:
            check_var(tokens,i)
        elif tok in io:
            check_io(tokens,i)
        elif tok in arithmeticOperator:
            check_arithmetic(tokens,i)
        elif tok in logicalOperator:
            check_logical(tokens,i)
        elif tok in conditionalOperator:
            check_coditional(tokens,i)
        elif tok in loops:
            check_loop(tokens,i+1)

def generateBytecode():
    return 0

def check_var(tokens,i):
    expression = getExpression(tokens,i+1,"SEMICOLON")

    for i, tok in enumerate(expression):
        if if_restricted_keyword_var(tok):
            exit("ERROR: Cannot use keyword ",tok," in line: "+ getOriginalExpression(expression))
        elif if_Equals(tok,expression):
            exit("ERROR: There is an argument missing in line: " + tok + " in: "+ getOriginalExpression(expression))
        elif if_Var(tok, expression):
            exit("ERROR: Cannot use keyword VAR in line: "+ getOriginalExpression(expression))


def check_io(tokens,i):
    return 0
    expression = getExpression(tokens,i+1,"SEMICOLON")

    for tok in expression:
        if tok in keyword:
            exit("Cannot use a system-defined keyword(",tok,"):",getOriginalExpression(expression))


    #counter = i
    #loop = 1
    #while loop:
    #    tok = tokens[counter]
    #    if tok in keyword:
    #        exit("ERROR: Keyword: ",tok,"cannot be set as Variable")
    #    elif tok == "EQUALS":
    #        if tokens[counter+1] in keyword:
    #            exit("Cannot assign Keyword: "+tokens[counter+1])
    #    elif tok == "SEMICOLON":
    #        if tokens[counter-1] == "VAR":
    #            Print
    #    counter+=1

def check_arithmetic(tokens,i):
    return 0

def check_logical(tokens,i):
    return 0

def check_coditional(tokens,i):
    return 0

def check_seperator(tokens,i):
    return 0

def check_semicolon(tokens,i):
    return 0

def check_loop(tokens,i):
    return 0

def refactor_quote(tokens): #since lexer converted all keyword into bytecode "1+1=" -> "ONE PLUS ONE EQUALS"
    loop = 1                #including string quote we need to revert the keyword inside "1+1=" -> "1+1="
    count = 0
    firstquote = True
    for i,tok in enumerate(tokens):
        if tok == quote:
            count = i
            while loop:
                if count+1 != len(tokens):
                    break
                if firstquote:
                    if tokens[count+1] == quote:
                        firstquote = False
                        break
                    if tokens[count+1] in bytecode:
                        tokens[count+1] = bytecode.get(tokens[count+1])
                else:
                    count+=1
                    firstquote=True
                count+=1

    return tokens

def getExpression(tokens,i,terminator):
    index = 0
    if terminator in tokens:
        tokens=tokens[i-1:len(tokens)+1] # Splice list from the start index forward
        index = tokens.index(terminator) # Get terminator index
        return tokens[0:index+1]         # return list from start index to terminator index
    else:
        exit("ERROR: Missing ; (semicolon)")

def getOriginalExpression(expression):
    expr = expression
    for i, tok in enumerate(expr):
        for byte in bytecode:
            if tok == byte:
                expr[i] = bytecode.get(tok)

    return " ".join(expr)

def if_restricted_keyword_var(tok):      # ERROR! if expression have a restricted keyword
    return tok in restricted_keyword_var:

def if_Equals(tok,expression):           # ERROR!  if there is variable name or value
    if tok == "EQUALS":
        return expression[i-1] == var or expression[i+1] == semicolon:
    else:
        return False

def if_Var(tok, expression):
    if tok == "VAR":                      # ERROR! if var keyword called twice
        if expression.count("VAR") == 1:
            return True
        else:
            return False
    else:
        return false
