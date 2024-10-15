import mysql.connector
from mysql.connector import Error

class MySqlConnect:
    @staticmethod
    def get_sql_connection():
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                database="thipython",
                user="root",
                password=""
            )
            # Sửa is_connect() thành is_connected()
            if connection.is_connected():
                print("Kết nối thành công")
                return connection
        except Error as e:
            print(f"Lỗi kết nối: {e}")
            return None
        return None
