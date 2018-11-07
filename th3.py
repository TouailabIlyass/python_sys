import threading

a=0
l=threading.Lock()
def inc():
	global a,l
	l.acquire()
	r=a
	for x in range(1000000):
		pass
	a=r+1
	l.release()
	print('th1 a = ',a)

def dec():
	global a,l
	l.acquire()
	r=a
	for x in range(1000000):
		pass
	a=r-1
	l.release()
	print('th2 a = ',a)
def main():
	t1=threading.Thread(target=inc)
	t2=threading.Thread(target=dec)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('fin a = ',a)	
				
if (__name__=='__main__'):
	main()				