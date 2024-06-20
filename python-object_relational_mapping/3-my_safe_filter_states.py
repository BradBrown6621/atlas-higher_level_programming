#!/usr/bin/python3


"""
3. Filter states by user input (no more pesky SQL injections)
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
            "SELECT states.id, states.name\
                    FROM states\
                    WHERE BINARY name = %s\
                    ORDER BY states.id ASC;", (sys.argv[4],)
                    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
