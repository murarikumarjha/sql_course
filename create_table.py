import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if NOT EXISTS test2.test1_table(c1 INT , c2 VARCHAR(50), c3 FLOAT , c4  INT , c5 VARCHAR(50))")
mydb.close()