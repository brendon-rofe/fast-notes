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
    if "note_updated" not in st.session_state:
        st.session_state.note_updated = False

    with st.spinner("Loading note..."):
        response = requests.get(f"http://localhost:8000/notes/{note_id}")
        if response.status_code == 200:
            note = response.json()
            st.subheader(note['title'])
            st.write(note['content'])

            if st.button("Edit Note"):
                st.session_state.editing = True

            if st.session_state.get("editing", False):
                with st.form("edit_note_form"):
                    note_title = st.text_input("Title:", value=note['title'])
                    note_content = st.text_area("Content", value=note['content'])
                    submitted = st.form_submit_button("Update")

                    if submitted:
                        updated_note = {
                            "title": note_title,
                            "content": note_content
                        }
                        with st.spinner("Updating note..."):
                            response = requests.put(
                                f"http://localhost:8000/notes/{note['id']}",
                                json=updated_note
                            )
                            if response.status_code == 200:
                                st.session_state.note_updated = True
                                st.session_state.editing = False
                                st.success("Note Updated")
                            else:
                                st.error("Failed to update note")
        else:
            st.error("Note not found.")  

get_by_id(note_id)
