from typing import List, Dict

CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    code VARCHAR (255)
    fullname VARCHAR(255),
    phone VARCHAR(255),
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (code,fullname, phone)
    VALUES (?, ?, ?)
"""


def get_all_users(execute_query=None) -> List[Dict]:

    return execute_query("SELECT code, fullname, phone FROM users")
