from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import sqlite3
import shutil
import os
import uuid

app = FastAPI()
db_path = "database.db"
img_folder = "images"
os.makedirs(img_folder, exist_ok=True)

# Initialize Database
def init_db():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                image_path TEXT
            )
        """)
        conn.commit()
init_db()

# Model for User
class User(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.post("/add/")
async def add_user(name: str = Form(...), age: int = Form(...), image: UploadFile = File(None)):
    img_path = None
    if image:
        filename = f"{uuid.uuid4()}_{image.filename}"
        img_path = os.path.join(img_folder, filename)
        with open(img_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age, image_path) VALUES (?, ?, ?)", (name, age, img_path))
        conn.commit()
    return {"message": "User added successfully!", "image_path": img_path}

@app.get("/view/")
def view_users():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    return {"users": users}

@app.put("/update/{user_id}")
def update_user(user_id: int, name: str = Form(...), age: int = Form(...)):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
        conn.commit()
    return {"message": "User updated successfully!"}

@app.delete("/delete/{user_id}")
def delete_user(user_id: int):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
    return {"message": "User deleted successfully!"}
