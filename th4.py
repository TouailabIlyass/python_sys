import threading,sys,time


def afficher(a,c):
	i=0
	
	while i<a:
		j=0
		while j<1000000:
			j+=1
			
		print(c,end='')
		i+=1


def thA():

	afficher(10,'A')
	print('fin du thread A')

def thC():

	afficher(10,'C')
	print('fin du thread C')

def thB():
	tc=threading.Thread(name='tC',target=thC)
	tc.start()
	afficher(10,'B')
	print('thB attend la fin du thread C')
	tc.join()
	print('fin du thread C')

def main():

	tA=threading.Thread(target=thA,name='tA')
	tB=threading.Thread(target=thB,name='tB')
	tA.start()
	tB.start()
	time.sleep(1)
	print('main attend A et B')
	tA.join()
	tB.join()
	sys.exit(0)

if __name__ == '__main__':
	main()

