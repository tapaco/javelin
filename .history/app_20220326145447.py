import streamlit as st
import pyrebase
from urllib.error import HTTPError

# config files
firebaseConfig = {
    'apiKey': "AIzaSyCR0W9FPOAZCWWEINysuE2QGdaZ2tBBGcI",
    'authDomain': "palyanytsya-c3eb4.firebaseapp.com",
    'projectId': "palyanytsya-c3eb4",
    'databaseURL': "https://palyanytsya-c3eb4-default-rtdb.europe-west1.firebasedatabase.app/",
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
password = st.text_input('Town')
s_rooms = st.selectbox('Number of single rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
d_rooms = st.selectbox('Number of double rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
room_type = st.radio('Room type', ['Rooms are in the house I am currently living in', 'Rooms are in a private house or flat'])
women = st.checkbox('I can only host women')
women_child = st.checkbox('I can host women and children')
photos = st.file_uploader('Add photos of your rooms', accept_multiple_files=True) 
other = st.text_input('Other information about you')
submit = st.button('Submit')

form = {
    "name": name,
    "email": email,
    "town": password,
    "single_rooms": s_rooms,
    "double_rooms": d_rooms,
    "room_type": room_type,
    "women": women,
    "women_and_children": women,
    "name": name,
    "other": other
}

try:
    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)

        save_form = db.child("users").push(form, user['idToken'])
        st.success('Thank you, your form has been submitted successfully! We will be in touch once there is a match')
except:
    st.error('There has been an error with submitting your form, please try another email address')
