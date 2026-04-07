from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

# Database Connection (try-except block se bahar rakhte hain)
client = MongoClient("mongodb://localhost:27017/")
db = client["my_portfolio"]
collection = db["skills"]

class NayaSkill(BaseModel):
    skill_name: str
    experience_years: int

@app.post("/add-skill")
def add_new_skill(skill_data: NayaSkill):
    # 1. LOGIC ERROR HANDLING: Experience negative nahi ho sakta!
    if skill_data.experience_years < 0:
        # User ko 400 (Bad Request) error bhejenge
        raise HTTPException(
            status_code=400, 
            detail="Error: Experience negative (minus) mein nahi ho sakta bhai! Sahi data bhejo."
        )

    # 2. SERVER ERROR HANDLING: Try-Except block
    # 'try' ke andar hum wo code rakhte hain jisme gadbad hone ka chance ho
    try:
        naya_data = {
            "skill_name": skill_data.skill_name,
            "experience_years": skill_data.experience_years
        }
        
        # Database mein data daalna
        collection.insert_one(naya_data)
        naya_data["_id"] = str(naya_data["_id"])
        
        return {
            "message": "Superb! Data safe tarike se save ho gaya.",
            "data": naya_data
        }
        
    # 'except' tab chalta hai jab 'try' wala code fail ho jaye (jaise MongoDB band ho)
    except Exception as e:
        # Yeh print statement tumhare Terminal (logs) mein aayegi taaki tum as a developer error dekh sako
        print(f"!!! BACKEND LOG ERROR !!! : {e}")
        
        # User ko 500 (Server Error) bhejenge taaki usko technical error na dikhe
        raise HTTPException(
            status_code=500, 
            detail="Server mein abhi kuch issue hai. Humara developer isko check kar raha hai."
        )