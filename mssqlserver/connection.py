import pyodbc

class Cursor:
    SERVER = 'DESKTOP-1S4N35S'
    DATABASE = 'quiz_base'
    USERNAME = 'user'

    @staticmethod
    def make_connection():
        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={Cursor.SERVER};DATABASE={Cursor.DATABASE};UID={Cursor.USERNAME};Trusted_Connection=yes'
        conn = pyodbc.connect(connectionString)
        return conn 
    
    @staticmethod
    def make_cursor(query):
        conn = Cursor.make_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor
    
"""   @staticmethod
    def execute_cursor(query):
        conn = Cursor.make_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor
"""
    