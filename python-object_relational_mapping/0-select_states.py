#!/usr/bin/python3
"""lists all states """

import MySQLdb
import sys
import sqlalchemy

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
            print(row)
    cursor.close()
    db.close()
