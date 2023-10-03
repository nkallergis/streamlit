import streamlit as st
import pandas as pd
import time

radio = st.sidebar.radio("Choose: ",[1,2])
slider = st.slider("Sliiiiide", 0, 10)
st.title(f"TEST {radio}: {slider}")

people = st.file_uploader("Pick a CSV file")
if people:
    df_people = pd.read_csv(people)
    st.line_chart(df_people)

c1, c2 = st.columns(2)
c1.write("Choice")
c2.write("Result")

with c1:
    c1_check = {}
    for i in range(33):
        c1_check[i] = st.checkbox(f"Y/N ({i+1})")
        if c1_check[i]:
            c2.write("Check!")
        else:
            c2.write("No check!")