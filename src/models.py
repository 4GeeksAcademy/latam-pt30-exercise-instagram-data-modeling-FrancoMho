import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'

    # PK
    id = Column(Integer, primary_key=True)
    # INFO
    name = Column(String(250), nullable=False)
    #CHILDREN |MANY TO ONE | USER
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('user', back_populates='followers' )

class User(Base):
    __tablename__ = 'user'

    # PK
    id = Column(Integer, primary_key=True)
    # INFO
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    # FK | FOLLOWER | MANY TO ONE
    person = relationship('follower', back_populates='user' )
    #CHILDREN | COMMENT | ONE TO MANY
    comment = relationship('comment', back_populates='user' )
    #CHILDREN | POST | ONE TO MANY
    comment = relationship('post', back_populates='user' )


class Comment(Base):
    __tablename__ = 'comment'

    # PK
    id = Column(Integer, primary_key=True)
    # INFO
    comment_text = Column(String(250))
    # FK | USER | ONE TO MANY
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('user', back_populates='comments' )
    # FK | POST | ONE TO MANY
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('post', back_populates='comments' )

class Post(Base):
    __tablename__ = 'post'

    # PK
    id = Column(Integer, primary_key=True)
    # INFO
    # FK | USER | ONE TO MANY
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('user', back_populates='posts' )
    #CHILDREN | COMMENT | ONE TO MANY
    comment = relationship('comment', back_populates='post' )
    #CHILDREN | MEDIA | ONE TO MANY
    comment = relationship('media', back_populates='post' )

class Media(Base):
    __tablename__ = 'media'

    # PK
    id = Column(Integer, primary_key=True)
    # INFO
    type = Column(String(250))
    url = Column(String(250))
    # FK | POST | ONE TO MANY
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('post', back_populates='medias' )
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
