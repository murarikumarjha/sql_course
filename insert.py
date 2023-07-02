import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")

mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")
mycursor.execute("insert into test2.test1_table values(12, 'murari', 14.55 ,75, 'kumar')")

mydb.commit()
mydb.close()