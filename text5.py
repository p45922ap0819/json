# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('test1.db')
c = conn.cursor()
print("Opened database successfully")
cursor = c.execute("SELECT id, name,country, phone  from SCHOOL")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("COUNTRY = ", row[2])
   print("PHONE = ", row[3], "\n")
print("Operation done successfully")
conn.close()