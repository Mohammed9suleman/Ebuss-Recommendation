import streamlit as st
import pickle
import pandas as pd

# Load models and dataset
@st.cache_resource
def load_models_and_data():
    with open('recommendation_model.pkl', 'rb') as f:
        recommendation_model = pickle.load(f)

    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf_vectorizer = pickle.load(f)

    with open('xgboost_model.pkl', 'rb') as f:
        sentiment_model = pickle.load(f)

    data = pd.read_csv('sample30.csv')

    return recommendation_model, tfidf_vectorizer, sentiment_model, data

# Check if a username exists
def check_username(username, data):
    return username in data['reviews_username'].unique()

# Get recommended products based on user reviews
def get_top_20_recommendations(user_reviewed_products, data):
    similar_users = data[data['id'].isin(user_reviewed_products)]['reviews_username'].unique()
    recommended_products = data[data['reviews_username'].isin(similar_users)]['id'].value_counts().head(20).index.tolist()
    return recommended_products

# Calculate sentiment score for a product
def get_sentiment_score(product_reviews, tfidf_vectorizer, sentiment_model):
    if product_reviews.empty:
        return 0

    tfidf_features = tfidf_vectorizer.transform(product_reviews)
    sentiments = sentiment_model.predict(tfidf_features)
    positive_sentiments = sum(sentiments)
    return positive_sentiments / len(sentiments)

# Generate recommendations based on sentiment analysis
def generate_recommendations(recommended_products, data, tfidf_vectorizer, sentiment_model):
    top_5_products = []

    for product_id in recommended_products:
        product_reviews = data[data['id'] == product_id]['reviews_text']
        product_name = data[data['id'] == product_id]['name'].iloc[0]
        sentiment_score = get_sentiment_score(product_reviews, tfidf_vectorizer, sentiment_model)
        top_5_products.append((product_name, sentiment_score))

    top_5_products = sorted(top_5_products, key=lambda x: x[1], reverse=True)[:5]
    return [prod[0] for prod in top_5_products]

# Main logic for recommendations
def get_recommendations_for_user(username, data, tfidf_vectorizer, sentiment_model):
    user_data = data[data['reviews_username'] == username]
    user_reviewed_products = user_data['id'].unique()
    recommended_products = get_top_20_recommendations(user_reviewed_products, data)
    return generate_recommendations(recommended_products, data, tfidf_vectorizer, sentiment_model)

# Streamlit UI
st.title("Ebuss Personalized Product Recommendations")

# Load models and data
recommendation_model, tfidf_vectorizer, sentiment_model, data = load_models_and_data()

# Input field for username
username = st.text_input("Enter your username:")

if username:
    if check_username(username, data):
        recommendations = get_recommendations_for_user(username, data, tfidf_vectorizer, sentiment_model)
        st.subheader(f"Top 5 Recommendations for {username}:")
        for i, product in enumerate(recommendations, 1):
            st.write(f"{i}. {product}")
    else:
        st.error("Username not found. Please try again.")
else:
    st.info("Please enter a username to get recommendations.")
