from math import sqrt

def T(x):
        return x*x

class MyClass:
    x=0
    y=2
    
    def __init__(self,x,y,name):
        self.x=x
        self.y=y
        self.name=name
    def distance(self,point):
        return sqrt(T(point.y-self.y)+T(point.x-self.x))
   
    def avance(self,x,y):
        self.x+=x
        self.y+=y
    def toString(self):
        return "{} : [{},{}]".format(self.name,self.x,self.y)


p1= MyClass(2,2,"x")
p2=MyClass(4,5,'y')
print("point 1")
print(p1.toString())     
print("point 2")
print(p2.toString())

print("distance entre 2 point : ",p1.distance(p2))