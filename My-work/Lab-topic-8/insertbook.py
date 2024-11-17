import sqlite3

con = sqlite3.connect("pfda.db")
cur = con.cursor()

# check there is nothing in the database
result = cur.execute("select * from book")
print (result.fetchone())

# insert a book
sql = """
INSERT INTO book VALUES
('Harry Pothead', 'Just Kidding Really', "112344"),
('Harry Potter does something profound', 'JK Rowling', "123444")
"""
# DANGER DANGER this can lead to SQL injection
cur.execute(sql)
con.commit() # remember to commit your updates

# something is missing here.... what do you think it is?
result = cur.execute("select * from book")
print (result.fetchone())
con.close()