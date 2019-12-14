#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa with Name starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("select * FROM states WHERE BINARY name = %s ORDER BY id",
                (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
