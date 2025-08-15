# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Attempt to connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',      # Update if needed
            user='root',           # Update to your MySQL username
            password='your_password'  # Update to your MySQL password
        )

        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as query_error:
                print(f"Error while executing query: {query_error}")
            finally:
                if cursor:
                    cursor.close()
    except Error as conn_error:
        print(f"Error while connecting to MySQL: {conn_error}")
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
