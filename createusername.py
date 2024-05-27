import pyodbc

#No encryption here, im not encrypting the user's username since its not private info. 
#ONLY encrypt personal info such as passwords, names, DOB, etc...

success = 0
def create_usename():
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;")
    cursor = conn.cursor()

    global username_of_function_create_username
    username_of_function_create_username = input("Please Enter a Username:> ")
    

    append_query_username = "INSERT INTO users ([UserName]) VALUES(?)"
    param_username = username_of_function_create_username
    

    conn.execute(append_query_username,param_username)
    cursor.commit()
    print(f"Username:{username_of_function_create_username} created successfully!")
    
def enter_email():
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;")
    cursor = conn.cursor()

    enter_username = username_of_function_create_username
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

create_usename()
enter_email()