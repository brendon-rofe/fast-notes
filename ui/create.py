import streamlit as st

st.header("Create a note:")

with st.form("create_note_form"):
  note_title = st.text_input("Title:")
  note_content = st.text_area("Content")
  
  submitted = st.form_submit_button("Submit")
  
if submitted:
    st.success("New note created!")
