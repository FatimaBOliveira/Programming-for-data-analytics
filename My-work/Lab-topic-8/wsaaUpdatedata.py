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

sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)
mycursor.execute(sql, values)

mydb.commit()
print("update done")

mycursor.close()
mydb.close()