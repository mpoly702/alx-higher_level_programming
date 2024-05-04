#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a' """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) == 4:
        user = sys.argv[1]
        passW = sys.argv[2]
        dataB = sys.argv[3]

        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            user, passW, dataB
        )

        engine = create_engine(DATABASE_URL)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        """Query and delete states with names containing 'a'"""
        _delete = session.query(State).filter(State.name.like("%a%")).all()
        for state in _delete:
            session.delete(state)

        session.commit()
        session.close()
        