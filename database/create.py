from datetime import date
import sqlite3
import random
import uuid

def createTables():
    conn = sqlite3.connect('my_medicalShop.db')
    cursor= conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR(255),
    password VARCHAR(255),
    level INT,
    date_of_creation DATE,
    approved BOOLEAN,
    blocked BOOLEAN,
    name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    pincode VARCHAR(10)
);
'''        )
    
# product table
conn = sqlite3.connect('my_medicalShop.db')
cursor= conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    brand VARCHAR(255),
    description VARCHAR(255),
    price FLOAT,
    category VARCHAR(255),
    stock INTEGER,
    isActive BOOLEAN
);
''')

conn.commit()
conn.close()
    
def createUser(name, password, address, email, phone, pincode):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    user_id = str(uuid.uuid4())
    date_of_creation = date.today()

    try:
        cursor.execute(''' INSERT INTO User (user_id, password, level, date_of_creation, approved, blocked, name, address, email, phone, pincode) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                       (user_id, password, -1, date_of_creation, 0, 0, name, address, email, phone, pincode))
        conn.commit()
        return True  # Data successfully inserted
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
        return False  # Data insertion failed
    finally:
        conn.close()

