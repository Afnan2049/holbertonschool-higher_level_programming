#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
The results show city ID, city name, and state name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = db.cursor()

    # SQL JOIN to get city info and state name in one go
    # cities.state_id is the foreign key linking to states.id
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch and print results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
