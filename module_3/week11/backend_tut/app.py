from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import os


import os 

load_dotenv()

app = FastAPI(title = "Simple FastAPI App", version = "1.0.0")

@app.get("/")
def root():
    return {"Message": "Welcome to my fastAPI Application"}

if __name__ == "  main  ":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host = os.getenv("host"), port = os.getenv("port"))