#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
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

    # Query all states containing 'a'
    # .delete(synchronize_session='fetch') ensures the session
    # stays in sync with the deleted records
    session.query(State).filter(State.name.like('%a%'))\
                        .delete(synchronize_session='fetch')

    # Commit the transaction to apply deletions
    session.commit()

    # Close the session
    session.close()
