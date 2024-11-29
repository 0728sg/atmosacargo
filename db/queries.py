CREATE_TABLE_USERS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    code VARCHAR (255),
    fullname VARCHAR(255),
    phone VARCHAR(255)
    )
"""


INSERT_USERS_QUERY = """
    INSERT INTO products (code, fullname, phone)
    VALUES (?, ?, ?)
"""