from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)

def get_session(): 
    engine = create_engine(
        "mysql+pymysql://root:@localhost:3306/orm_test",
        encoding= "utf-8",
        echo=True
    )
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    return session

if __name__ == '__main__':
    u = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    u.name = 10
    session = get_session()
    session.add(u)
    session.commit()
    session.close()