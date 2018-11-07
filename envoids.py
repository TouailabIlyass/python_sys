import os
p=os.fork()

if p==0:
	print('fils started')
	os.execlp('xeyes','xeyes')
	print('erreur')

else:
	print("tapez <0> pour quitter")
	print("pid du fils ",p)
	i=1
	while i!=0:
		i=int(input('signal>'))
		if i==0:
			os.kill(p,15)
			break
		os.kill(p,i)

