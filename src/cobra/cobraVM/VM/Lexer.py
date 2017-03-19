import re

statement = {                       # Source code into statement dicitonary
    "+":" PLUS ",
    "-":" MINUS ",
    "*":" TIMES ",
    "/":" DIVIDE ",
    "=":" EQUALS ",
    "\"":" QUOTE ",
    "!=":" NOTEQUALS ",
    ">=":" GREATEREQUALS ",
    "<=":" LESSEREQUALS ",
    "==":" ISEQUALS ",
    ";":" SEMICOLON ",
    "{":" STARTBR ",
    "}":" ENDBR ",
    "(":" STARTPAR ",
    ")":" ENDPAR ",
    "var":" VAR ",
    "print":" PRINT ",
    "scan":" SCAN ",
    "if":" IF ",
    "elif":" ELSEIF ",
    "else":" ELSE ",
    "while":" WHILE ",
    "for":" FOR "
    }

def tokenize(src):
    for key in statement:              # Loop through statements using key
        if key in src:                 # If key is in the file, convert all source code into a statement
            src = src.replace(key,statement.get(key))
    return src                         # Return string line
