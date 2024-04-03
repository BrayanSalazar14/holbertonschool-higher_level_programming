#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_sql_user = argv[1]
    my_sql_pass = argv[2]
    my_sql_db = argv[3]
    name_search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=my_sql_user, passwd=my_sql_pass, db=my_sql_db)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = \'{}\'".format(name_search))
    query_rows = cur.fetchall()
    print(*query_rows)

    cur.close()
    db.close()
