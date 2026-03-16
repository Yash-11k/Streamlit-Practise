import streamlit as st 
st.title("Chai Maker App(Widgets)")

if st.button("Make chai "):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("massala added to your chai")

tea_type = st.radio("Pick your chia base", ["Milk", "Water", "Cocoa", "Tea-Powder"])
st.write(f"Selected base: {tea_type}.....you have a great choice")


flavours = st.selectbox("Choose Flavour", ["Adrak", "Kesar","Tulsi","Kkari"])
st.write(f"Flavour Choose {flavours}")


sugar = st.slider("Sugar Spoon", 0,5,0) #2 humara default value hai 
st.write(f"Sugar Spoon {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value =10,step=1)
st.write(f"You Select {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome to Ysh chai {name} you chai is on the way.")

dob = st.date_input("Select your date of birth")
st.write(f" Your Date of Birth :{dob}")