import MySQLdb
import sys

db = MySQLdb.connect(
    username=sys.argv[0]
    password=sys.argv[1]
    name=sys.argv[2]
)
mycursor = db.cursor()