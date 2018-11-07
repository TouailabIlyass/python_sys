import os

os.fork()
print("je suis un proccessus mon pid = ",os.getpid())



'''
def child():
	print(' A new child  ',os.getpid())
	print(' son pere est ',os.getppid())
	
	os._exit(0)

def parent():
	print('parent ',os.getpid())
	os._exit(0)

def main():

	pid=os.fork()
	if pid==0:
		child()
	else:
		parent()
if __name__ == '__main__':
					main()

'''
