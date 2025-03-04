import streamlit as st
import datetime

import streamlit as st
from streamlit_autorefresh import st_autorefresh
import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.getenv('GEMINI_API_KEY')

if 'data' not in st.session_state:
    st.session_state['data'] = []
if 'response' not in st.session_state:
    st.session_state['response'] = ""
tab3, tab1, tab2 = st.tabs(["Plant Status", "Chatbot", "Conditions History"])

# Fetch data from the local server
def fetch_data():
    try:
        response = requests.get("http://127.0.0.1:8000/data")
        if response.status_code == 200:
            data = response.json()
            st.session_state['data'] = json.loads(data)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data: {e}")

fetch_data()

with tab3:
    st.header("Plant Status")
    optimal_temp = (18, 25)
    optimal_humidity = (40, 60)
    
    data_list = st.session_state['data']
    if data_list:
        data = data_list[-1]
        last_temp = float(data['temperature'])
        last_humidity = float(data['humidity'])
        
        if optimal_temp[0] <= last_temp <= optimal_temp[1] and optimal_humidity[0] <= last_humidity <= optimal_humidity[1]:
            emoji = "😃"  # Happy face for good conditions
            message = "Your plant is doing great!"
        else:
            emoji = "😟"  # Sad face for poor conditions
            message = "Your plant needs attention."
        
        st.markdown(f"### Plant Status: {emoji}")
        st.caption(message)

with tab1:
    st.header("Ask About Plant Care")
    query = st.text_input("What is going on with your plant today?")
    if st.button("Submit"):
        prompt = f"Explain: {query}"
        response = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}", json={
            "contents": [{
            "parts":[{"text": prompt}]
            }]})
        response_data = json.loads(response.text)
        text_response = response_data['candidates'][0]['content']['parts'][0]['text']
        print("Gemini Response:", text_response)
        st.session_state['response'] = text_response
    print("Response:", st.session_state['response'])
    st.text_area("Response", st.session_state['response'], height=150)

with tab2:
    st.header("Historical Data")
    if 'data' in st.session_state:
        stock = pd.DataFrame({
            'time': [d["time"] for d in st.session_state['data']],
            'temperature': [d["temperature"] for d in st.session_state['data']]
        })
        st.line_chart(stock, x="time", y="temperature")
        stock = pd.DataFrame({
            'time': [d["time"] for d in st.session_state['data']],
            'humidity': [d["humidity"] for d in st.session_state['data']]
        })
        st.line_chart(stock, x="time", y="humidity")

# Auto-refresh the Streamlit app every 10 seconds
count = st_autorefresh(interval=10000, debounce=True)

