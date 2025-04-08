import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Replace with your .env key variable name

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Updated product data with working links
product_data = {
    "zepto": [
        {"name": "Fresh Bananas", "price": "60", "link": "https://www.zeptonow.com/c/fruit-and-vegetables/fruits"},
        {"name": "Almonds (100g)", "price": "90", "link": "https://www.zeptonow.com/c/snacks-and-branded-foods/dry-fruits"},
        {"name": "Brown Bread", "price": "45", "link": "https://www.zeptonow.com/c/bakery-cakes-and-dairy/bread-and-buns"},
        {"name": "Explore more foods", "price": "", "link": "https://www.zeptonow.com/search?q=healthy"}
    ],
    "blinkit": [
        {"name": "Apples (1kg)", "price": "180", "link": "https://blinkit.com/prn/apple/cid/148/"},
        {"name": "Greek Yogurt", "price": "120", "link": "https://blinkit.com/prn/greek-yogurt/cid/91/"},
        {"name": "Quinoa (500g)", "price": "160", "link": "https://blinkit.com/s/?q=quinoa"},
        {"name": "Explore more foods", "price": "", "link": "https://blinkit.com/search?q=healthy"}
    ],
    "instamart": [
        {"name": "Spinach Leaves", "price": "40", "link": "https://www.swiggy.com/instamart/category/3148"},
        {"name": "Organic Eggs", "price": "70", "link": "https://www.swiggy.com/instamart/category/3101"},
        {"name": "Protein Bars", "price": "150", "link": "https://www.swiggy.com/instamart/search?q=protein%20bar"},
        {"name": "Explore more foods", "price": "", "link": "https://www.swiggy.com/instamart/search?q=healthy"}
    ]
}

# 🔍 Search product using keyword
def search_product(keyword):
    results = []
    keyword = keyword.lower()
    for store, products in product_data.items():
        for product in products:
            if keyword in product["name"].lower():
                results.append({"store": store, "product": product})
    if not results:
        for store, products in product_data.items():
            results.append({
                "store": store,
                "product": {"name": f"Explore more {store.title()} foods", "price": "", "link": products[-1]["link"]}
            })
    return results

# 💬 Q&A using Gemini
def food_question_answer(question):
    prompt = f"You are a nutrition assistant. Give short, reliable advice for:\n\nUser Question: {question}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "❌ Sorry, I couldn't process your question. Please try again."

# 🎯 Main shop function
def shop():
    st.title("NutriBuddy: Healthy Food Shop & Assistant 🛒💬")

    tab1, tab2 = st.tabs(["🛍️ Shop Healthy Foods", "💬 Ask Food Queries"])

    # ---------------- Tab 1 ----------------
    with tab1:
        st.header("Shop from Zepto, Blinkit & Instamart")
        search_query = st.text_input("Enter a healthy food name or keyword:")
        if st.button("🔍 Search Foods"):
            if search_query:
                results = search_product(search_query)
                st.success(f"Showing results for: {search_query}")
                st.balloons()
                for result in results:
                    product = result["product"]
                    store = result["store"].title()
                    if product["price"]:
                        st.markdown(f"**🛒 {product['name']}**  \n💰 ₹{product['price']}  \n🔗 [Buy on {store}]({product['link']})")
                    else:
                        st.markdown(f"🔗 [Explore more {store} foods here]({product['link']})")
            else:
                st.warning("Please enter a food keyword to search.")

    # ---------------- Tab 2 ----------------
    with tab2:
        st.header("Ask Anything About Food or Supplements 🍎💊")
        user_question = st.text_input("Enter your food/nutrition-related question:")
        if st.button("💬 Get Answer"):
            if user_question:
                with st.spinner("NutriBuddy is thinking..."):
                    answer = food_question_answer(user_question)
                    st.markdown(answer)
            else:
                st.warning("Please type your question first.")

# Run if standalone
if __name__ == "__main__":
    shop()
