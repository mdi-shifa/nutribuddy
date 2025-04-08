import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from mypharmacy import search_medicine_skincare  # Still using this for medicine links
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def prescription():
    # Load environment variables (API key)
    load_dotenv()
    genai.configure(api_key="AIzaSyDqqYFp12cYBtEmTuh8WuVlu_FVpzKwLjo")

    def get_gemini_response(input_prompt, image_data, user_prompt):
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
        model = genai.GenerativeModel("gemini-1.5-flash", safety_settings=safety_settings)
        response = model.generate_content([input_prompt, image_data[0], user_prompt])
        return response.text

    def input_image_setup(uploaded_file):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            image_parts = [
                {
                    "mime_type": uploaded_file.type,
                    "data": bytes_data,
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")

    def extract_medicine_names_heuristic(text):
        import re
        potential_medicines = re.split(r'\d+\.\s*|\n|\r|,', text)
        cleaned_medicines = []
        for med in potential_medicines:
            med = med.strip()
            if (
                len(med) > 30 or
                not med or
                med.lower().startswith(("here's", "the prescription", "this plan", "and", "or", "if")) or
                med.lower().endswith("solution.") or
                len(med.split()) > 5
            ):
                continue
            cleaned_medicines.append(med)
        return cleaned_medicines

    st.title("Nutribuddy: Diet Plan & Prescription Analyzer 🥗💊")
    st.write("Welcome to **Nutribuddy's Analyzer**! Upload your diet plan or prescription image, and let our AI break it down into detailed descriptions, dietary suggestions, and links to any mentioned medicines or supplements.")

    st.write("Choose your image (prescription or diet plan)...")
    uploaded_file = st.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png", "webp", "jfif", "afif"], label_visibility="visible")
    image = ""

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    submit = st.button("Analyze Image")
    user_prompt = "Give me a detailed explanation of the diet plan or prescription, including meal items, supplements, nutrients, and medicines along with their purpose."
    info_prompt = """You are a nutrition and health expert.
    You will receive diet or prescription images and must give complete explanations, including supplements and meal insights.
    Always include full text details and purpose behind each item, like {user_prompt}."""

    medicine_prompt = "List all medicines or supplements (if any) mentioned in the document."

    if submit:
        image_data = input_image_setup(uploaded_file)

        info_response = get_gemini_response(info_prompt.format(user_prompt=user_prompt), image_data, "")
        st.subheader("Analyzed Content & Description:")
        st.write(info_response)

        medicine_response = get_gemini_response(medicine_prompt, image_data, "")
        medicine_names = extract_medicine_names_heuristic(medicine_response)

        if medicine_names:
            st.subheader("Detected Medicines/Supplements:")
            medicine_list = ", ".join(medicine_names)
            st.write(medicine_list)

            st.subheader("Medicine/Supplement Purchase Links:")
            for medicine in medicine_names:
                st.markdown(f"### {medicine}")
                results_df = search_medicine_skincare(medicine)
                if results_df is not None and not results_df.empty:
                    for index, row in results_df.head(7).iterrows():
                        st.markdown(f"[{row['Product Name']}]({row['Link']}) - {row['Price']} ₹")
                else:
                    st.write(f"No results found for {medicine}")
                    st.markdown(f"🔗 [Search on 1mg](https://www.1mg.com/search/all?name={medicine})")
                    st.markdown(f"🔗 [Search on Netmeds](https://www.netmeds.com/catalogsearch/result?q={medicine})")
                    st.markdown(f"🔗 [Search on Amazon](https://www.amazon.in/s?k={medicine})")
        else:
            st.write("No medicine or supplement names found using the heuristic approach.")

    st.write("To analyze your diet plan or prescription image, upload a file above and click 'Analyze Image' to get your personalized insights.")
    st.balloons()

if __name__ == '__main__':
    prescription()
