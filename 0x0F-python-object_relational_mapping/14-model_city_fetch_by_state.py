#!/usr/bin/python3
"""model state
"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Sess = sessionmaker(bind=engine)
    sess = Sess()
    res = sess.query(City, State).\
        join(State, State.id == City.state_id).all()
    if res:
        for city, st in res:
            print(f"{st.name}: ({city.id}) {city.name}")
    sess.close()
