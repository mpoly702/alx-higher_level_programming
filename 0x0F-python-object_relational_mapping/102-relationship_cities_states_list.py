#!/usr/bin/python3
"""Lists all City objects from the database"""


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

        """Query all cities with linked states"""
        st_ct = session.query(City).join(State).order_by(City.id.asc())
        for city in st_ct.all():
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
        