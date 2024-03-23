#!/usr/bin/python3
"""
takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)

    db.close()
