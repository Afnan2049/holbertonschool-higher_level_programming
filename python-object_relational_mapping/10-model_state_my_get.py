#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
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

    # Setup session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state name passed as the 4th argument (sys.argv[4])
    # .filter() is safe from SQL injection
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the state ID or "Not found"
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
