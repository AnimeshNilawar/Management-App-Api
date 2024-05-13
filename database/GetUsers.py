import sqlite3
import json

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