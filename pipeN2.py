import os,sys

if not os.path.exists('pipe'):
		os.mkfifo('pipe')

p=os.fork()

if p==0:
	w=os.open('pipe',1)
	os.dup2(w,1)
	os.close(w)
	os.execlp(sys.argv[1],sys.argv[1])
	print("erreur")
else:
	r=os.open('pipe',0)
	os.dup2(r,0)
	os.close(r)
	os.execlp(sys.argv[2],sys.argv[2],sys.argv[3])
	print('errrrrrr')
