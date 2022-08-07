#!/usr/bin/python3

"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    from sys import argv
    import MySQLdb

    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    db = MySQLdb.connect(host=MY_HOST, port=3306, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
               cities.state_id = states.id WHERE states.name = %s ORDER BY
               cities.id ASC""", (argv[4],))

    rows = cur.fetchall()
    records_list = []
    for r in rows:
        records_list.append(r[0])
    print(", ".join(records_list))

    cur.close()
    db.close()
