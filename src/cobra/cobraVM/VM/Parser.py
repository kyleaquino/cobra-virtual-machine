import SourceReader

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
restricted_keyword_io = loops + conditionalOperator + logicalOperator

def parse(source,tokens):
    tokens = tokens.split();
    checkTokens(tokens)
    return generateBytecode(source,tokens)

def checkTokens(tokens): # Code Recoginition method of the virtual machine

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
            check_conditional(tokens,i)
        elif tok in loops:
            check_loop(tokens,i+1)

def generateBytecode(source, tokens):
    return SourceReader.write(source,tokens)

def check_var(tokens,i):
    expression = getExpression(tokens,i,"SEMICOLON")
    print expression
    for i, tok in enumerate(expression):
        if if_restricted_keyword_var(tok):
            exit("ERROR: Cannot use system-defined keyword ("+bytecode.get(tok)+") in line: "+ getOriginalExpression(expression))
        elif if_Equals(tok,expression,i):
            exit("ERROR: There is an argument missing in : ("+bytecode.get(tok)+") in line: "+ getOriginalExpression(expression))
        elif if_Var(tok, expression):
            exit("ERROR: Cannot use keyword VAR in line: "+ getOriginalExpression(expression))


def check_io(tokens,i):
    expression = getExpression(tokens,i,"SEMICOLON")

    for tok in expression:
        if if_restricted_keyword_io(tok):
            exit("ERRROR: Cannot use a system-defined keyword ("+bytecode.get(tok)+"): "+ getOriginalExpression(expression))
        elif if_Scan(tok,expression):
            exit("ERRROR: Syntax Error in ("+bytecode.get(tok)+"): "+ getOriginalExpression(expression))
        elif if_Print(tok,expression):
            exit("ERRROR: Syntax Error in ("+bytecode.get(tok)+"): "+ getOriginalExpression(expression))


def check_arithmetic(tokens,i):
    expression = getExpression(tokens,i,"SEMICOLON")
    return 0

def check_logical(tokens,i):
    expression = getExpression(tokens,i,"SEMICOLON")
    return 0

def check_conditional(tokens,i):
    expression = getExpression(tokens,i,"SEMICOLON")
    return 0

def check_loop(tokens,i):
    expression = getExpression(tokens,i,"SEMICOLON")
    return 0

def refactor_quote(tokens): # Refactor mistaken keywords inside string keyword
    loop = 1
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

def getExpression(tokens,i,terminator):     # Get substring expression
    index = 0
    if terminator in tokens:
        tokens=tokens[i:len(tokens)+1]      # Splice list from the start index forward
        index = tokens.index(terminator)    # Get terminator index
        return tokens[0:index+1]            # Return list from start index to terminator index
    else:
        exit("ERROR: Missing ; (semicolon)")

def getOriginalExpression(expression):      # Revert bytecode to source code
    for i, tok in enumerate(expression):
        for byte in bytecode:
            if tok == byte:                 # If token macthed byte revert it to source code
                expression[i] = bytecode.get(tok)

    return " ".join(expression)             # Return reverted code as one string

def if_restricted_keyword_var(tok):  # ERROR! if expression have a restricted keyword
    if tok in restricted_keyword_var:
        return True
    else:
        return False

def if_restricted_keyword_io(tok):  # ERROR! if expression have a restricted keyword
    if tok in restricted_keyword_io:
        return True
    else:
        return False

def if_Equals(tok,expression,i): # ERROR!  if there is variable name or value
    if tok == "EQUALS":
        if expression[i-1] == var or expression[i+1] == semicolon:
            return True
    else:
        return False

def if_Var(tok, expression): # ERROR! if var keyword called twice
    if tok == "VAR":
        if expression.count("VAR") == 1:
            return False
        else:
            return True
    else:
        return False

def if_Scan(tok,expression):
    if tok == "SCAN":
        if expression.count("SCAN") == 1:
            return False
        else:
            return True
    else:
        return False

def if_Print(tok,expression):
    if tok == "PRINT":
        if expression.count("PRINT") == 1:
            return False
        else:
            return True
    else:
        return False
