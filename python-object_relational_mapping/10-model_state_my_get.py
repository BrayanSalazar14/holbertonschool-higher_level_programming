#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    st_name_search = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    flag = False
    for instance in session.query(State).filter_by(name=st_name_search):
        print(f"{instance.id}")
        flag = True

    if flag is False:
        print("Not found")
