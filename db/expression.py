import re


#excercie 1

print("excercie 1")

while True:

   password=input("enter votre mot de passe : ")
   if re.match(r"([0-9]){6,}",password) is not None:
   		break
   print("failed")
print("done")   	



#excercie 2

print("excercie 2")


tele=""

while re.match(r"^0[0-9]([-. ]?[0-9]{2}){4}$",tele) is None:
	tele= input("Saisissez un numero de telephone  valide :")

print("done")	
	