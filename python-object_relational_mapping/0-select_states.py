#!/usr/bin/python3
"""
This module provides a script that lists all states from the database
hbtn_0e_0_usa. It connects to a MySQL server running on localhost at
port 3306 using arguments passed through the command line.
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the database and prints all states in ascending order by id.
    """
    # Arguments: sys.argv[1] = user, sys.argv[2] = passwd, sys.argv[3] = db
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Clean up
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()#!/usr/bin/python3
"""
This module provides a script that lists all states from the database
hbtn_0e_0_usa. It connects to a MySQL server running on localhost at
port 3306 using arguments passed through the command line.
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the database and prints all states in ascending order by id.
    """
    # Arguments: sys.argv[1] = user, sys.argv[2] = passwd, sys.argv[3] = db
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Clean up
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
