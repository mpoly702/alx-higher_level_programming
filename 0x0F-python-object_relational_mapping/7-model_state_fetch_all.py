#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    user = sys.argv[1]
    passW = sys.argv[2]
    dataB = sys.argv[3]

    """Creating db URL"""
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            user, passW, dataB
        )

    """Create engine and connecting to db"""
    engine = create_engine(DATABASE_URL)

    """Create metadata and establish session"""
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    """Querying all State obj"""
    rows = session.query(State).all()

    for res in rows:
        print('{}: {}'.format(res.id, res.name))
    