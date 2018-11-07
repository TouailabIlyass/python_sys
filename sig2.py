import signal,os,time


def action(signum,stack):
	print("now yes")
	signal.signal(signal.SIGINT,signal.SIG_DFL)


def main():

	signal.signal(signal.SIGINT,signal.SIG_IGN)
	signal.signal(signal.SIGUSR1,action)
	print('my pid is : ',os.getpid())
	while True:
			time.sleep(3)

if __name__ == '__main__':
					main()				