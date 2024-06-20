#!/usr/bin/python3


"""
My first ORM project YAAAAY!!
This wasn't super hard, but I still have a few to go.
"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute(
            "SELECT states.id, states.name FROM states ORDER BY states.id ASC;"
                    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
