from triangle import tri
from rect import rect
class Area(tri,rect):
    def area(self):
        print(tri.a)
        print(rect.x*rect.x)
obj= Area()
obj.area()