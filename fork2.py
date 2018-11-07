import os

print("hello")

pid=os.fork()

if pid==0:
	print("jes suis le fils ",os.getpid())
	os._exit(100)
else:
	pidx,status=os.wait()
	print("le pere")
	status=status>>8
	print("ok {} et {}".format(pidx,status))	

	
'''a 16-bit number, whose low byte is the signal number that 
   killed the process, and whose high byte is the exit status
'''
