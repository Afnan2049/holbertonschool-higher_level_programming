#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
This script uses SQLAlchemy to query the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine to connect to the MySQL server
    # Format: mysql+mysqldb://user:password@host:port/database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Configure a session factory
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
