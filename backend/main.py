from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

class Note(BaseModel):
  id: Optional[str] = None
  title: str
  content: str

class UpdateNote(BaseModel):
  id: Optional[int] = None
  title: Optional[str] = None
  content: Optional[str] = None

notes = []

app = FastAPI()

@app.get("/notes")
def get_all():
  with open("notes_data.json", "r") as f :
    notes = json.load(f)
    return notes

@app.get("/notes/{note_id}")
def get_by_id(note_id: int):
  with open("notes_data.json", "r") as f:
    notes = json.load(f)
    for note in notes:
      if note["id"] == note_id:
        return note
    return {"Error": "No note with that ID found"}

@app.post("/notes")
def create(note: Note):
  with open("notes_data.json", "r") as f:
    notes = json.load(f)
    id = len(notes) + 1
    new_note = {
      "id": id,
      "title": note.title,
      "content": note.content
    }
    notes.append(new_note)
  with open("notes_data.json", "w") as file:
    json.dump(notes, file, indent=2)

@app.put("/notes/{note_id}")
def update(note_id: int, updated_note: UpdateNote):
  with open ("notes_data.json", "r") as f:
    notes = json.load(f)
  for note in notes:
    if note["id"] == note_id:
      note["title"] = updated_note.title
      note["content"] = updated_note.content
  with open("notes_data.json", "w") as file:
    json.dump(notes, file, indent=2)

@app.delete("/notes/{note_id}")
def delete(note_id: int):
  for note in notes:
    if note["id"] == note_id:
      notes.remove(note)
      with open("notes_data.json", "w") as file:
        json.dump(notes, file, indent=2)
