import threading
a=0
lock=threading.Semaphore(1)

def inc():
	global a,lock

	lock.acquire()
	for x in range(1000000):
		a=a+1
	lock.release()


def main():
	#global a,lock
	#lock=threading.Lock()
	#a=0
	print('we start a = ',a)
	t1=threading.Thread(target=inc,name='t1')
	t2=threading.Thread(target=inc,name='t2')
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	print('fin  a = ',a)
if __name__ == '__main__':
				main()			

