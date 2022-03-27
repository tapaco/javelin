import streamlit as st
import pyrebase

# config files
firebaseConfig = {
    'apiKey': "AIzaSyCR0W9FPOAZCWWEINysuE2QGdaZ2tBBGcI",
    'authDomain': "palyanytsya-c3eb4.firebaseapp.com",
    'databaseURL': "https://palyanytsya-c3eb4-default-rtdb.europe-west1.firebasedatabase.app/",
    'projectId': "palyanytsya-c3eb4",
    'storageBucket': "palyanytsya-c3eb4.appspot.com",
    'messagingSenderId': "416655451409",
    'appId': "1:416655451409:web:268d8e2600d4dfeb21d8b0",
    'measurementId': "G-4Z9WJ6FSKW"
} 

# firebase auth
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database 
db = firebase.database()
storage = firebase.storage()

st.markdown('# Family Matching :flag-ua::flag-gb:')
st.markdown('---')

name = st.text_input('First Name')
email = st.text_input('Email')
postcode = st.text_input('Town')
rooms = st.selectbox('Number of single rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rooms = st.selectbox('Number of double rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
house = st.radio('Room type', ['Rooms are in the house I am currently living in', 'Rooms are in a private house or flat'])
women = st.checkbox('I will only host women')
women_child = st.checkbox('I can host women and children')

photos = st.file_uploader('Add photos of your rooms', accept_multiple_files=True) 
other = st.text_input('Other information about you')
submit = st.button('Submit')

if submit: 
    user = auth.create_user_with_email_and_password(email, postcode)
