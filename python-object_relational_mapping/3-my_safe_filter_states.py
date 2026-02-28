#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from SQL injection.
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

    # Use a parameterized query to prevent SQL Injection.
    # The %s is a placeholder, not a string format operator.
    # The second argument to execute is a tuple containing the input.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    # Fetch and print results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
