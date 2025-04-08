def chatbot():
    # Importing necessary modules
    import streamlit as st
    import os
    from langchain_google_genai import ChatGoogleGenerativeAI  # for Google chatbot
    from dotenv import load_dotenv  # to load environment variables
    import pyttsx3  # for voice response functionality

    # Load environment variables from .env file
    load_dotenv()

    # Function to handle voice response
    def speak_response(response_content):
        engine = pyttsx3.init()
        engine.say(response_content)
        engine.runAndWait()

    # Set up the Google Generative AI model
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key is None:
        st.error("Google API key is missing. Make sure you have added it to your .env file.")
        return

    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)

    # Main function for the chatbot interface
    st.title("NutriBuddy ChatBot 🥦🤖")
    st.subheader("Your AI-Powered Food & Nutrition Assistant")
    st.markdown("""
    Welcome to NutriBuddy! 🌱  
    Ask anything related to **diet**, **nutrition**, **healthy eating**, **meal planning**, **fitness diets**, and more.  
    Your personalized AI nutritionist is here to help you make better food choices!
    """)

    voice_response = st.checkbox("Enable Voice Response")

    # Initialize chat history if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input for user prompt
    if prompt := st.chat_input("Ask your Nutrition or Diet Query"):
        # Display user's input in the chat
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Try to generate a response
        try:
            # Generate a response from the Google AI model
            response = model.invoke(prompt)
            response_content = response.content

            # Display assistant's response
            st.chat_message("assistant").markdown(response_content)
            st.session_state.messages.append({"role": "assistant", "content": response_content})

            # Voice output if enabled
            if voice_response:
                speak_response(response_content)

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    chatbot()
