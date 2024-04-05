#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py that prints all City}
objects from the database hbtn_0e_14_usa
"""


from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # new_instance = session.query(State.name, City.id, City.name).\
    #     order_by(City.id).\
    #     join(City, City.state_id == State.id, isouter=True).all()

    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")