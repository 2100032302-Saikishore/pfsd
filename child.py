from classes import Addtion
class A(Addtion):
    d=0;
    def __init__(self,a,b,d):
        super(A, self).__init__(a,b)
        self.d=d
    def dis(self):
        c=self.d+Addtion.answer
        print("c",c)
o=A(1000,2000,1000)
o.dis()
