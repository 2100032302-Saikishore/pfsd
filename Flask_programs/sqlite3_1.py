import sqlite3
conn=sqlite3.connect('pfsd2.db')
print("Opened database successfully")
#Creating a Table
# conn.execute('''CREATE TABLE sqliteexample(ID Number,name Text,sub1 varchar,sub2 varchar,sub3 varchar)''')
# print("Table created successfully")
#inserting data into table
conn.execute("Insert into sqliteexample values(2100032302,'kishore','DAA','AIDS','PFSD')")
print("Inserted Successfully")
cur=conn.cursor()
for row in cur.execute('SELECT * FROM sqliteexample'):
    print(row)
data1=[(2100032410,"Sarath",'DAA','AIDS','PFSD'),(2100030261,"Koushik",'DAA','AIDS','PFSD')]
#inserting multiple data into the table
cur.executemany('INSERT INTO sqliteexample VALUES(?,?,?,?,?);',data1)
print("Inserted Multiple data successfully")
for row in cur.execute('SELECT * FROM sqliteexample'):
    print(row)