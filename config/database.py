import mysql.connector
import os

class DatabaseConfig:
    HOST = "localhost"
    USER = "root"
    PASSWORD = ""  # Adjust for your MySQL setup
    DATABASE = "heart_disease_db"  # Match Android app's database name

    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=DatabaseConfig.HOST,
            user=DatabaseConfig.USER,
            password=DatabaseConfig.PASSWORD,
            database=DatabaseConfig.DATABASE
        )

    SECRET_KEY = os.urandom(24)  # For Flask session security
