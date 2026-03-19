from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# ------------------------
# Model
# ------------------------
class TeamMember(BaseModel):
    id: str
    name: str
    role: str
    bio: str
    photo: str
    linkedin: str

class TeamMemberCreate(BaseModel):
    name: str
    role: str
    bio: str
    photo: str
    linkedin: str


# ------------------------
# In-memory DB
# ------------------------

db: List[TeamMember] = [
    TeamMember(
        id=str(uuid4()),
        name="Shakthi",
        role="Software Engineer Intern",
        bio="Passionate about building full-stack apps and solving real-world problems.",
        photo="https://i.pravatar.cc/150?img=1",
        linkedin="https://linkedin.com/in/shakthi"
    ),
    TeamMember(
        id=str(uuid4()),
        name="Aarav Mehta",
        role="Frontend Developer",
        bio="Loves crafting beautiful UI and smooth user experiences.",
        photo="https://i.pravatar.cc/150?img=5",
        linkedin="https://linkedin.com"
    ),
    TeamMember(
        id=str(uuid4()),
        name="Riya Sharma",
        role="Backend Developer",
        bio="Enjoys building scalable APIs and working with databases.",
        photo="https://i.pravatar.cc/150?img=6",
        linkedin="https://linkedin.com"
    ),
]


# ------------------------
# Routes
# ------------------------

@app.get("/team", response_model=List[TeamMember])
def get_team():
    return db


@app.post("/team", response_model=TeamMember)
def add_member(member: TeamMemberCreate):
    new_member = TeamMember(id=str(uuid4()), **member.dict())
    db.append(new_member)
    return new_member


@app.put("/team/{member_id}", response_model=TeamMember)
def update_member(member_id: str, updated: TeamMemberCreate):
    for i, m in enumerate(db):
        if m.id == member_id:
            db[i] = TeamMember(id=member_id, **updated.dict())
            return db[i]
    raise HTTPException(status_code=404, detail="Member not found")


@app.delete("/team/{member_id}")
def delete_member(member_id: str):
    global db
    db = [m for m in db if m.id != member_id]
    return {"message": "Deleted"}