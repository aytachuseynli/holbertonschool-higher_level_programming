#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N)
"""
   
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db,
        charset="utf8"
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    