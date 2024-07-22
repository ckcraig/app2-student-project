import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.header("The Best Company")

placeholder_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. Sociis natoque penatibus et magnis 
dis parturient montes. Id faucibus nisl tincidunt eget. Laoreet suspendisse interdum 
consectetur libero id faucibus nisl tincidunt eget. Placerat in egestas erat imperdiet sed 
euismod nisi. Orci nulla pellentesque dignissim enim sit amet venenatis urna cursus. 
Sed elementum tempus egestas sed. Sollicitudin nibh sit amet commodo nulla facilisi nullam. 
Aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh. Ut enim blandit 
volutpat maecenas volutpat blandit aliquam. Id neque aliquam vestibulum morbi blandit. 
Iaculis nunc sed augue lacus. Ut tellus elementum sagittis vitae et leo duis ut. At tellus at 
urna condimentum mattis. Sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque. 
Tincidunt lobortis feugiat vivamus at augue eget arcu dictum. Semper eget duis at tellus.
"""
st.write(placeholder_text)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv", sep=",")
with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])
