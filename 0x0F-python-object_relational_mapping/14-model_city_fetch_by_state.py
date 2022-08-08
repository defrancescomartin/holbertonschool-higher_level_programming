#!/usr/bin/python3

"""script 14-model_city_fetch_by_state.py that prints all City objects from
the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PASS, MY_DB))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for i, ii in session.query(City, State)\
            .filter(State.id == City.state_id).all():
        print('{}: ({:d}) {}'.format(ii.name, i.id, i.name))

    session.close()
