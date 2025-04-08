import streamlit as st
import pandas as pd
import os
import re

def feedback():
    st.title("📬 Contact & Feedback - NUTRIBUDDY")
    st.markdown("Have thoughts to share or want to get in touch? Here's how!")

    # 🧑‍🤝‍🧑 Team Contact Info
    st.subheader("👥 Meet Our Team")

    team_data = [
        {"name": "Mohammadi Shifa", "email": "shifamohammadi07@gmail.com"},
        {"name": "Zoya Fathima", "email": "zoya@gmail.com"},
        {"name": "Srushti", "email": "Srushti@gmail.com"},
        {"name": "Tanushri", "email": "Tanushri@gmail.com"},
    ]

    for member in team_data:
        st.markdown(f"""
        **👤 {member['name']}**  
        📧 [Send Email via Gmail](https://mail.google.com/mail/?view=cm&fs=1&to={member['email']})  
        """)

    st.markdown("---")

    # 📣 Feedback Form
    st.subheader("💬 Share Your Feedback")
    st.markdown("We value your input! Please fill out the form below to let us know how we're doing.")

    with st.form(key='user_feedback_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        rating = st.selectbox("Rate your experience with Nutribuddy", [1, 2, 3, 4, 5])
        comments = st.text_area("Any comments, suggestions, or issues you'd like to share?")
        submit_button = st.form_submit_button(label="Submit Feedback")

    if submit_button:
        # Basic validation
        if not name.strip() or not email.strip():
            st.error("Please fill in both your name and email.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Please enter a valid email address.")
        elif not comments.strip():
            st.error("Please share your thoughts in the comment section.")
        else:
            st.success("✅ Thank you for your feedback!")

            # Save feedback to CSV
            feedback_entry = {
                "Name": name,
                "Email": email,
                "Rating": rating,
                "Comments": comments
            }

            feedback_df = pd.DataFrame([feedback_entry])
            if os.path.exists("nutribuddy_user_feedback.csv"):
                feedback_df.to_csv("nutribuddy_user_feedback.csv", mode='a', header=False, index=False)
            else:
                feedback_df.to_csv("nutribuddy_user_feedback.csv", index=False)

            st.info("Your feedback has been recorded successfully.")

# If this file is run directly
if __name__ == "__main__":
    feedback()
