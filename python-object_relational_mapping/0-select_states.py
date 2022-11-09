#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost',
    port=3306
    username=sys.argv[1],
    password=sys.argv[2],
    name=sys.argv[3]
)
mycursor = db.cursor()
mycursor.execute("SELECT * FROM states;")
result = mycursor.fetchall()
for record in result:
    print(record)
db.close()