import signal,os,time

def action(signum,a):
	print("sign recv ",signum,a)


def main():
	signal.signal(signal.SIGUSR1,action)
	print('my pid is : ',os.getpid())
	while True:
		print("waiting")
		time.sleep(3)

if __name__ == '__main__':
			main()		

