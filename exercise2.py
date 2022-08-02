
class circle:
    radius="NULL"
    def cperi(self,radius):
        cirperi=self.radius*2*3.14
        print("Perimeter of Circle :",cirperi)
class rectangle:
    length="NULL"
    breadth="NULL"
    def rperi(self,l,b):
       recperi=2*(self.length+self.breadth)
       print("Perimeter of Rectangle :",recperi)
class triangle:
    side1="NULL"
    side2="NULL"
    side3="NULL"
    def tperi(self,s1,s2,s3):
        tperi=self.side1+self.side2+self.side3
        print("Perimeter of Triangle :",tperi)
class perimeter(circle,rectangle,triangle):
    def init(self,r,l,b,s1,s2,s3):
        self.radius=r
        self.length=l
        self.breadth=b
        self.side1=s1
        self.side2=s2
        self.side3=s3
p=perimeter(float(input("Enter the Radius of CIRCLE :")),float(input("Enter Length of rectangle :")),float(input("Enter Breadth")),float(input("Enter the Sides of triangle :")),float(input()),float(input()))
p.cperi(p.radius)
p.rperi(p.length,p.breadth)
p.tperi(p.side1,p.side2,p.side3)