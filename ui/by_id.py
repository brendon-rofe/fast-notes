import streamlit as st
import requests

def get_by_id(note_id):
  response = requests.get(
    f"http://localhost:8000/notes/{note_id}"
  )
  note = response.json()
  if "title" in note:
    st.subheader(f"{note["title"]}")
    st.write(f"{note["content"]}")
  else:
    st.warning("No note with that ID found")

st.header("Find Note By ID:")

note_id = st.slider("Pick a note ID", 0, 5)

get_by_id(note_id)
