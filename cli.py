import sys
from lib.database import session
from lib.models import Member, Trainer

def main_menu():
    while True:
        print("\n🏋️ Gym Membership System 🏋️")
        print("1. View all Trainers")
        print("2. View all Members")
        print("3. Add a Trainer")
        print("4. Add a Member")
        print("5. Find a Trainer by ID")
        print("6. Find a Member by ID")
        print("7. Delete a Trainer")
        print("8. Delete a Member")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            trainers = Trainer.get_all()
            for trainer in trainers:
                print(trainer)
        
        elif choice == "2":
            members = Member.get_all()
            for member in members:
                print(member)
        
        elif choice == "3":
            name = input("Trainer Name: ")
            age = int(input("Age: "))
            address = input("Address: ")
            phone = input("Phone: ")
            email = input("Email: ")
            expertise = input("Expertise: ")
            Trainer.create(name, age, address, phone, email, expertise)
            print("Trainer added successfully!")
        
        elif choice == "4":
            name = input("Member Name: ")
            age = int(input("Age: "))
            address = input("Address: ")
            phone = input("Phone: ")
            email = input("Email: ")
            membership_type = input("Membership Type: ")
            trainer_id = int(input("Trainer ID: "))
            Member.create(name, age, address, phone, email, membership_type, trainer_id)
            print("Member added successfully!")

        elif choice == "5":
            trainer_id = int(input("Enter Trainer ID: "))
            trainer = Trainer.find_by_id(trainer_id)
            print(trainer if trainer else "Trainer not found.")

        elif choice == "6":
            member_id = int(input("Enter Member ID: "))
            member = Member.find_by_id(member_id)
            print(member if member else "Member not found.")

        elif choice == "7":
            trainer_id = int(input("Enter Trainer ID to delete: "))
            trainer = Trainer.find_by_id(trainer_id)
            if trainer:
                trainer.delete()
                print("Trainer deleted.")
            else:
                print("Trainer not found.")

        elif choice == "8":
            member_id = int(input("Enter Member ID to delete: "))
            member = Member.find_by_id(member_id)
            if member:
                member.delete()
                print("Member deleted.")
            else:
                print("Member not found.")

        elif choice == "9":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
