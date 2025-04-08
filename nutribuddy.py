import streamlit as st
from streamlit_option_menu import option_menu

# Importing Nutribuddy module functions
from nutribuddy import welcome
from food_scanner import food_scanner
from chatbot import chatbot
from nutrition_analyzer import nutrition_analyzer
from diet_plan import diet_plan
from shopping_links import shop_nutribuddy
from feedback import show_feedback

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
        ['Welcome', 'Scan Meal', 'Ask Nutribuddy', 'Nutrition Analyzer',
         'Get Diet Plan', 'Shop Smart', 'Contact & Feedback'],
        icons=['house', 'camera', 'chat-dots', 'clipboard-data', 'person-check', 'cart', 'envelope'],
        menu_icon="🥗",
        default_index=0
    )

# Page routing
if selected == 'Welcome':
    welcome()

if selected == 'Scan Meal':
    food_scanner()

if selected == 'Ask Nutribuddy':
    chatbot()

if selected == 'Nutrition Analyzer':
    nutrition_analyzer()

if selected == 'Get Diet Plan':
    diet_plan()

if selected == 'Shop Smart':
    shop_nutribuddy()

if selected == 'Contact & Feedback':
    show_feedback()
