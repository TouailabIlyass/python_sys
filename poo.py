Etudiant={}

Enom=input('your name ')
Ep=input('your last name ')

Etudiant['nom']=Enom
Etudiant['pr']=Ep

print(Etudiant)

for i in Etudiant.keys():
	print('key : ',i,"  valeur : ",Etudiant[i])




	


'''
class Point:

	def __init__(self):
		self.x=10
		self.y=50
	def show(self):
		print(self.x,self.y,self.z)	


p= Point()
p.z=80
p.show()		
'''