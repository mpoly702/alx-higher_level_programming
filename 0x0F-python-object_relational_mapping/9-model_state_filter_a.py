#!/usr/bin/python3
"""Prints State objects containing the letter "a" from the database"""


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

        """Querying for State objects containing the letter a"""
        res = session.query(State).order_by(State.id.asc()).filter(
            State.name.like('%a%')
        )

        """Display results"""
        for st in res:
            print('{}: {}'.format(st.id, st.name))
        