# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('test1.db')
c = conn.cursor()
print("Opened database successfully")
c.execute("INSERT INTO SCHOOL (ID,NAME,AGE,COUNTRY,PHONE) \
 VALUES (1, '王曉明', 15, 'China', 012345678 )");
c.execute("INSERT INTO SCHOOL (ID,NAME,AGE,COUNTRY,PHONE) \
 VALUES (2, 'Allen', 15, 'Fance', 23456789 )");
c.execute("INSERT INTO SCHOOL (ID,NAME,AGE,COUNTRY,PHONE) \
 VALUES (3, 'Teddy', 16, 'Japan', 34567891 )");
c.execute("INSERT INTO SCHOOL (ID,NAME,AGE,COUNTRY,PHONE) \
 VALUES (4, 'Mark', 15, 'USA ', 45678912 )");
conn.commit()
print("Records created successfully")
conn.close()


