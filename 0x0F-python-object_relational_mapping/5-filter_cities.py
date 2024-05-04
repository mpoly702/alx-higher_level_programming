#!/usr/bin/python3
"""Lists all cities of a specific state from the database hbtn_0e_4_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    print(', '.join(map(lambda x: x[0], rows)))

    cur.close()
    conn.close()
    