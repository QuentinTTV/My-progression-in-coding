import pyodbc

def enter_email():
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=X:\database\passwordbank.accdb;")
    cursor = conn.cursor()

    enter_username = input("Please enter your username:> ")

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

enter_email()