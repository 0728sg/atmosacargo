import sqlite3
from db import queries

db_file = 'db/store.sqlite'
db= sqlite3.connect(db_file)
cursor = db.cursor()


async def sql_create():
    if db:
        print("Data base is connected")

        cursor.execute(queries.CREATE_TABLE_USERS)
        db.commit()

async def sql_insert_products( code, fullname, phone):
    if db:
        print("Insert is starting")
        cursor.execute(queries.INSERT_USERS_QUERY, (code, fullname, phone))
        db.commit()