import streamlit as st
import requests

st.header("Find Note By ID:")

note_id = None
num_notes = None

@st.cache_data
def get_notes():
  response = requests.get(
  "http://localhost:8000/notes"
  )
  if response.status_code == 200:
    return response.json()
  return []

with st.spinner("Getting number of notes..."):
  notes = get_notes()
  num_notes = len(notes)

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
      
      edit = st.button("Edit Note")
      if edit:
        with st.form("edit_note_form"):
          note_title = st.text_input("Title:", placeholder=f"{note["title"]}")
          note_content = st.text_area("Content", placeholder=f"{note["content"]}")
          
          submitted = st.form_submit_button("Update")
          
        

get_by_id(note_id)
