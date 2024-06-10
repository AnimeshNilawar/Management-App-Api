import sqlite3

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

# order table
conn = sqlite3.connect('my_medicalShop.db')
cursor= conn.cursor()   
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR(255),
    product_id VARCHAR(255),
    status BOOLEAN,
    isApproved BOOLEAN,
    quantity INT,
    date_of_create_order DATE,
    total_amount FLOAT
);
''')

conn.commit()
conn.close()
