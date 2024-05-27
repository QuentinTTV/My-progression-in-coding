import hashlib
import pyodbc

def encode_password(password):
    message = hashlib.new("SHA256")
    message.update(password.encode())
    return message.hexdigest()

def get_stored_password(username, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT UserPassword FROM users WHERE UserName = ?", username)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def validate_user(username, entered_password, connection):
    stored_password = get_stored_password(username, connection)
    if stored_password:
        entered_password_hashed = encode_password(entered_password)
        if entered_password_hashed == stored_password:
            return True
        else:
            return False
    else:
        return False

def mainlogon():
    # Get user input
    username = input("What is your username:>")
    password = input("Enter your password:>")
    
    # Encode the password
    entered_password = encode_password(password)
    
    # Connect to the MS Access database
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ty\Documents\passwordbank.accdb;'
    connection = pyodbc.connect(connection_string)
    
    # Validate the user
    if validate_user(username, password, connection):
        print(f"Login successful! Welcome back {username} ")
    else:
        print("Invalid username or password.")
    
    # Close the connection
    connection.close()

if __name__ == "__main__":
    mainlogon()