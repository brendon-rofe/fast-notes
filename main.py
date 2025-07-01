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

@app.get("/notes")
def get_all():
  return notes

@app.get("/notes/{note_id}")
def get_by_id(note_id: int):
  for note in notes:
    if note["id"] == note_id:
      return note
  return {"Error": "No note with that ID found"}
