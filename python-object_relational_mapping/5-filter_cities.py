#!/usr/bin/python3
"""
Lists all cities of a state provided as an argument from the
database hbtn_0e_4_usa. Safe from SQL injection.
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

    # Query to JOIN cities and states and filter by state name
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute with the 4th argument as a parameter
    cur.execute(query, (sys.argv[4],))

    # Fetch all results
    query_rows = cur.fetchall()

    # Format the output: Extract name from each tuple and join with commas
    cities_list = [row[0] for row in query_rows]
    print(", ".join(cities_list))

    # Clean up
    cur.close()
    db.close()
