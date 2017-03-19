import SourceReader
import Lexer
import Parser

def run(source):
    src = SourceReader.readSource(source)   # Pass string of source file to variable src
    tokens = Lexer.tokenize(src)            # Tokenize the string through lexer function
    bytecode = Parser.parse(source,tokens)  # Generate bytecode file
    execute(bytecode)                       # Execute program using the bytecode file

def execute(byc): # Mimic parser functions but for only direct running of functions
    bytecode = SourceReader.readByte(byc)

    for i, byte in enumerate(bytecode):

        if byte == "VAR":
            do_VAR(byc,i)
        elif byte == "PRINT":
            return 0
        elif byte == "SCAN":
            return 0

def do_VAR(byc,i):
    expr = Parser.getExpression(byc,i,"SEMICOLON")

def do_PRINT(byc,i):
    expr = Parser.getExpression(byc,i,"SEMICOLON")
    return 0

def do_SCAN(byc,i):
    expr = Parser.getExpression(byc,i,"SEMICOLON")
    return 0
