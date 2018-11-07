import os


print("hello",end=',')
#print("ok",end=',' ,flush=True)
print("non",end='')
os.write(1,b"oui")
print("ok")