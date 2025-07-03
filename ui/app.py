import streamlit as st

st.title("Fast Notes")

pg = st.navigation(
    [
      st.Page("all.py", title="All Notes"), 
      st.Page("by_id.py", title="Find By ID"), 
      st.Page("create.py", title="Create Note", icon=":material/add_circle:")
    ]
  )
pg.run()
