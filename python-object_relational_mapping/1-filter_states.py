#!/usr/bin/python3


"""
1. Filter status
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
            "SELECT states.id, states.name FROM states WHERE LEFT(states.name, 1) = 'N' ORDER BY states.id ASC;"
                    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
