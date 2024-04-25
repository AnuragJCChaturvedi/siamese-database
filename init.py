import psycopg2
import os
from psycopg2 import sql

from creds import host, port, dbname, user, password

# SQL commands to create tables
commands = [
    """
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    """,
    """
    CREATE TABLE IF NOT EXISTS users (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v1(),
        firstName VARCHAR(255),
        lastName VARCHAR(255),
        amount DECIMAL(10, 2),
        createdAt TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        updatedAt TIMESTAMP WITHOUT TIME ZONE DEFAULT now()
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS images (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v1(),
        userId UUID NOT NULL,
        rawImage BYTEA,
        createdAt TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        updatedAt TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        FOREIGN KEY (userId) REFERENCES users(id)
    );
    """
]

def create_tables():
    conn = None
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        cur = conn.cursor()
        
        # Create each table
        for command in commands:
            cur.execute(command)
        
        # Close communication with the PostgreSQL database server
        cur.close()
        # Commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

if __name__ == '__main__':
    create_tables()
