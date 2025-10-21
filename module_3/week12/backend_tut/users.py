from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field 
from sqlalchemy import text 
import os 
from dotenv import load_dotenv 
import bcrypt
import uvicorn 

load_dotenv()

app = FastAPI(title = "Simple App", version = "1.0.0")

class Simple(BaseModel):
    name: str = Field(..., example = "Sam Larry")
    email: str = Field(..., example = "sam@gmail.com")
    password: str = Field(..., example = "sam123")

@app.post("/signup")
def signUp(input: Simple):
    try:
        duplicate_query = text("SELECT * FROM user WHERE email = :email")
        existing = db.execute(duplicate_query, {"email": input.email}).fetchall()

        if existing:
            raise HTTPException(status_code = 400, detail = "Email already registered")
        
        query = text("""
            INSERT INTO users (name, email, password)
            VALUES (:name, :email, :password)
        """)

        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedPassword)

        db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword})
        db.commit()

        return {"message": "user created successfully",
                "data": {"name": input.name, "email": input.email}}
    
    except Exception as e:
        raise HTTPException (status_code = 500, detail = str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
    port = int(os.getenv("PORT", 8000))