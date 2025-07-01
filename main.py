from fastapi import FastAPI
from pydantic import BaseModel
import json

class Note(BaseModel):
  id: int
  title: str
  content: str

notes = []

with open("notes_data.json") as file:
  notes = json.load(file)

app = FastAPI()

@app.get("/all")
def all_notes():
  return notes
