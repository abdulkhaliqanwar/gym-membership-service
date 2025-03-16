from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from lib.database import Base, session  # Import from database.py

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

    # CRUD methods
    @classmethod
    def create(cls, name, age, address, phone, email, membership_type, trainer_id):
        member = cls(name=name, age=age, address=address, phone=phone, email=email, 
                     membership_type=membership_type, trainer_id=trainer_id)
        session.add(member)
        session.commit()
        return member

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, member_id):
        return session.query(cls).filter_by(id=member_id).first()

    def update_info(self, name=None, age=None, address=None, phone=None, email=None, membership_type=None):
        if name: self.name = name
        if age: self.age = age
        if address: self.address = address
        if phone: self.phone = phone
        if email: self.email = email
        if membership_type: self.membership_type = membership_type
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

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

    @classmethod
    def create(cls, name, age, address, phone, email, expertise):
        trainer = cls(name=name, age=age, address=address, phone=phone, email=email, expertise=expertise)
        session.add(trainer)
        session.commit()
        return trainer

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, trainer_id):
        return session.query(cls).filter_by(id=trainer_id).first()

    def update_info(self, name=None, age=None, address=None, phone=None, email=None, expertise=None):
        if name: self.name = name
        if age: self.age = age
        if address: self.address = address
        if phone: self.phone = phone
        if email: self.email = email
        if expertise: self.expertise = expertise
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()
