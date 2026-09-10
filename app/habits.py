from database.habits_db import save_habit, get_habits


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

def log_habit():
    pass


def delete_habit():
    pass