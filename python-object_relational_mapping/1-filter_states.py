#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N)
"""
import MySQLdb
import sqlalchemy
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor =  db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(row) for row in cursor.fetchall()]
    db.close