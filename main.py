import os
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

# --- MONGODB SETUP ---
# Railway khud 'MONGO_URL' provide karta hai, hum bas usse fetch kar rahe hain
MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["my_database"]
collection = db["skills"]

# --- DATA MODEL ---
class NayaSkill(BaseModel):
    skill_name: str
    experience_years: int
    is_expert: bool

# --- ROUTES ---

@app.get("/")
def home():
    return {"message": "API is Live and Running!", "docs": "/docs"}

@app.get("/my-info")
def get_my_info():
    return {
        "name": "Ravi Singh",
        "role": "Chat Executive at Rio AI",
        "goal": "Backend Developer & Data Expert",
        "project": "Gobble Cube"
    }

@app.post("/add-skill")
def add_skill(data: NayaSkill):
    # MongoDB mein data insert karna
    skill_dict = data.dict()
    result = collection.insert_one(skill_dict)
    return {"message": "Skill added successfully!", "id": str(result.inserted_id)}

@app.get("/get-skills")
def get_skills():
    # MongoDB se saara data nikaalna
    all_skills = list(collection.find({}, {"_id": 0}))
    return {"total_skills": len(all_skills), "skills": all_skills}