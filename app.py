import streamlit as st

st,title("Temp conveter")
celcius = st.number_input
fahrenheit = celcius*9/5+32
st.write(f"{celcius} c son {fahrenheit} f")