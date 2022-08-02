class Conformation :
    def display(self):
     print("Your ticket is booked")
class detiles(Conformation):
   a1,b1,c1 ='null',"null","null"
   def __init__(self,a,b,c):
        self.a1=a
        self.b1=b
        self.c1=c
   def display(self):
        print("name:",self.a1)
        print("date",self.b1)
        print("type:",self.c1)

class j(detiles):
    a,b="null","null"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("Soucre :",self.a)
        print("Destination",self.b)

n=input("enter your Source: ")
n1=input("enter your destination: ")
n2=input("enter your name: ")
n3=input("enter date: ")
n4=input("want a sleeper or Ac: ")
obj=j(n,n1)
obj1=detiles(n2,n3,n4)
obj2=Conformation()
obj2.display()
obj1.display()
obj.display()



