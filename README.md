# Gym Membership CLI Application

## 📌 Overview
The **Gym Membership CLI Application** is a Python-based command-line interface (CLI) that allows users to manage a gym's trainers and members. This project leverages **SQLAlchemy** for database interactions and follows Object-Relational Mapping (ORM) principles. Users can add, view, update, and delete trainers and members while ensuring data integrity and relationships.

## 🚀 Features
- **Trainers Management:** Add, view, and remove trainers.
- **Members Management:** Add members, assign them to trainers, and manage memberships.
- **View Related Data:** See which members belong to which trainers.
- **Database Persistence:** Uses SQLite to store data.
- **Data Seeding:** Generates fake trainers and members using the `Faker` library.
- **Interactive CLI:** Provides user-friendly menus and input validation.

## 🏗️ Technologies Used
- **Python 3**
- **SQLAlchemy** (ORM for database interactions)
- **Alembic** (Database migrations)
- **Faker** (For generating dummy data)

## 📂 Project Structure
```
project-folder/
│── cli.py
│── crud.py
│── models.py
│── seed.py
│── lib/
│   ├── database.py
│   ├── __init__.py
│── migrations/
│── README.md

## 🔧 Installation & Setup
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd phase-3-project
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```sh
   alembic upgrade head
   ```

5. **Seed the database with fake data**:
   ```sh
   python seed.py
   ```

6. **Run the CLI**:
   ```sh
   python cli.py
   ```

## 🖥️ Usage Guide
Once inside the CLI, follow the menu prompts to:
- Add/View/Delete Trainers
- Add/View/Delete Members
- Assign Members to Trainers
- Exit the application



## 📜 License
This project is for educational purposes. Feel free to modify and improve it!

## 🙌 Acknowledgments
Thanks to Moringa School for the guidance and support in learning Python, ORM, and CLI development!



