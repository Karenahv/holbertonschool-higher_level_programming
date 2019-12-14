#!/usr/bin/python3
"""print first object"""

from model_state import Base, State
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
    count = 0
    for row in session.query(State).filter(
            State.name == sys.argv[4]).order_by(State.id):
            print(row.id)
            count = count + 1
    if count == 0:
        print("Not found")
    session.close()
