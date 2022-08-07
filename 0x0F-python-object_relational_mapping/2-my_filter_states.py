#!/usr/bin/python3

"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

from sys import argv
import MySQLdb
if __name__ == '__main__':

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC" .format(argv[4]))

    rows = cur.fetchall()
    for r in rows:
        print("{}".format(r))

    cur.close()
    db.close()
