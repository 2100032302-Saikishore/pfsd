import datetime
import time
print(time.time())
print(time.asctime(time.localtime(time.time())))
date_obj=datetime.datetime.now()
print(date_obj)
import calendar
s=calendar.prcal(1)
print(datetime.time.min)
def h1():
    print("hello wrold")
h1()
a=int(input())
b=int (input())
print("operation +,-,*,/")
c=input()
def a1(a,b):
    return(a+b)
def a2(a,b):
    return(a-b)
def a3(a,b):
    return(a*b)
def a4(a,b):
    return(a/b)

if(c=="+"):
    print(a1(a,b))
if (c == "-"):
        print(a2(a, b))
if (c == "*"):
    print(a3(a, b))
if (c == "/"):
     print(a4(a, b))
