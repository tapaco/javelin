import streamlit as st

st.markdown('# Family Matching :flag-ua::flag-gb:')
st.markdown('---')

full_name = st.text_input('Full Name')
email = st.text_input('Email')
mobile = st.text_input('Mobile')
rooms = st.radio('Number of rooms', [1, 2, 3, 4, '5+'])
postcode = st.text_input('First Half Of Post Code e.g. HP13')
submit = st.button('Submit Form')
