import os
from dotenv import load_dotenv
from database.connection import get_connection

load_dotenv()
DB_PASSWORD = os.getenv("POSTGRESQL_PASS")


def validate_habit(name, data_type, unit=None):

    if not name or not name.strip():
        raise ValueError("Habit name cannot be empty.")

    if data_type not in ("bool", "numeric"):
        raise ValueError("Invalid data type.")

    if data_type == "bool" and unit is not None:
        raise ValueError("Boolean habits cannot have a unit.")

    if data_type == "numeric" and unit is None:
        raise ValueError("Numeric habits require a unit.")

def save_habit(name, data_type, unit=None):
    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO habits (name, data_type, unit)
        VALUES (%s, %s, %s)
    """, (name, data_type, unit))

    conn.commit()

    cur.close()
    conn.close()

def add_habit(name, data_type, unit=None):
    validate_habit(name, data_type, unit)
    save_habit(name, data_type, unit)

def get_habits():
    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT * FROM habits;")

    habits = cur.fetchall()

    cur.close()
    conn.close()

    return habits

def log_habit():
    pass

def delete_habit():
    pass