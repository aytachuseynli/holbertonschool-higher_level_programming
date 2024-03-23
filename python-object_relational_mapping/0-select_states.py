#!/usr/bin/python3
"""lists all states """

import MySQLdb
import sys

def main():
    def list_states(username, password, db_name):
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=db_name,
                             port=3306)

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        db.close()


if __name__ == "__main__":
    main()