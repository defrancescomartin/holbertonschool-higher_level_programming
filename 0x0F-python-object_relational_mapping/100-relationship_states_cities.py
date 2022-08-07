#!/usr/bin/python3
"""script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    """generate database schema"""
    Base.metadata.create_all(engine)
    """create a new session"""
    session = Session()

    st = State(name='California')
    st.cities = [City(name='San Francisco')]
    session.add(st)
    session.commit()
