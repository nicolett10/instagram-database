import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column (Integer, primary_key = True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column (String(30), nullable=False) 
    lastname = Column (String(30), nullable=False) 
    email = Column (String(50), nullable=False) 
    password = Column (String(10), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column (Integer, primary_key = True)

class Post(Base):
    __tablename__ = 'posts'
    id = Column (Integer, primary_key = True)   

class Media (Base):
    __tablename__ = 'medias'
    id = Column (Integer, primary_key = True)

class Follower(Base):
    __tablename__ = 'followers'
    id = Column (Integer, primary_key = True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')