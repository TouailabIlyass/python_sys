import os,sys


r,w=os.pipe()



p=os.fork()

if p==0:
	print('child')
	os.close(r)
	os.dup2(w,1)
	os.close(w)
	os.execlp(sys.argv[1],sys.argv[1])
	print('erreur')
else:
	print('parent')
	os.close(w)
	os.dup2(r,0)
	os.close(r)
	os.execlp(sys.argv[2],sys.argv[2])
	print('errr')	

