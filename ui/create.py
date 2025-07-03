import streamlit as st

st.header("Create a note:")

with st.form("create_note_form"):
  note_title = st.text_input("Your note's title:")
  note_content = st.text_area("Your note's content")
  
  submitted = st.form_submit_button("Submit")
  if submitted:
    st.success("New note created!")
