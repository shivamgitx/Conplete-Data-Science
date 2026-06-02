import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}")

options=["python","java","c++"]
choice=st.selectbox("Select your favorite programming language",options)
st.write(f"Your favorite programming language is {choice}")

data={
    "Name":["ram","shyam","mohan"],
    "Age":[10,20,30],
    "City":["pune","mumbai","banglore"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv",index=False)
st.write(df)

if name:
    st.write(f"Hello {name}")

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
