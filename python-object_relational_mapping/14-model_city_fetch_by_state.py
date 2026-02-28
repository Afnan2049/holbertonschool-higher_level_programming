#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Displays results as <state name>: (<city id>) <city name>.
"""
import sys
from model_state import Base, State
from model_city import City
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

    # Query City and State objects using a join
    # Results are sorted by cities.id
    results = session.query(State, City).join(City).order_by(City.id).all()

    # Display results in the required format
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
