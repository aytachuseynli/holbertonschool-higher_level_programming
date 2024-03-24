#!/usr/bin/python3
"""
All states via SQLAlchemy
"""


import sys
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Model
    """

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db), 
        pool_pre_ping=True)
    Base.metadata.create_all(bind = engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()