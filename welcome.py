import streamlit as st
import os

def welcome():
    # Load Google Fonts
    st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Lora:wght@700&display=swap" rel="stylesheet">""", unsafe_allow_html=True)

    # Centered logo using container
    with st.container():
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("images/logo.jpeg", width=200)  # Ensure this file exists in the 'images' folder
        st.markdown("</div>", unsafe_allow_html=True)

    # Main Heading
    st.markdown("""
        <h1 style="font-family: 'Lora', serif; font-size: 48px; color: #2e7d32; text-align: center;">
        Welcome to Nutribuddy 🥗
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <p style="font-family: 'Roboto', sans-serif; font-size: 24px; color: #555555; text-align: center;">
        Your AI-powered Personalized Nutrition Companion 🍎
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Two equal-width columns
    col1, col2 = st.columns([1, 1])

    # Key Features
    with col1:
        st.markdown("""
        <div style="background-color:#f0fff4; padding:20px; border-radius:10px; text-align:center; height: 100%; box-shadow: 0px 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color:#2e7d32; font-size:24px; margin-bottom:10px; font-family: 'Lora', serif;">Key Features 🌿</h3>
        <ul style="text-align:left; color:#333333; font-size:16px; line-height:1.6; font-family: 'Roboto', sans-serif;">
        <li><strong>🥑 AI Meal Suggestions</strong><br>
        Get AI-powered meal ideas based on your dietary preferences and health goals.</li><br>
        
        <li><strong>📊 Nutritional Analysis</strong><br>
        Upload food images or ingredients to analyze calories, macros, and more.</li><br>

        <li><strong>🧠 Smart Diet Planning</strong><br>
        Create weekly meal plans with balanced nutrition tailored just for you.</li><br>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # More Features
    with col2:
        st.markdown("""
        <div style="background-color:#f0fff4; padding:20px; border-radius:10px; text-align:center; height: 100%; box-shadow: 0px 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color:#2e7d32; font-size:24px; margin-bottom:10px; font-family: 'Lora', serif;">More Features 💡</h3>
        <ul style="text-align:left; color:#333333; font-size:16px; line-height:1.6; font-family: 'Roboto', sans-serif;">
        <li><strong>🍽️ Recipe Analyzer</strong><br>
        Analyze any recipe for its health score and improve it with suggestions.</li><br>

        <li><strong>🤖 Nutrition Chatbot</strong><br>
        Ask any nutrition or diet question and get AI-driven advice instantly.</li><br>

        <li><strong>📥 Feedback & Support to any queries</strong><br>
        Share suggestions, get help, or connect with our support team directly.</li><br>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # How to Use section
    st.markdown("""
    <div style="background-color:#fffde7; padding:20px; border-radius:10px; text-align:center; box-shadow: 0px 4px 8px rgba(0,0,0,0.1);">
    <h3 style="color:#4e342e; font-size:24px; margin-bottom:10px; font-family: 'Lora', serif;">How to Use 🍴</h3>
    <ul style="text-align:left; color:#4e342e; font-size:16px; line-height:1.6; font-family: 'Roboto', sans-serif;">
    <li>📂 Use the sidebar menu to navigate between tools and features.</li>
    <li>📸 Upload food images for analysis and nutritional breakdown.</li>
    <li>💬 Ask diet questions using the Nutrition Chatbot.</li>
    <li>🧾 Use the Recipe Analyzer to break down complex dishes.</li>
    <li>📈 Track and plan meals through AI-generated diet plans.</li>
    <li>📬 Reach out through the feedback section for queries or ideas.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    welcome()
