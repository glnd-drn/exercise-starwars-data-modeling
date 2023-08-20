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
    rating = Column(Integer, nullable = True)

class FavoritesPlanets(Base):
    __tablename__='favoritesplanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class FavoritesVehicles(Base):
    __tablename__='favoritesvehicles'       
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('vehicle.id'))

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable=True) #nullable=true funciona para dejar vacia la info.
    birth_year = Column(String(250), nullable = False)
    skin_color = Column(String(250), nullable = False)
    height = Column(Integer, nullable = False)
    homeworld = Column(String(250), nullable = False)
    film = Column(Integer, nullable = False)
    mass = Column(Integer, nullable = False)
    created = Column(String(250), nullable = False)
    edited = Column(String(250), nullable = False)
    species = Column(Integer, nullable = False)
    starships = Column(Integer, nullable = False)
    url = Column(String(250), nullable = False)
    vehicles = Column(Integer, nullable = False)
    hair_color = Column(String(250), nullable = False)
    favorites_person = relationship(FavoritesPerson, backref='person', lazy =True)
    

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
    favorites_person = relationship(FavoritesPerson, backref='user', lazy=True)

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
