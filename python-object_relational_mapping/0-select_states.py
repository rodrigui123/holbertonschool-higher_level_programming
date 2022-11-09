#!/usr/bin/python3
"""task 0"""


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states;")
    result = mycursor.fetchall()
    for record in result:
        print(record)
    mycursor.close()
    db.close()
