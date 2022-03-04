#!/usr/bin/python3
"""write a script that takes in arguments
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

if __name__ == '__main__':
    
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
