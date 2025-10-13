import psycopg2
import pandas as pd

def connect_db():
    try:
        connection = psycopg2.connect(
            host = "192.168.0.155",
            database = "library_db",
            user = "postgres",
            password = "admin",
            port = 5432
        )
        print("Connection successful")
        return connection 
    except Exception as e:
        print("Connection failed:", e)
        return None 
    
if __name__ == "__main__":
    connect_db()