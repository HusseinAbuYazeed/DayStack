import datetime

from app.habits import (
    add_habit,
    show_habits,
    get_habit_info,
    log_habit
)


while True:

    today = datetime.date.today()
    date = today.strftime("%A, %Y-%m-%d")

    print("""
========================================
              DAYSTACK
========================================
""")

    print(f"Today is {date}")
    print("Habits you're tracking:")
    print("Today's To-Do:")

    choice = input("""
========================================
1. Log habits
2. Check today's to-do list
3. Make a to-do list for a day
4. Add a habit to track
5. Show All Habits
6. Exit

Choose an option:

> """)

    if choice == "1":

        habits = show_habits()

        if not habits:
            print("You don't have any habits to log.")
            continue

        print("\nYour habits:")

        for habit in habits:
            print(f"{habit[0]}. {habit[1]}")

        try:
            habit_id = int(input("\nChoose a habit:\n\n> "))

        except ValueError:
            print("Please enter a valid habit ID.")
            continue

        habit = get_habit_info(habit_id)

        if habit is None:
            print("Habit not found.")
            continue

        data_type = habit[2]
        unit = habit[3]

        if data_type == "bool":

            value_choice = input("""
1- Yes
2- No

> """)

            if value_choice == "1":
                value = True

            elif value_choice == "2":
                value = False

            else:
                print("You can only pick 1 or 2.")
                continue

        elif data_type == "numeric":

            value = input(f"""
How many {unit}?

> """)

            try:
                value = float(value)

            except ValueError:
                print("Please enter a valid number.")
                continue

        try:
            log_habit(habit_id, today, value)
            print("Habit logged successfully!")

        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "2":
        ...

    elif choice == "3":
        ...

    elif choice == "4":

        name = input("What is the habit you want to track: ")

        data_type = input("""
1- Boolean
2- Numeric

> """)

        if data_type == "1":
            data_type = "bool"
            unit = None

        elif data_type == "2":

            unit = input("""
Choose a unit:

1- liter
2- hour
3- minute
4- page
5- rep

> """)

            units = {
                "1": "liter",
                "2": "hour",
                "3": "minute",
                "4": "page",
                "5": "rep"
            }

            if unit in units:
                unit = units[unit]
                data_type = "numeric"

            else:
                print("Invalid unit.")
                continue

        else:
            print("You can only pick 1 or 2.")
            continue

        try:
            add_habit(name, data_type, unit)
            print(f"Successfully added '{name}'!")

        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "5":

        habits = show_habits()

        formatter = [
            "id: ",
            "name: ",
            "data_type: ",
            "unit: ",
            "created_at: "
        ]

        print("--------------------------")

        for habit in habits:
            for item, info in zip(formatter, habit):
                print(item, info)

        print("--------------------------")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")