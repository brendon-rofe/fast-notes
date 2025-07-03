import streamlit as st
import requests

all_notes = requests.get(
  "http://localhost:8000/notes"
)

num_notes = len(all_notes.json())

def get_by_id(note_id):
  response = requests.get(
    f"http://localhost:8000/notes/{note_id}"
  )
  note = response.json()
  st.subheader(f"{note["title"]}")
  st.write(f"{note["content"]}")

st.header("Find Note By ID:")

note_id = st.slider("Pick a note ID", 1, num_notes)

get_by_id(note_id)
