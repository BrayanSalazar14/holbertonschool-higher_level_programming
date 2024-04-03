#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    my_sql_user = argv[1]
    my_sql_pass = argv[2]
    my_sql_db = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=my_sql_user, passwd=my_sql_pass, db=my_sql_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
