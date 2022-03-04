from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:postgres@postgres/mycompany")
Session = sessionmaker(bind=engine)


def db_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
