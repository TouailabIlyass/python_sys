import socket,threading

def send(a):
		m=''
		while m!='fin':
			m=input("client > ")
			a.send(m.encode())
			
		print('fin')	

def main():
	
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(('127.0.0.1',9098))
	
	print("client pret")
	
	t=threading.Thread(target=send,args=(sock,))
	t.start()
	m=''
	while m!='fin':
		m=sock.recv(1204)
		m=m.decode
		print(m)
		if m=='fin':
			sock.send('fin'.encode())
			break
		
	print("fin client")
	
	sock.close()
if __name__ == '__main__':
		main()	