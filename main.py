from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

class Note(BaseModel):
  id: Optional[str] = None
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

@app.post("/notes")
def create(note: Note):
	id = len(notes) + 1
	new_note = {
		"id": id,
		"title": note.title,
		"content": note.content
	}
	notes.append(new_note)
	with open("notes_data.json", "w") as file:
		json.dump(notes, file, indent=2)

