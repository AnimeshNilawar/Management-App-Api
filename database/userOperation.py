import sqlite3

def blockedAPi(id, blocked):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()

        cursor.execute(''' UPDATE User SET blocked = ? WHERE id = ?''', (blocked, id))
        
        # Commit the changes
        conn.commit()
        return True  # Return True if the update was successful
    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")
        return False  # Return False if there was an error
    finally:
        # Close the connection
        conn.close()

def ApprovedAPi(id, approved):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()

        cursor.execute(''' UPDATE User SET approved = ? WHERE id = ?''', (approved, id))
        
        # Commit the changes
        conn.commit()
        return True  # Return True if the update was successful
    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")
        return False  # Return False if there was an error
    finally:
        # Close the connection
        conn.close()

def updateUserLevelAPi(id, level):
    try:
        conn = sqlite3.connect('my_medicalShop.db')
        cursor = conn.cursor()

        cursor.execute(''' UPDATE User SET level = ? WHERE id = ?''', (level, id))
        
        # Commit the changes
        conn.commit()
        return True  # Return True if the update was successful
    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")
        return False  # Return False if there was an error
    finally:
        # Close the connection
        conn.close()
