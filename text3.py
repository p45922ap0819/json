# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('test1.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE SCHOOL
  (ID INT PRIMARY KEY NOT NULL,
  NAME TEXT    NOT NULL,
  AGE  INT NOT NULL,
  COUNTRY   CHAR(50),
  PHONE    REAL);''')
print("Table created successfully")
conn.commit()
conn.close()
