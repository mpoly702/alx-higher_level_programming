#!/usr/bin/python3
"""Creates the State 'California' with the City San 'Francisco'"""


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

        """State 'California' and City 'San Francisco'"""
        california = State(name="California")
        san_francisco = City(name="San Francisco", state=california)

        """Add and commit changes"""
        session.add(california, san_francisco)
        session.commit()
        session.close()
        