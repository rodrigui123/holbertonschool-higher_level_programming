#!/usr/bin/python3
"""task 2"""


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
    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    result = mycursor.fetchall()