#!/usr/bin/python3
"""Start link class in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    dStates = session.query(State).filter(State.name.like(f'%a%')).all()
    if dStates:
        for st in dStates:
            session.delete(st)
        session.commit()

    session.close()
