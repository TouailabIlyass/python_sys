import socket,threading

def send(a):
		m=''
		while m!='fin':
			m=input('server >')
			a.send(m.encode())
			
		print('fin')

def main():
	
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('127.0.0.1',9098))
	sock.listen(4)
	print("server pret")
	cnx_cl,s=sock.accept()
	t=threading.Thread(target=send,args=(cnx_cl,))
	t.start()
	m=''
	while m!='fin':
		m=cnx_cl.recv(1204)
		m=m.decode()
		print(m)
		if m=='fin':
			cnx_cl.send('fin'.encode())
			break
	print("fin serv")
	cnx_cl.close()
	sock.close()

if __name__ == '__main__':
		main()	