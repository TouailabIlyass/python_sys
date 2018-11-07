import os,signal,time


p=os.fork()

if(p==0):
	i=0
	while i<10:
		
		print('child ....',end="")
		
		i+=1
	print("fin")
	time.sleep(1)
	print(os.getppid())
else:
	os.kill(p,19)
	print('proccessus fils stop',os.getpid())
	time.sleep(5)
	os.kill(p,18)
	
	
	
	