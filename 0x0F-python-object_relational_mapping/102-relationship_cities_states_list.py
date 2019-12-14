#!/usr/bin/python3
"""print first object"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()
    for s, c in query:
        print("{}: {} -> {}".format(c.id, c.name, s.name))
    session.close()
