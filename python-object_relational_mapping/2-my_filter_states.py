#!/usr/bin/python3
"""
takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa where name matches the argument.
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
                SELECT * FROM states WHERE name = "{:s}" ORDER BY id ASC
                """.format(name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()
    