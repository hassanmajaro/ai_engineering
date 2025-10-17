from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os


import os 

load_dotenv()

app = FastAPI(title = "Simple FastAPI App", version = "1.0.0")
data = [{"name": "Sam Larry", "age": 20, "track": "AI Developer"},
        {"name": "Bahuballi", "age":21, "track": "Backend Developer"},
        {"name": "John Doe", "age": 22, "track": "Ethical Hacker"}]

class Item(BaseModel):
    name: str = Field(..., example = "Perpetual")
    age: int = Field(..., example = 25)
    track: str = Field(..., example = "Fullstack Developer")

@app.get("/", description = "This endpoint just returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}

@app.get("/get data")
def get_data():
    return data 

@app.post("/create data")
def create_data(req: Item):
    data.append(req.dict())
    return {"Message": "Data Received", "Data": data}

@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    data[id] - req.dict()
    print(data)
    return {"Message": "Data Updated", "Data": data}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host = os.getenv("host"), port = int(os.getenv("port")))