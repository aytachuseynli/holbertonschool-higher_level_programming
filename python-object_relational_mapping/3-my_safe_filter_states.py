#!/usr/bin/python3
"""
 takes in arguments and displays all values in the states table 
 of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    # Connect to MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db,
        charset="utf8"
    )

    # Create cursor
    cur = conn.cursor()

    # Execute safe parameterized query
    cur.execute(
        """
        SELECT * FROM states WHERE name = %s ORDER BY id ASC
        """,
        (name,)
    )

    # Fetch and print results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()