#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usals"""


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

        """Make state object,add state object to session and commit to db"""
        nState = State(name="Louisiana")
        session.add(nState)
        session.commit()

        print(nState.id)

        session.close()
        