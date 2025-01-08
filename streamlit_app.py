import streamlit as st
import requests  # To communicate with Flask backend
import json

# Set the Flask app URL (assumes the Flask app is running locally)
FLASK_API_URL = "http://127.0.0.1:5000/recommend"

st.title('Product Recommendation System')

# Input for username
username = st.text_input('Enter username')

if username:
    # Send request to Flask backend
    response = requests.post(FLASK_API_URL, data={'username': username})
    
    # Handle response
    if response.status_code == 200:
        # Extract recommended product names from Flask response
        result = response.json()
        
        if 'recommendations' in result:
            st.subheader(f"Top 5 Recommendations for {username}:")
            for i, product in enumerate(result['recommendations'], 1):
                st.write(f"{i}. {product}")
        else:
            st.error(result.get('message', 'An error occurred.'))
    else:
        st.error("Failed to get recommendations. Please try again.")
else:
    st.info("Please enter a username to get recommendations.")
