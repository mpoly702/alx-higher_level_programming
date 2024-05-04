#!/usr/bin/python3
"""Prints the first State object from the database"""


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

        """Querying for the first State object"""
        top = session.query(State).first()

        """Checking if the table is empty"""
        if top is None:
            print("Nothing")
        else:
            print('{}: {}'.format(top.id, top.name))
        