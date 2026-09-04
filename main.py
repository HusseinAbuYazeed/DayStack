import datetime

today = datetime.date.today()
date = today.strftime("%A, %Y-%m-%d")

print("""
========================================
              DAYSTACK
========================================
""")


print(f"Today is {date}")

print(f"Habits you're tracking: ")

print(f"Today's To-Do: ")

print("""
========================================

1. Log habits
2. Check today's to-do list
3. Make a to-do list for a day
4. Add a habit to track
5. Exit

Choose an option:
>
""")