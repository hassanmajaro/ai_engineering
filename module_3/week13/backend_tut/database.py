from sqlalchemy import create_engine, text 
from sqlalchemy.orm import sessionmaker 
from pymysql.constants import CLIENT 
from dotenv import load_dotenv 
import os 


load_dotenv()

db_url = f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("db.password")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"

engine = create_engine(
    db_url,
    connect_args = {
        "client_flag": CLIENT.MULTI_STATEMENTS
    }
)

session = sessionmaker(bind = engine)

db = session()

create_query = text("""
    CREATE TABLE IF NOT EXISTS user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS courses(
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(100) NOT NULL,
        level VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS enrollments(
        id INT PRIMARY KEY AUTO_INCREMENT,
        userid INT,
        courseid INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (userid) REFERENCES user(id),
        FOREIGN KEY (courseid) REFERENCES courses(id)
    );
""")

db.execute(create_query)
print("Tables created successfully.")