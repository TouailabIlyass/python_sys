import os




print("hello")


for i in range(0,3):
	p=os.fork()
	if p>0:
		break
	print("fils pid={0} avec pere pid={1}".format(os.getpid(),os.getppid()))
if p>1:
   os.wait()
print("fin ",os.getpid())	