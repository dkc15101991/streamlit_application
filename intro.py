import streamlit as st

st.title("This is a title")

st.subheader("deploying using streamlit app")

st.write("we are learning split first time")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre=="Comedy":
    st.write("you comedy me ---")
elif genre=="Drama":
    st.write("you selected drama")



option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

import streamlit as st

options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)