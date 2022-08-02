class Addtion:
    first =  0
    second=0
    answer=0

    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("first number",self.first)
        print("second number",self.second)
        print("answer",self.answer)
    def calculate(self):
        self.answer=self.first+self.second
