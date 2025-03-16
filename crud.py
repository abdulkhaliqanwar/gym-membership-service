from lib.database import session
from lib.models import Member, Trainer

# CRUD for Members
class MemberCRUD:
    @staticmethod
    def create(name, age, address, phone, email, membership_type, trainer_id):
        member = Member(name=name, age=age, address=address, phone=phone, email=email, 
                        membership_type=membership_type, trainer_id=trainer_id)
        session.add(member)
        session.commit()
        return member

    @staticmethod
    def get_all():
        return session.query(Member).all()

    @staticmethod
    def find_by_id(member_id):
        return session.query(Member).filter_by(id=member_id).first()

    @staticmethod
    def update(member, name=None, age=None, address=None, phone=None, email=None, membership_type=None):
        if name: member.name = name
        if age: member.age = age
        if address: member.address = address
        if phone: member.phone = phone
        if email: member.email = email
        if membership_type: member.membership_type = membership_type
        session.commit()
        return member

    @staticmethod
    def delete(member):
        session.delete(member)
        session.commit()

# CRUD for Trainers
class TrainerCRUD:
    @staticmethod
    def create(name, age, address, phone, email, expertise):
        trainer = Trainer(name=name, age=age, address=address, phone=phone, email=email, expertise=expertise)
        session.add(trainer)
        session.commit()
        return trainer

    @staticmethod
    def get_all():
        return session.query(Trainer).all()

    @staticmethod
    def find_by_id(trainer_id):
        return session.query(Trainer).filter_by(id=trainer_id).first()

    @staticmethod
    def update(trainer, name=None, age=None, address=None, phone=None, email=None, expertise=None):
        if name: trainer.name = name
        if age: trainer.age = age
        if address: trainer.address = address
        if phone: trainer.phone = phone
        if email: trainer.email = email
        if expertise: trainer.expertise = expertise
        session.commit()
        return trainer

    @staticmethod
    def delete(trainer):
        session.delete(trainer)
        session.commit()
