from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['PFSD'] #database name
info=db.PFSD
student1={"reg No":"2100032410","Name":"SARATH"}  #dictionary
student2=[
    {"reg No":"2100032302","Name":"KISHORE"},#dictionaries in a list
    {"reg No":"2100030261","Name":"KOUSHIK"}
]
studentdata=db.student
studentdata.insert_one(student1)#inserting one data
#inserting many data
studentdata.insert_many(student2)
#fetching one data
print(studentdata.find_one())
#fetching specific data
tofind1={"reg No":"2100030261"}
for x in tofind1:
    print(studentdata.find_one(tofind1))
#delete one data
todelete1={"reg No":"2100030261"}
studentdata.delete_one(todelete1)
#print(todelete1.deleted_count,"documents deleted")
#delete many data
todelete2={"reg No":"2100032410"}
studentdata.delete_many(todelete2)
print(len(todelete2),"documents deleted")