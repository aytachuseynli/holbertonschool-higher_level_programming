#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N)
"""
import MySQLdb
import sqlalchemy
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <database>")
        sys.exit(1)
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
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        
    finally:
        db.close()