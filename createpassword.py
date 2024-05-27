import hashlib
import pyodbc

##SHA256 CODE
def encode_password():
    message = hashlib.new("SHA256")
    password = input("ENter new password:>")

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
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ty\Documents\passwordbank.accdb")
cursor = conn.cursor()


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

conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")