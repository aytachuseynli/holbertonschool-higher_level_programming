#!/usr/bin/python3
"""
All states via SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    """
    Model
    """

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(username, password, db),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()