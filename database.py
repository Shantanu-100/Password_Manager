import mysql.connector
from cryptography.fernet import Fernet

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your password",
        database="your database name"
    )

def load_key():
    return open("secret.key", "rb").read()

def add_user(username, password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, encrypted_password))
    conn.commit()
    cursor.close()
    conn.close()

def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        key = load_key()
        f = Fernet(key)
        encrypted_password = result[0]
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password == password
    return False

def add_password(site, username, password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (site, username, password) VALUES (%s, %s, %s)", (site, username, encrypted_password))
    conn.commit()
    cursor.close()
    conn.close()

def get_password(site, username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM passwords WHERE site = %s AND username = %s", (site, username))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        key = load_key()
        f = Fernet(key)
        encrypted_password = result[0]
        return f.decrypt(encrypted_password).decode()
    return None
