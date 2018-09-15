from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Dogs(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            }


class DogsItem(Base):
    __tablename__ = 'dogs_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    temperament = Column(String(250))
    group = Column(String(250))
    height = Column(String(50))
    weight = Column(String(50))
    description = Column(String(250))
    dogs_id = Column(Integer, ForeignKey('dogs.id'))
    dogs = relationship(Dogs)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'temperament': self.temperament,
            'group': self.group,
            'height': self.height,
            'weight': self.weight,
            'description': self.description,
            }

engine = create_engine('sqlite:///dogscatalog.db')


Base.metadata.create_all(engine)
