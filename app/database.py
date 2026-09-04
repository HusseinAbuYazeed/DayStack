import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()
DB_PASSWORD = os.getenv("POSTGRESQL_PASS")


# make a connection object

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres"
                      , password = DB_PASSWORD, port = 5432)

cur = conn.cursor()

# do smth

cur.execute("""

CREATE TABLE IF NOT EXISTS habits (
    id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    data_type VARCHAR(20) NOT NULL
        CHECK (data_type IN ('bool', 'numeric')),

    unit VARCHAR(20)
        CHECK (
            unit IN ('liter', 'hour', 'minute', 'page', 'rep')
            OR unit IS NULL
        ),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CHECK (
        (data_type = 'bool' AND unit IS NULL)
        OR
        (data_type = 'numeric' AND unit IS NOT NULL)
    )
);

""")

conn.commit()

cur.close()
conn.close()