import sys
import Interpreter

def main(argv):                             # Cobra Virtual Machine Entry Point
    try:                                    # Try to Open file
        f=open(argv[1])
    except IOError:                         # Stop program if there is no file
        exit("ERROR: No such file or directory")
    except IndexError:                      # Stop program if there is no file argument
        exit("ERROR: Input source code argument (ex. python CobraMain.py test.cob)")
    if ".cob" in argv[1]:                   # Pass source code argument to interpeter
        Interpreter.run(argv[1])
    else:                                   # Stop program if file is not a .cob source file
        exit("ERROR: "+ argv[1] +" not a Cobra++ source sode")

def target(*args):
	return main, None

if __name__ == '__main__':
	main(sys.argv)
