import os

r,w=os.pipe()

p=os.fork()


if p==0:
	os.close(r)
	print("child writing")
	os.write(w,b"any text...")
	os.close(w)
	print("child closing")

else:
	os.close(w)
	print('parent reading')
	str=os.read(r,1024)
	print(str)
	print("ok fin")



print("fin programme")
