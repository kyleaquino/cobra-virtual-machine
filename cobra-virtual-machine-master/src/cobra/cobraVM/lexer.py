import sys
import byte

stack = []
count = 0
forend = 0
forstart = 0
times = 0
ls = []
point = 0
funcs={"END","PUSH","RMV","PRNT","ADD","SUB","MUL","DIV","OUT","MOD","START.FOR","END.FOR","ASGN"}


OP_EOP = NULL
OP_PRINT = "PRNT"
OP_ADD = "ADD"
OP_SUB = "SUB"
OP_MUL = "MUL"
OP_DIV = "DIV"
OP_OUT = "OUT"
OP_MOD = "MOD"
OP_ASG = "ASGN"

def load_program(argv):
	f = open(argv)
	lines = f.read().replace("\n"," ")
	lines = lines.split()
	print lines
	f.close()
	return lines

def run_program(argv):
	l = load_program(argv)
	byte.execute_program(l)

def main(argv):
	run_program(argv[1])
	return 0

def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)
