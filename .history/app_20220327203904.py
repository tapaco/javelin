import streamlit as st
import pyrebase
from PIL import Image
from config import firebaseConfig

# firebase auth
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database 
db = firebase.database()
storage = firebase.storage()

st.markdown('# Families for Ukraine :flag-ua::flag-gb:')
st.markdown('To assist with the Homes For Ukraine scheme, the High Wycombe Ukrainian community is matching Ukrainians with hosts in South East England, through our contacts with family, friends and local NGOs on the ground in Ukraine. Please fill out the form below and once we identify a match, we will reach out to you for introductions and next steps. Any questions, please email contact@familiesforukraine.co.uk')
st.markdown('---')

st.sidebar.markdown('# Useful links :link:')
st.sidebar.markdown('- [Ukrainian Institute London](https://refugee-support.ukrainianinstitute.org.uk/): a one-stop shop for information relevant to UK hosts who are supporting Ukrainians from entering to settling in the country')
st.sidebar.markdown('- [Support Ukraine Coordination Hub](https://supportukraine.uk/): a London-based charity coordinating the combined logistical support and humantarian response of Ukrainians living in the UK helping those back home')
st.sidebar.markdown('- [British-Ukrainian Aid](https://british-ukrainianaid.org/): a UK-based charity supporting everyone suffering from the war and humanitarian crisis in Ukraine, including the injured and wounded, orphaned children, the elderly, internally displaced persons, refugees and families who have lost their breadwinners.')
st.sidebar.markdown('- [Homes for Ukraine](https://homesforukraine.campaign.gov.uk/): the UK Government site which allows UK hosts to sponsor matched Ukrainians')


col1, col2 = st.columns(2)

child_age = 'N/A'

with col1:
    name = st.text_input('First Name')
    email = st.text_input('Email')
    password = '0000' + st.text_input('Town') + '0000'
    s_rooms = st.selectbox('Number of single rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    d_rooms = st.selectbox('Number of double rooms', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    room_type = st.radio('Room type', ['Rooms are in the house I am currently living in', 'Rooms are in a private house or flat'])
    guest_type = st.selectbox('Guest type', ['I can host women', 'I can host women and children', 'I can host women, children and the elderly'])
    if guest_type == 'I can host women and children' or guest_type == 'I can host women, children and the elderly':
        child_age = st.multiselect('What are the ages of children you can cater for?', ['0-3', '3-5', '6-10', '11-15', '16-18'])
        str_child_age = str(child_age)
    dbs = st.selectbox('Are you DBS checked?', ['Not sure', 'Yes', 'No'])
    photos = st.file_uploader('Share a photo of a room', help='Sharing a photo will expedite your chances of being matched') 
    other = st.text_input('Other information about you', placeholder='Hobbies, Interests, Languages, Pets etc')
    info = st.markdown("By submitting this form, you agree to share your data with our NGO partners and our cookie policy. You consent to receive communications from Families For Ukraine. If you wish to withdraw, email contact@familiesforukraine.co.uk")
    submit = st.button('Submit')

with col2:
    image1 = Image.open('mama.jpg')
    image = Image.open('flagua.jpg')
    st.image(image1)
    st.image(image)

form = {
    "name": name,
    "email": email,
    "town": password,
    "single_rooms": s_rooms,
    "double_rooms": d_rooms,
    "room_type": room_type,
    "child_age": child_age,
    "guest_type": guest_type,
    "other": other
}

if submit: 
    user = auth.create_user_with_email_and_password(email, password)
    user = auth.sign_in_with_email_and_password(email, password)

    save_form = db.child("users").push(form, user['idToken'])
    save_photos = storage.child(f"images/users/'{email}'").put(photos, user['idToken'])
    st.success('Thank you, your form has been submitted successfully! We will be in touch once there is a match') 
    #st.error('There has been an error with submitting your form, please try another email address or contact@familiesforukraine.co.uk')

st.markdown('---')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

