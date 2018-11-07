import os,sys
if not os.path.exists('pipe'):
 os.mkfifo('pipe',os.O_CREAT)

p=os.fork()

if p==0:
	w=os.open('pipe',1)
	os.write(w,'hello'.encode())
	os.close(w)
else:

	r=os.open('pipe',0)
	line=os.read(r,1024)
	print(line.decode())
	os.close(r)

print('fin')
	