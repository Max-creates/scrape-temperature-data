import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM data")
data = cursor.fetchall()
value_x = []
value_y = []

for row in data:
    value_x.append(row[0])
    value_y.append(row[1])


figure = px.line(x=value_x, y=value_y, labels={"x":"Date", "y":"Temperature (C)"})

st.plotly_chart(figure)

connection.close()