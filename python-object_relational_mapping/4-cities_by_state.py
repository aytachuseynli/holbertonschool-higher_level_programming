#!/usr/bin/python3
"""
 lists all cities
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_cities.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    [print(row) for row in cursor.fetchall()]

    db.close()