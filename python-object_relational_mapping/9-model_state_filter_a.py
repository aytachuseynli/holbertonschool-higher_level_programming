#!/usr/bin/python3
"""
Write a script that lists all State objects that 
contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """
    Model
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    
    session = Session(engine)
    
    for state in session.query(State).filter(State.name.contains("a")):
        print("{}: {}".format(state.id, state.name))
    
    session.close()
