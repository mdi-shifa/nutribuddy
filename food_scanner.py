import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

def food_analyser():
    # Configure the API key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Load Gemini Vision Model and get response
    def get_gemini_response(image, prompt):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([image[0], prompt])
        return response.text

    # Convert uploaded image to model input format
    def input_image_setup(uploaded_file):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            return [{"mime_type": uploaded_file.type, "data": bytes_data}]
        else:
            raise FileNotFoundError("No file uploaded")

    # UI
    st.title("🍽️ Nutribuddy's AI Food Analyzer")
    st.write(
        """
        Upload an image of your meal and let Nutribuddy break it down for you!  
        Our AI will identify the food item and provide nutritional insights, suggestions, and tips to keep your health on track.
        """
    )

    uploaded_file = st.file_uploader("Choose a food image for analysis...", type=["jpg", "jpeg", "png", "webp", "jfif", "afif"])
    image = None

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Meal Image", use_column_width=True)

        # Food image analysis prompt
        input_prompt = f"""Image: (content of the uploaded food image)
        You are an expert AI nutritionist trained to analyze meals from images.
        Analyze the image and provide the following information:

        * Identified Food: Name the food items or ingredients seen in the image.
        * Calories Estimate: Approximate total calories based on portion size and food types.
        * Macronutrients: Provide estimates of carbohydrates, protein, and fat content.
        * Dietary Suitability: Is the meal suitable for specific diets (e.g., keto, diabetic, vegetarian)?
        * Suggestions: Provide healthy alternatives or preparation suggestions to improve the meal.

        If the image doesn't contain food, inform the user clearly.

        Use headings in your response for clarity.
        """

        submit = st.button("Analyze Meal")
        st.warning("Meal analysis is based on visible ingredients and general nutritional data.")

        disclaimer = (
            "**Disclaimer:** This AI tool is designed to provide approximate nutritional information from food images. "
            "Results may not be 100% accurate and should not replace advice from certified nutritionists or dietitians."
        )

        if submit:
            if image:
                with st.spinner("Analyzing Meal..."):
                    image_data = input_image_setup(uploaded_file)
                    response = get_gemini_response(image_data, input_prompt)
                st.subheader("Analysis Result:")
                st.write(response)
                st.warning(disclaimer)
                st.balloons()
            else:
                st.error("Please upload an image to proceed.")
    else:
        st.info("Upload an image of your food to get started!")
        st.write(
            """
            To get a breakdown of your meal, upload an image using the uploader above, then click 'Analyze Meal' to get detailed insights.
            """
        )
        st.balloons()

if __name__ == "__main__":
    food_analyser()
