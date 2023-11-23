import streamlit as st
import requests
import pandas as pd
import plotly.express as px

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

data = requests.get("https://datos-argentina-backend-qkcide3fmq-ue.a.run.app/").json()
df = pd.DataFrame(data)

st.write(df)

fig = px.line(
    data_frame=df,
    x='year',
    y='pct_ingresos',
    title='% de ingresos sobre el gasto',
)
fig.update_xaxes(tickmode='linear')
st.plotly_chart(fig)