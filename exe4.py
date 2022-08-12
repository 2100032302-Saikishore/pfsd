import csv
# with open('Employee.csv','r') as csv_file:
#     csv_reader =csv.DictReader(csv_file)
#     with open("New_Employee.csv",'w') as newfile:
#         fieldnames = ['EMPID', 'Name',"DOB","Department","designaton","no of years",'Experience',"no of leaves","salary"]
#         csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t')
#         csv_writer.writeheader()
with open("employees.csv", mode='w') as myfile:
  mywriter= csv.writer(myfile, delimiter="/t")
  for row in mywriter:
    empid= int(input("enter employee number: "))
    name= input("enter employee name: ")
    salary= int(input("enter employee salary: "))
    DPt= input("enter employee address: ")
    no_of_years= int(input("enter no oy years: "))
    designaton=input("enter deg : ")
    DOB=input("enter dob : ")
    Experience=input("enter experience")
mywriter.writerow([empid, name, salary, DPt,no_of_years,designaton,DOB,Experience])

