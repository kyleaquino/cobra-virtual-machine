import sys
import lexer
import byte2

def main(argv):
        try:
                LOC = byte2.main(argv)
                lexer.run_program(LOC)
                return 0
        except IOError:
                exit("No File")
        except IndexError:
                exit("Unexpected Error. Check if File has [END] Function or Spaces between lines.")
def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)
