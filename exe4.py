import csv,operator
def add():
  with open("Employees.csv", mode='w') as myfile:
        n=int(input("ennter n"))
        mywriter= csv.writer(myfile, delimiter=",")
        for row in range(1,n+1):
            empid= (input("enter employee number: "))
            name= input("enter employee name: ")
            salary= (input("enter employee salary: "))
            DPt= input("enter employee address: ")
            no_of_days= (input("enter no oy years: "))
            designaton=input("enter deg : ")
            DOB=input("enter dob : ")
            Experience=input("enter experience")
            mywriter.writerow([empid, name, salary, DPt,no_of_days,designaton,DOB,Experience])
def sort_by_salary():
    data = csv.reader(open('Employees.csv'), delimiter=',')
    data = sorted(data, key=operator.itemgetter(2))
    with open('Employees.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))

def sort_by_no_of_days():
    data = csv.reader(open('Employees.csv'), delimiter=',')
    data = sorted(data, key=operator.itemgetter(4))

    with open('Employees.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
def show():
    with open('Employees.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
           print(', '.join(row))

o=1
while(o!=0):
    k=input("1.add 2.sort_by_salary 3. sort_by_no_of_days 4.show 5.Exit :")
    if(k=='1'):
        add()
    if(k=='2'):
        sort_by_salary()
    if(k=='3'):
        sort_by_no_of_days()
    if(k=='4'):
        show()
    if(k=='5'):
        o=0
