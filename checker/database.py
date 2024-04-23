import psycopg
from environ import Env
import os


settings = Env()
Env.read_env(os.path.join(os.getcwd(), ".settings"))


def get_equal_name(client_name):
    with psycopg.connect(
        dbname=settings("POSTGRES_DB"),
        user=settings("POSTGRES_USER"),
        password=settings("POSTGRES_PASSWORD"),
        host=settings("HOST"),
        port=settings("PORT"),
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT name FROM  names_man WHERE name LIKE {client_name}")
            if cur.fetchone():
                return "man"
            cur.execute(f"SELECT name FROM  names_woman WHERE name LIKE {client_name}")
            if cur.fetchone():
                return "woman"
            else:
                raise Exception("Имя клиента указано неверно проверьте написание.")
