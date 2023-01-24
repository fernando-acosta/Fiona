import os

import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )
    return conn


def get_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)