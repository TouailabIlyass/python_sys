import os

print("hello",end=" ")

os.write(1,'ok\n'.encode())

print('world')