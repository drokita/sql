import sqlite3

#conn = sqlite3.connect("new.db")
#cursor = conn.cursor()
#cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
#cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
#conn.commit()
#conn.close()

with sqlite3.connect("new.db") as connection:
   c = connection.cursor()
   c.execute("INSERT INTO population VALUES('Belleville', 'IL', 42000)")

