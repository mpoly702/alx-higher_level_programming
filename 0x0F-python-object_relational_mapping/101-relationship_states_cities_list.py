#!/usr/bin/python3
"""Lists all State and City objects"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

        """Query all states with cities"""
        st_ct = session.query(State).order_by(State.id.asc()).all()

        for state in st_ct:
            print('{}: {}'.format(state.id, state.name))
            for city in state.cities:
                print('\t{}: {}'.format(city.id, city.name))
        session.close()
        