from datetime import date
import sqlite3
import random
import uuid

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


def update_User_details(id, **keywords):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    try:
        for key, value in keywords.items():
            cursor.execute(f''' UPDATE User SET {key} = ? WHERE id = ?''', (value, id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()

def getAllUser():
    # Get all users from database
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM User''')
    users = cursor.fetchall()
    conn.close()
    userJson = []  # List to store all users
    
    for user in users:
        tempUser= {
            'id': user[0],
            'user_id': user[1],
            'password': user[2],
            'level': user[3],
            'date_of_creation': user[4],
            'approved': user[5],
            'blocked': user[6],
            'name': user[7],
            'address': user[8],
            'email': user[9],
            'phone': user[10],
            'pincode': user[11]
        }
        userJson.append(tempUser)  # Append tempUser to userJson list

    return userJson
      
def getSpecificUser(user_id):  # Change argument name to userID
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM User WHERE user_id = ?''', (user_id,))  # Use userID as parameter
    users = cursor.fetchall()
    conn.close()
    userJson = []  # List to store all users
    
    for user in users:
        tempUser= {
            'id': user[0],
            'user_id': user[1],
            'password': user[2],
            'level': user[3],
            'date_of_creation': user[4],
            'approved': user[5],
            'blocked': user[6],
            'name': user[7],
            'address': user[8],
            'email': user[9],
            'phone': user[10],
            'pincode': user[11]
        }
        userJson.append(tempUser)  # Append tempUser to userJson list

    return userJson 
