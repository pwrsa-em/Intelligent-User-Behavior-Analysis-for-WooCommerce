import mysql.connector
from mysql.connector import pooling
from config.settings import DB_CONFIG

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'pool'):
            self.pool = pooling.MySQLConnectionPool(
                pool_name='ml_pool',
                pool_size=5,
                **DB_CONFIG
            )

    def get_connection(self):
        return self.pool.get_connection()