#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
This script takes 3 arguments: mysql username, mysql password
and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Database connection parameters from arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object to execute queries
    cur = db.cursor()

    # Execute SQL query to fetch all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results from the executed query
    query_rows = cur.fetchall()

    # Print each row in the specified format
    for row in query_rows:
        print(row)

    # Close cursor and database connection to free resources
    cur.close()
    db.close()
