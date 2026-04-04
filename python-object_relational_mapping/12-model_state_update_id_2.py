#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
The state with id = 2 is updated to 'New Mexico'.
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

    # Retrieve the state object where id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name attribute if the object exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        # Commit the transaction to save changes
        session.commit()

    # Close the session
    session.close()
