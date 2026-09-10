from database.habits_db import save_habit, get_habits
from database.habit_logs_db import save_habit_log
from database.habit_logs_db import get_habit_by_id

def validate_habit(name, data_type, unit=None):

    if not name or not name.strip():
        raise ValueError("Habit name cannot be empty.")

    if data_type not in ("bool", "numeric"):
        raise ValueError("Invalid data type.")

    if data_type == "bool" and unit is not None:
        raise ValueError("Boolean habits cannot have a unit.")

    if data_type == "numeric" and unit is None:
        raise ValueError("Numeric habits require a unit.")


def add_habit(name, data_type, unit=None):
    validate_habit(name, data_type, unit)
    save_habit(name, data_type, unit)


def show_habits():
    return get_habits()

def get_habit(habit_id):
    ...


def log_habit(habit_id, date, value):

    habit = get_habit_by_id(habit_id)

    if habit is None:
        raise ValueError("Habit not found.")

    data_type = habit[2]

    if data_type == "bool":
        if not isinstance(value, bool):
            raise ValueError("Value must be True or False.")

    elif data_type == "numeric":
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be numeric.")

    save_habit_log(habit_id, date, value)


def get_habit_info(habit_id):
    return get_habit_by_id(habit_id)


def delete_habit():
    pass