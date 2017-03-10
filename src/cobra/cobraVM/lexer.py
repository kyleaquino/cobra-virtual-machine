import sys
import token

def load_program(argv):
	f = open(argv)
	lines = f.read().replace("\n"," ")
	lines = lines.split()
	print lines
	f.close()
	return lines

def run_program(argv):
	l = load_program(argv)
	token.execute_program(l)

def main(argv):
	run_program(argv[1])
	return 0

def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)

