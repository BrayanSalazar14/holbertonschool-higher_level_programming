#!/usr/bin/python3
"""
script that takes in the name of a state as an
argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_sql_user = argv[1]
    my_sql_pass = argv[2]
    my_sql_db = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=my_sql_user, passwd=my_sql_pass, db=my_sql_db)

    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM cities " +
        "INNER JOIN states ON cities.state_id = states.id " +
        "WHERE states.name = '{}'".format(state_name))

    query_rows = cur.fetchall()

    for rows in range(len(query_rows)):
        print(*query_rows[rows], end="")
        if rows < len(query_rows) - 1:
            print(", ", end="")
    print()

    cur.close()
    db.close()
