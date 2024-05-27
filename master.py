import pyodbc
import hashlib


#master file containing all my database user creation fonctions and gives a simple menu for users to choose 
#if they want to login, create an account or change their current password.

#CURRENT CONNECTION STRING:> r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;"

# AS OF 5/27/2024 ALL PASSWORD ARE HASHED WITH SHA256 FOR SECURE PASSWORD STORAGE

print("###Simple Logon Functions###")
choice = int(input("1: Logon 2: Create Account 3:Change Password/Set password:> "))


#functions
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
    repeater = 0
    while repeater == 0:
        try:
            username = input("What is your username:>")
            password = input("Enter your password:>")
    
            entered_password = encode_password(password)
    
            connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;'
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
    
            if validate_user(username, password, connection):
            #making it look nice
                print(f"Login successful! Welcome back {username} ")
                print("___________________________________________________________________")
                print(f"Here is the user info for account name {username}")
                print("___________________________________________________________________")


                select_query = f"""
                SELECT * FROM users 
                WHERE UserName = ?"""
                cursor.execute(select_query,username)
                for row in cursor.fetchone():
                    print(row)
                    print("___________________________________________________________________")
                    repeater += 1
            else:
                print("Invalid username or password:> ")
        except:
            print("Invalid Username or password:> ")
    
            connection.close()

    
    hang = input("PRESS ANY KEY TO EXIT THE PROGRAM:> ")

def create_usename():
    conn = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;'
    connection = pyodbc.connect(conn)
    cursor = connection.cursor()

    global username_of_create_username
    username_of_create_username = input("Please Enter a Username:> ")

    append_query = "INSERT INTO users ([UserName]) VALUES(?)"
    param = username_of_create_username
    
    cursor.execute(append_query,param)
    cursor.commit()
    print(f"Username:{username_of_create_username} created successfully!")

    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;")
    cursor = conn.cursor()

def enter_email():
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;")
    cursor = conn.cursor()

    enter_username = username_of_create_username
    email = input("Please enter a valid Email adress:> ")
    append_query_email= """
    UPDATE users 
    SET UserEmail = ? 
    WHERE UserName = ?
    """

    param=(email,enter_username)

    conn.execute(append_query_email,param)
    conn.commit()
    conn.close()

    print(f"Email was associated with account: {enter_username} successfully!")


if choice == 1:
    if __name__ == "__main__":
        mainlogon()

if choice == 2:
    success = 0
    while success == 0:
        try:
            create_usename()
            enter_email()
            success += 1        
        except:
            print(f"{username_of_create_username} already in use, please choose another username!")

    def encode_password():
        message = hashlib.new("SHA256")
        password = input("Enter new password:>")

        message.update(password.encode())
        global EncodePassword
        EncodePassword = message.hexdigest()

    def check_entry_hash():
        entrypass = hashlib.new("SHA256")
        entry = input("Enter password to login:>")

        entrypass.update(entry.encode())
        global EncodedEntry
        EncodedEntry = entrypass.hexdigest()

    ##DATABASE CODE
    conn = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;'
    connection = pyodbc.connect(conn)
    cursor = connection.cursor()


    #Defining my DB objects
    table_name = 'users'
    username_field = 'UserName'
    password_field = 'UserPassword'
    username = input("Enter your username again:> ")


    username
    encode_password()

    Value_insert = EncodePassword

    #UPDATE QUERY
    update_query = f"""
    UPDATE {table_name}
    SET {password_field} = ?
    WHERE {username_field} = ?
    """
    cursor.execute(update_query, (Value_insert, username))

    cursor.commit()
    cursor.close()
    connection.close()

    print("Data inserted successfully!")
    hang = input("Press ENTER to close program")


if choice == 3:
    def encode_password():
        message = hashlib.new("SHA256")
        password = input("Enter new password:>")

        message.update(password.encode())
        global EncodePassword
        EncodePassword = message.hexdigest()

    def check_entry_hash():
        entrypass = hashlib.new("SHA256")
        entry = input("Enter password to login:>")

        entrypass.update(entry.encode())
        global EncodedEntry
        EncodedEntry = entrypass.hexdigest()

    ##DATABASE CODE
    conn = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;'
    connection = pyodbc.connect(conn)
    cursor = connection.cursor()


    #Defining my DB objects
    table_name = 'users'
    username_field = 'UserName'
    password_field = 'UserPassword'
    username = input("Enter your username:> ")


    username
    encode_password()

    Value_insert = EncodePassword

    #UPDATE QUERY
    update_query = f"""
    UPDATE {table_name}
    SET {password_field} = ?
    WHERE {username_field} = ?
    """
    cursor.execute(update_query, (Value_insert, username))

    cursor.commit()
    cursor.close()
    connection.close()

    print("Data inserted successfully!")
    hang = input("Press ENTER to close program")