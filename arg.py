import sys,os


def main():
	print("number of arg : ",len(sys.argv))
	print('is : ',str(sys.argv),sys.argv[1])
	os.execlp(sys.argv[1],sys.argv[1],sys.argv[2])
	print('fin')
if __name__ == '__main__':
	main()