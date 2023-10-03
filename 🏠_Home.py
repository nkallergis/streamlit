import streamlit as st
import pandas as pd
import time

radio = st.sidebar.radio("Choose: ",[1,2])
slider = st.slider("Sliiiiide", 0, 10)
st.title(f"TEST {radio}: {slider}")

# Play with tabs
t1, t2, t3 = st.tabs(["T1", "T2", "T3"])
# Tab 1
with t1:
    st.write("Lalalala!")

# Tab 2
with t2:
    st.echo()
    with st.echo():
        st.write("Code bla bla")

# Tab 3
with t3:
    st.toast("Success!")