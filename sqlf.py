import sqlite3

with sqlite3.connect("new.db") as connection:
   c = connection.cursor()

   for row in c.execute("Select firstname, lastname from employees"):
      print row

