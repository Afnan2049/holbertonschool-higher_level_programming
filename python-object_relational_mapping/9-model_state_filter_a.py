#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
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

    # Query states containing the letter 'a' and sort by id
    # .like() is used for pattern matching
    states = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
