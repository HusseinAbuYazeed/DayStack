import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()
DB_PASSWORD = os.getenv("POSTGRESQL_PASS")


# make a connection object

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres"
                      , password = DB_PASSWORD, port = 5432)

cur = conn.cursor()



cur.execute(
    """
            CREATE TABLE IF NOT EXISTS habit_logs (
            id SERIAL PRIMARY KEY,

            habit_id INTEGER NOT NULL,

            date DATE NOT NULL,

            value TEXT NOT NULL,

            CONSTRAINT fk_habit_logs_habit
                FOREIGN KEY (habit_id)
                REFERENCES habits(id)
                ON DELETE CASCADE
        );
"""
)


conn.commit()

cur.close()
conn.close()