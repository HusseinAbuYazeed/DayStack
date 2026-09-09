from database.connection import get_connection


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


def get_habits():
    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT * FROM habits;")

    habits = cur.fetchall()

    cur.close()
    conn.close()

    return habits