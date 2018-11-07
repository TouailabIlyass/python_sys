import threading


#print(threading.activeCount())
#print(threading.enumerate())
#print(threading.currentThread())

def th1():
	print('thread 1')
	print(threading.enumerate())
def th2():

	print('thread 2')
	print(threading.enumerate())

def main():
	t1=threading.Thread(target=th1,name='ok')
	t2=threading.Thread(target=th2,name='2')
	t1.start()
	t2.start()
	print(threading.enumerate())


if __name__ == '__main__':
				main()			