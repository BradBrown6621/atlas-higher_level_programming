#!/usr/bin/python3


"""
5. All cities by state
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
            "SELECT cities.name\
                    FROM cities\
                    WHERE cities.state_id = (\
                        SELECT id FROM states\
                        WHERE states.name = %s\
                        LIMIT 1)\
                    ORDER BY cities.id ASC;", (sys.argv[4], )
                    )
    print(cur.fetchone()[0], end="")
    rows = cur.fetchall()
    for row in rows:
        print(', ', end="")
        print(row[0], end="")
    print('')

    cur.close()
    db.close()
