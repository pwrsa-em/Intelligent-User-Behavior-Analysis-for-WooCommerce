from .database import Database

class Repository:
    def __init__(self):
        self.db = Database()

    def execute(self, query, params=None):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        conn.commit()
        cursor.close()
        conn.close()

    def fetchall(self, query, params=None):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or [])
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def fetchone(self, query, params=None):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or [])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
