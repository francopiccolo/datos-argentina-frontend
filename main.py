import streamlit as st

st.set_page_config(page_title='Datos Argentina 🤖', layout='wide')

# Define session_state
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []


with st.sidebar:
    st.header("Bienvenidos a Datos Argentina")

st.title("🧠 Datos Argentina 🤖")