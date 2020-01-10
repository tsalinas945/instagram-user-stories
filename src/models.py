import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    bio = Column(String(250))
    picture = Column(String(250))
    post_code = Column(String(250), nullable=False)
    comments_id = Column(Integer, ForeignKey('profile.id'))
    #person = relationship(Person)

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_code = Column(String(250), nullable=False)
    likes_id = Column(Integer, ForeignKey('comments.id'))
    #person = relationship(Person)

class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    bio = Column(String(250))
    picture = Column(String(250))
    post_code = Column(String(250), nullable=False)
    profile_id = Column(Integer, ForeignKey('user.id'))
    #person = relationship(Person)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    post_code = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('profile.id'))
    #person = relationship(Person)

class Pictures(Base):
    __tablename__ = 'pictures'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    bio = Column(String(250))
    picture = Column(String(250))
    post_code = Column(String(250), nullable=False)
    picture_id = Column(Integer, ForeignKey('profile.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')