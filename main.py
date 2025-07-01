from fastapi import FastAPI

notes = []

app = FastAPI()

@app.get("/all")
def all_notes():
    return notes
