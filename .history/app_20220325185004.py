import streamlit as st

st.markdown('# Family Matching :flag-ua::flag-gb:')
st.markdown('---')

full_name = st.text_input('First Name')
email = st.text_input('Email')
rooms = st.radio('Number of single rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rooms = st.radio('Number of double rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
house = st.radio('Home type', ['The rooms are in the house I am currently living in', 'The rooms are in a private house or flat'])
postcode = st.text_input('Town')
submit = st.button('Submit Form')


