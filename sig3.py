import signal,os,time

def action(si,a):
	print("hello")
	for x in range(1,10):
		print(x)

signal.signal(signal.SIGINT,action)
s=os.getpid()
print(s)


signal.pause()
#os.kill(s,19)

print("finish")