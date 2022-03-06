#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MYSQLdb
import sys

if __name__ == "__main__":
    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = connection.cursor()

    cursor.execute(("SELECT cities.id, cities.name, states.name FROM cities "
                    "INNER JOIN states ON cities.state_id = states.id "
                    "ORDER BY cities.id"))

    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
