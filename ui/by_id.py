import streamlit as st
import requests

st.header("Find Note By ID:")

note_id = None

with st.spinner("Getting number of notes..."):
  response = requests.get(
  "http://localhost:8000/notes"
  )
  if response.status_code == 200:
    num_notes = len(response.json())

    note_id = st.slider("Pick a note ID", 1, num_notes)

def get_by_id(note_id):
  with st.spinner("Loading note..."):
    response = requests.get(
      f"http://localhost:8000/notes/{note_id}"
    )
    if response.status_code == 200:
      note = response.json()
      st.subheader(f"{note["title"]}")
      st.write(f"{note["content"]}")

get_by_id(note_id)
