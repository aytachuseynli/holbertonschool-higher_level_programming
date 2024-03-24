#!/usr/bin/python3
"""
takes in the name of a state as an argument and 
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
        charset="utf8")
    
    cur = conn.cursor()
    cur.execute("""
                    SELECT cities.name 
                    FROM cities 
                    INNER JOIN states 
                    ON cities.state_id = states.id 
                    WHERE states.name = %s 
                    ORDER BY cities.name
                """.format(name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()