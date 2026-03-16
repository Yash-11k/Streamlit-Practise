import streamlit as st 
st.title("Welcome to my Streamlit App")
st.subheader("Go with the streamlit")
st.text("Made by Yash for learing purpose")
st.write("Choose your best Programming Language")

pr_lang = st.selectbox("Your fav chai : ", ["c++", "Python", "GO", "Java"])
st.write(f"You chose {pr_lang}: Excellent choice ")

st.success("Your Programming choice is good")

