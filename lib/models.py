from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    membership_type = Column(String)
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    trainer = relationship('Trainer', back_populates='members')

    def __repr__(self):
        return f"<Member {self.name}, Age: {self.age}, Trainer: {self.trainer.name if self.trainer else 'None'}>"

class Trainer(Base):
    __tablename__ = 'trainers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    expertise = Column(String)
    members = relationship('Member', back_populates='trainer', cascade="all, delete")

    def __repr__(self):
        return f"<Trainer {self.name}, Expertise: {self.expertise}>"
