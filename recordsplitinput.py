from recordinput import recordandsave
import sys

def recordinputs(name):

	for i in range(1000):
		filename = name + "-" + str(i) + ".wav"
		print filename
		record(filename)
		
if __name__ == '__main__':
	recordinputs(sys.argv[1]) 