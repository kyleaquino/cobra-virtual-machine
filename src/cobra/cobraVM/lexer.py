import sys
import byte

def load_program(argv):
        lines = argv
	lines = lines.split("\n")
	#print lines
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

