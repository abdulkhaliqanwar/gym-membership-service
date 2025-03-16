import random  # Import random
from faker import Faker
from lib.database import session
from lib.models import Member, Trainer

fake = Faker()

def seed_trainers(n=5):
    """Generate fake trainers."""
    trainers = []
    for _ in range(n):
        trainer = Trainer.create(
            name=fake.name(),
            age=fake.random_int(min=25, max=60),
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email(),
            expertise=fake.job()
        )
        trainers.append(trainer)
    return trainers

def seed_members(n=10):
    """Generate fake members and assign random trainers."""
    members = []
    trainers = Trainer.get_all()  # Get existing trainers
    if not trainers:
        trainers = seed_trainers()  # Ensure trainers exist

    for _ in range(n):
        trainer = random.choice(trainers) if trainers else None  # ✅ Fixed here
        member = Member.create(
            name=fake.name(),
            age=fake.random_int(min=18, max=65),
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email(),
            membership_type=fake.random_element(["Basic", "Premium", "VIP"]),
            trainer_id=trainer.id if trainer else None
        )
        members.append(member)
    return members

def seed_database():
    print("\n🌱 Seeding the database...")
    
    trainers = seed_trainers(5)
    print(f"✅ Seeded {len(trainers)} trainers.")
    
    members = seed_members(10)
    print(f"✅ Seeded {len(members)} members.")

if __name__ == "__main__":
    seed_database()
