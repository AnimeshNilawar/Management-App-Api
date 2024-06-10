import sqlite3
from datetime import date

def orderDetails(user_id, product_id, status, quantity, total_amount):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    date_of_create_order = date.today()

    try:
        cursor.execute(''' INSERT INTO Orders (user_id, product_id, status, quantity, date_of_create_order, total_amount) VALUES (?, ?, ?, ?, ?, ?)''', 
                       (user_id, product_id, status, quantity, date_of_create_order, total_amount))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()


def updateOrderDetails(id, **keywords):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    try:
        for key, value in keywords.items():
            cursor.execute(f''' UPDATE Orders SET {key} = ? WHERE id = ?''', (value, id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()

def getAllOrders():
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM Orders''')
    orders = cursor.fetchall()
    conn.close()
    orderJson = []  # List to store all orders
    
    for order in orders:
        tempOrder = {
            'id': order[0],
            'user_id': order[1],
            'product_id': order[2],
            'status': order[3],
            'isApproved': order[4],
            'quantity': order[5],
            'date_of_craete_order': order[6],
            'total_amount': order[7]
        }
        orderJson.append(tempOrder)
    return orderJson

def getOrderDetailsByFilter(user_id, isApproved):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM Orders WHERE user_id = ? AND isApproved = ?''', (user_id, isApproved))
    orders = cursor.fetchall()
    conn.close()
    orderJson = []  # List to store all orders
    
    for order in orders:
        tempOrder = {
            'id': order[0],
            'user_id': order[1],
            'product_id': order[2],
            'status': order[3],
            'isApproved': order[4],
            'quantity': order[5],
            'date_of_craete_order': order[6],
            'total_amount': order[7]
        }
        orderJson.append(tempOrder)
    return orderJson