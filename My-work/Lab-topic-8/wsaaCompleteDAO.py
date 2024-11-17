import mysql.connector

class StudentDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""


    def __init__(self):
    #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="wsaa"

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
    # your code here
        cursor = self.getCursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        studentlist = []
        #for row in result:
        #    studentlist.append(self.convertToDict(row))
        #self.closeAll()
        for x in result:
            print(x)
        return studentlist

    def findByID(self, id):
    #your code here
        cursor = self.getCursor()
        sql="select * from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self

    def update(self, values):
    #your code here
        cursor = self.getCursor()
        sql="update student set name= %s, age=%s  where id = %s"
        values = (values)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return self

    def delete(self, id):
    # your code here
        cursor = self.getCursor()
        sql="delete from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll
        #print("delete done")
        return True

studentDAO = StudentDAO()