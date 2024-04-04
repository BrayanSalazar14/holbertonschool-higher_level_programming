#!/usr/bin/python3
"""
script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
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
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    [print(row) for row in query_rows if row[1] == name_search]

    cur.close()
    db.close()
