import math
class circle:
    a=0
    def __init__(self,a):
        self.a=a
    def area(self):
       print (self.a*self.a*math.pi)
    def perimeter(self):
        print(self.a*2*math.pi)
class rect:
    a=0
    b=0
    def area(self):
        print(self.a*self.b)
    def perimeter(self):
        print(2*(self.a+self.b))
class tri:
    a,b,c=0,0,0
    def area(self):
        print(0.5*self.b*self.c)
    def perimater(self):
        print(self.a+self.b+self.c)
n=int(input("enter no of inputs "))
if(n==1):
   obj= circle(int(input()))
   obj.area()
   obj.perimeter()
if(n==2):
    a=int(input())
    b=int(input())
    obj1=rect()
    obj1.a=a
    obj1.b=b
    obj1.area()
    obj1.perimeter()
if(n==3):
    a = int(input())
    b = int(input())
    c =  int(input())
    obj2=tri()
    obj2.a=a
    obj2.b=b
    obj2.c=c
    obj2.area()
    obj2.perimater()








