import streamlit as st
import requests
import pandas as pd

from src.config import BACKEND_URL
from src.charts import pct_ingresos_sobre_gasto_fig

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

# % ingresos sobre gasto
data = requests.get(BACKEND_URL + 'pct_ingresos_sobre_gasto').json()
df = pd.DataFrame(data)
fig = pct_ingresos_sobre_gasto_fig(df)
st.plotly_chart(fig)