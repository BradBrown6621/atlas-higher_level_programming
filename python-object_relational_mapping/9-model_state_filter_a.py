#!/usr/bin/python3


"""
Fetches 'State' objects that have a letter 'A' or 'a' in their name
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
            State.name.contains('a')
            ).order_by(State.id).all()
    if states is None:
        print("Nothing")
    else:
        for state in states:
            print("{}: {}".format(state.id, state.name))

    session.close()
