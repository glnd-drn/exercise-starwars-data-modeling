import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoritesPerson(Base):
    __tablename__='favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))




class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable=True) #nullable=true funciona para dejar vacia la info.
    age = Column(Integer, nullable=False) #integer para numeros enteros, como la edad.
    favorites_user = relationship(FavoritesPerson, backref='person')
    

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False) #integer para numeros enteros, como la edad.
    favorites_person = relationship(FavoritesPerson, backref='user')
    
class FavoritesPerson(Base):
    __tablename__='favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))




class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
