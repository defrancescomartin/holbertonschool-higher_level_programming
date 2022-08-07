#!/usr/bin/python3

"""script that prints the State object with the name passed as argument
 from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PASS, MY_DB))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    statelist = session.query(State).filter(State.name.like(argv[4])).first()
    if statelist is not None:
        print("{}".format(statelist.id))
    else:
        print("Not found")

    session.close()
