import datetime
from app.habits import add_habit, get_habits


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
        ...

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
        habits = get_habits()
       
        for habit in habits:
            print(habit)
    
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")