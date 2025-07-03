import streamlit as st
import requests

def get_all_notes():
  response = requests.get(
    "http://localhost:8000/notes"
  )
  notes = response.json()
  for note in notes:
    st.subheader(f"{note["title"]}")
    st.write(f"{note["content"]}")
  
get_all_notes()
