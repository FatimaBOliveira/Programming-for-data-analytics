import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 #user="datarep", # this is the user name on my mac
 #passwd="password" # for my mac
 database="wsaa"
)

mycursor = mydb.cursor()

sql="delete from student where id = %s"
values = (1,)
mycursor.execute(sql, values)

mydb.commit()
print("delete done")

mycursor.close()
mydb.close()