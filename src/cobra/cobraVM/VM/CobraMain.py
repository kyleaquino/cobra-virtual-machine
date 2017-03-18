import sys
import Interpreter

class Cobra:

    def main(argv):
        try:
            f=open(argv[1])
        except IOError:
            print "ERROR: No such file or directory"
            return 0
        except IndexError:
            print "ERROR: Input source code argument (ex. python CobraMain.py test.cob)"
            return 0

        Interpreter.run(argv[1])

    def target(*args):
    	return main, None

    if __name__ == '__main__':
    	main(sys.argv)
