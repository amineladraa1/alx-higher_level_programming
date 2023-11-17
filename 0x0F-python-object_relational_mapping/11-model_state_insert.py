#!/usr/bin/python3
"""Start link in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        transaction = connection.begin()
        query = insert(State).values(name="Louisiana")
        connection.execute(query)
        q = select(State).where(State.name == "Louisiana")
        st = connection.execute(q).fetchone()
        if st:
            print(st.id)
        transaction.commit()

    engine.dispose()
