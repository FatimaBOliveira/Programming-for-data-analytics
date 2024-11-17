import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

for row in cur.execute("select * from book"):
    print (f"row {row}")

''' # Same as
sql = "select * from book"
result = cur.execute(sql)
for row in result.fetchall():
    print(row)
'''