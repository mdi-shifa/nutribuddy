import streamlit as st
from streamlit_option_menu import option_menu

# Importing Nutribuddy module functions
from welcome import welcome
from food_scanner import food_analyser
from chatbot import chatbot
from prescription import prescription
# from shop import shop
# from feedback import feedback

# Page config
st.set_page_config(
    page_title="Nutribuddy - Your AI Nutritionist",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="auto"
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Nutribuddy',
        ['Welcome', 'Scan Meal', 'Ask Nutribuddy', 'Prescription Analyzer',
           'Shop Smart', 'Contact & Feedback'],
        icons=['house', 'camera', 'chat-dots', 'clipboard-data', 'cart', 'envelope'],
        menu_icon="🥗",
        default_index=0
    )

# Page routing
if selected == 'Welcome':
    welcome()

elif selected == 'Scan Meal':
    food_analyser()

elif selected == 'Ask Nutribuddy':
    chatbot()

elif selected == 'Nutrition Analyzer':
    prescription()

 
# elif selected == 'Shop Smart':
#     shop()

# elif selected == 'Contact & Feedback':
#     feedback()
