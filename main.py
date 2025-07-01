from fastapi import FastAPI
import json

notes = []

with open("notes_data.json") as file:
  notes = json.load(file)

app = FastAPI()

@app.get("/all")
def all_notes():
  return notes
