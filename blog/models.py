from .database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(String(512))
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")

    # def __init__(self, title, body):
    #     self.title = title
    #     self.body = body

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(254))
    password = Column(String(512))
    blogs = relationship("Blog", back_populates="creator")
