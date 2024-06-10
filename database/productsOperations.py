import sqlite3


def add_product(name, brand, price, category, stock, isActive):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Products (name, brand, price, category, stock, isActive) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, brand, price, category, stock, isActive))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
        return False
    finally:
        conn.close()


def updateProductDetails(id, **keywords):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    try:
        for key, value in keywords.items():
            cursor.execute(f''' UPDATE Products SET {key} = ? WHERE product_id = ?''', (value, id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    

def getAllProducts():
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM Products''')
    products = cursor.fetchall()
    conn.close()
    productJson = []  # List to store all products
    
    for product in products:
        tempProduct = {
            'product_id': product[0],
            'name': product[1],
            'brand': product[2],
            'description': product[3],
            'price': product[4],
            'category': product[5],
            'stock': product[6],
            'isActive': product[7]
        }
        productJson.append(tempProduct)
    return productJson

def getSpecificProduct(product_id):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM Products WHERE product_id = ?''', (product_id,))
    product = cursor.fetchone()
    conn.close()
    if product:
        tempProduct = {
            'product_id': product[0],
            'name': product[1],
            'brand': product[2],
            'description': product[3],
            'price': product[4],
            'category': product[5],
            'stock': product[6],
            'isActive': product[7]
        }
        return tempProduct
    else:
        return None