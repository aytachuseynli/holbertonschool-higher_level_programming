#!/usr/bin/python3
"""
Takes in the name of a state as an argument and 
lists all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    db = argv[3]
    name = argv[4]

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
                SELECT cities.name 
                FROM cities 
                INNER JOIN states 
                ON cities.state_id = states.id 
                WHERE states.name = "{}"
                ORDER BY cities.name
                """.format(name))

    query_rows = cur.fetchall()
    result = ""
    for i in range(len(query_rows)):
        result += query_rows[i][0] + ", "
    print(result[:-2])

    cur.close()
    conn.close()
