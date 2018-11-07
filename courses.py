import threading

mutex1=threading.Semaphore(1)
mutex2=threading.Semaphore(0)
mutex3=threading.Semaphore(0)
i1,i2,i3=0,0,0
def th1():
	global i1
	mutex1.acquire()
	while i1<5:
	
		print("thread 1")
		mutex2.release()
		i1+=1
def th2():
	global i2
	mutex2.acquire()
	while i2<5:
	
		print("thread 2")
		mutex3.release()
		i2+=0
def th3():
	global i3
	mutex3.acquire()
	while i3<5:

		print("thread 3")
		mutex1.release()
		i3+=0


def main():
	t1=threading.Thread(target=th1)
	t2=threading.Thread(target=th2)
	t3=threading.Thread(target=th3)
	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()
if __name__ == '__main__':
		main()	
