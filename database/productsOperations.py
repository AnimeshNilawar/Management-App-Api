import sqlite3


def add_product(name, brand, description, price, category, stock, isActive):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Products (name, brand, description, price, category, stock, isActive) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, brand, description, price, category, stock, isActive))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def productisActiveAPi(name, isActive):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()

        cursor.execute(''' UPDATE Products SET isActive = ? WHERE name = ?''', (isActive, name))
        
        # Commit the changes
        conn.commit()
        return True  # Added return statement
    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")
        return False  # Added return statement
    finally:
        # Close the connection
        conn.close()


def updatePriceAPi(name, price):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()
        cursor.execute(''' UPDATE Products SET price = ? WHERE name = ?''', (price, name))
        
        # Commit the changes
        conn.commit()
        return True  # Added return statement
    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")
        return False  # Added return statement
    finally:
        # Close the connection
        conn.close()

def updateStockAPi(name, stock):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()
        cursor.execute(''' UPDATE Products SET stock = ? WHERE name = ?''', (stock, name))
        
        # Commit the changes
        conn.commit()
        return True  # Added return statement
    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")
        return False  # Added return statement
    finally:
        # Close the connection
        conn.close()
