#!/usr/bin/python3
"""
Takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()

    cur.execute("""
                SELECT * FROM states WHERE name = %s ORDER BY id ASC
                """, (name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()