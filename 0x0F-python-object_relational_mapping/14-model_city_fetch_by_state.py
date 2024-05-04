#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

        """Query all City objects and print them"""
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            stateName = session.query(State).filter_by(
                id=city.state_id).first().name
            print("{}: ({}) {}".format(stateName, city.id, city.name))

        session.close()
        