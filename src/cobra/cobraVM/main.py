import sys
import lexer
import byte2

def main(argv):
        LOC = byte2.main(argv)
	lexer.run_program(LOC)
	return 0

def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)
