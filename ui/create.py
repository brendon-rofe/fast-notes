import streamlit as st
import requests

st.header("Create a note:")

with st.form("create_note_form"):
  note_title = st.text_input("Title:")
  note_content = st.text_area("Content")
  
  submitted = st.form_submit_button("Submit")
  
if submitted:
  note = {
    "title": note_title,
    "content": note_content
  }
  with st.spinner("Creating note..."):
    response = requests.post(
      "http://localhost:8000/notes",
      json=note
    )
    if response.status_code == 200:
      st.success("Note created successfully!")
    else:
      st.error("Failed to create new note")
