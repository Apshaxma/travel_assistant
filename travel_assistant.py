import streamlit as st
import google.generativeai as genai
from datetime import datetime

# Configure Gemini API Key (Replace with your own key)
genai.configure(api_key="AIzaSyBI-B3Y7KUdcc7AQnYKhHK1aqVqggTlrVg")

def get_travel_itinerary(user_input):
    """Generate a travel itinerary based on user input using Gemini API"""
    prompt = f"""
    You are an AI travel assistant. Based on the user's input:
    {user_input}
    Generate a detailed day-wise itinerary including:
    - Morning, Afternoon, and Evening plans
    - Restaurant recommendations
    - Local transport options
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response.text else "No itinerary generated. Try again."

# Streamlit UI
st.title("AI Travel Planner")

# User Inputs
budget = st.selectbox("Budget", ["Low", "Moderate", "Luxury"])
destination = st.text_input("Destination")
start_date = st.date_input("Start Date", min_value=datetime.today())
days = st.number_input("Number of Days", min_value=1, max_value=30)
purpose = st.text_area("Purpose of Travel (e.g., adventure, relaxation)")
preferences = st.text_area("Any specific preferences? (Food, activities, etc.)")

if st.button("Generate Itinerary"):
    user_input = f"Budget: {budget}, Destination: {destination}, Start Date: {start_date}, Days: {days}, Purpose: {purpose}, Preferences: {preferences}"
    itinerary = get_travel_itinerary(user_input)
    st.write(itinerary)
