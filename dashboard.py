import mysql.connector
from mysql.connector import Error
import streamlit as st

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="yash1436@",
        database="satellite_twin"
    )
    cursor = conn.cursor()
except Error as err:
    st.error(f"Cannot connect to MySQL server: {err}")
    cursor = None
    data = None

if cursor is not None:
    cursor.execute("SELECT battery_level,fuel_level,signal_strength FROM telemetry ORDER BY telemetry_id DESC LIMIT 1")
    data = cursor.fetchone()
else:
    data = None

st.title("Satellite Digital Twin")

st.metric("Battery", f"{data[0]}%")
st.metric("Fuel", f"{data[1]}%")
st.metric("Signal", f"{data[2]}%")