import SourceReader
import Lexer
import Parser

def run(source):
    src = SourceReader.read(source)         # Pass string of source file to variable src
    tokens = Lexer.tokenize(src)            # Tokenize the string through lexer function
    bytecode = Parser.parse(source,tokens)  # Generate bytecode file
    #execute(bytecode)                      # Execute program using the bytecode file

def execute(byc): # Mimic parser functions but for only direct running of functions
    return 0
