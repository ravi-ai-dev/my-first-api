from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import motor.motor_asyncio
import os

app = FastAPI()

# --- DATABASE CONNECTION ---
# Railway par MONGO_URL set hona chahiye, varna local pe chalega
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.rio_ai_db

# --- MODELS (Purana + Naya) ---

# Purana Model (Skills wala)
class Skill(BaseModel):
    name: str
    level: str

# Naya Model (Arrangement wala)
class Arrangement(BaseModel):
    cx_mobile: str
    medicine_name: str
    warehouse: str  # Gaur City / Sector 78 / Indirapuram
    executive_name: str
    advance_amount: int
    status: str = "Pending"
    timestamp: datetime = datetime.now()

# --- ENDPOINTS ---

@app.get("/")
async def root():
    return {"message": "Rio AI API is Live and Running!"}

# 1. Purana Endpoint: My Info
@app.get("/my-info")
async def get_info():
    return {
        "name": "Ravi Singh",
        "role": "AI Automation & Backend Developer",
        "company": "Rio AI Medicine"
    }

# 2. Naya Endpoint: Add Arrangement (Fake Data Testing ke liye)
@app.post("/add-arrangement")
async def add_arrangement(data: Arrangement):
    # Dictionary mein convert karke DB mein save karna
    new_doc = data.dict()
    new_doc["timestamp"] = datetime.now() # Real time save karne ke liye
    result = await db.arrangements.insert_one(new_doc)
    return {"message": "Arrangement Recorded Successfully", "id": str(result.inserted_id)}

# 3. Naya Endpoint: Get Zone Wise Data
@app.get("/get-arrangements/{zone}")
async def get_by_zone(zone: str):
    cursor = db.arrangements.find({"warehouse": zone})
    results = await cursor.to_list(length=100)
    for res in results:
        res["_id"] = str(res["_id"]) # MongoDB ki ID ko string banana padta hai
    return results

# 4. Status Update (Jab medicine mil jaye)
@app.put("/update-status/{cx_mobile}")
async def update_status(cx_mobile: str, status: str):
    result = await db.arrangements.update_one(
        {"cx_mobile": cx_mobile}, 
        {"$set": {"status": status}}
    )
    if result.modified_count:
        return {"message": f"Status updated to {status}"}
    raise HTTPException(status_code=404, detail="Order not found")