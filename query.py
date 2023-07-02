import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from test2.test1_table")
for i in mycursor.fetchall():
    print(i)

mydb.close()