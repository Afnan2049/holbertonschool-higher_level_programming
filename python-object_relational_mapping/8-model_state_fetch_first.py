#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
The state displayed is the one with the lowest id.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine to connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Configure a session factory and create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object ordered by id
    # .first() returns None if no result is found
    state = session.query(State).order_by(State.id).first()

    # Display results or "Nothing" if table is empty
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
