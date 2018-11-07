import os

a=2

print(a)
pid=os.fork()

if pid==0:
	a+=10
	print("le fils ",a)
else:
	a+=20
	#os.execlp("ps","xf")
	print("le pere ",a)


print(a)
txt=b"hello world"
os.write(1,b"oui")
os.write(1,txt)
