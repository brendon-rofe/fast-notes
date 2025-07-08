import streamlit as st
import requests
  
st.header("All notes:")
st.divider()
  
with st.spinner("Loading all notes..."):
  response = requests.get(
    "http://localhost:8000/notes"
  )
  if response.status_code == 200:
    notes = response.json()
    for note in notes:
      st.subheader(note["title"])
      st.write(note["content"])
      st.divider()
