import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa"
)

mycursor = mydb.cursor()

sql="select * from student where id = %s"
values = (1,)
mycursor.execute(sql, values)

result = mycursor.fetchall()
for x in result:
    print(x)

mycursor.close()
mydb.close()