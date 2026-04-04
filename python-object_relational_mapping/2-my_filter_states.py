#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided by the user.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    # Arguments: 1:user, 2:passwd, 3:db, 4:search_name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = db.cursor()

    # Use format to create the SQL query with the user input
    # BINARY ensures case-sensitivity to match the input exactly
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY states.id ASC".format(sys.argv[4])

    # Execute the query
    cur.execute(query)

    # Fetch and print the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
