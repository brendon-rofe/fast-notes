import streamlit as st
import requests

st.header("Find Note By ID:")

@st.cache_data
def get_notes():
  response = requests.get(
  "http://localhost:8000/notes"
  )
  if response.status_code == 200:
    return response.json()
  return []

if "num_notes" not in st.session_state:
  with st.spinner("Getting number of notes..."):
    notes = get_notes()
    st.session_state.num_notes = len(notes)

def get_by_id(note_id):
  if "note_updated" not in st.session_state:
    st.session_state.note_updated = False

  with st.spinner("Loading note..."):
    response = requests.get(f"http://localhost:8000/notes/{note_id}")
    if response.status_code == 200:
      note = response.json()
      st.divider()
      st.subheader(note['title'])
      st.write(note['content'])
      st.divider()

      col1, col2 = st.columns([1, 1])

      with col1:
        if st.button("✏️ Edit Note", use_container_width=True):
          st.session_state.editing = True

      if "confirm_delete" not in st.session_state:
        st.session_state.confirm_delete = False

      with col2:
        if st.button("🗑️ Delete Note", type="primary", use_container_width=True):
          st.session_state.confirm_delete = True
          
        if st.session_state.get("confirm_delete", False):
          st.warning("Are you sure you want to delete this note?")
          col3, col4 = st.columns([1, 1])
          with col3:
            if st.button("Yes", use_container_width=True, key="confirm_yes"):
              response = requests.delete(f"http://localhost:8000/notes/{note_id}")
              if response.status_code == 200:
                st.success("Note deleted!")
                st.session_state.confirm_delete = False
                st.session_state.num_notes -= 1
                st.rerun()
              else:
                st.error("Failed to delete note")
          with col4:
            if st.button("No", use_container_width=True, key="confirm_no"):
              st.session_state.confirm_delete = False
              st.rerun()
              
              
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
        
        if st.button("Cancel"):
          st.session_state.editing = False
          st.rerun()

if "num_notes" in st.session_state and st.session_state.num_notes > 0:
  note_id = st.slider("Pick a note ID", 1, st.session_state.num_notes)
  get_by_id(note_id)
else:
  st.info("No notes available.")
