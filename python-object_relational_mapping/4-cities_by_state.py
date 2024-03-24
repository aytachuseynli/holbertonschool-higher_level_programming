#!/usr/bin/python3
"""
Lists all cities
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
    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id=states.id
                ORDER BY cities.id ASC
                """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()