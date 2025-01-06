from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import xgboost as xgb
import streamlit as st

app = Flask(__name__)

# Load necessary files
with open('recommendation_model.pkl', 'rb') as f:
    recommendation_model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

with open('xgboost_model.pkl', 'rb') as f:
    sentiment_model = pickle.load(f)

# Load dataset
data = pd.read_csv('sample30.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    username = request.form['username']

    # Check if username exists
    if username not in data['reviews_username'].unique():
        return render_template('index.html', message="Username not found!")

    # Filter user-specific data
    user_data = data[data['reviews_username'] == username]

    # Get all products reviewed by the user
    user_reviewed_products = user_data['id'].unique()

    # Find top 20 products rated by similar users (example logic)
    similar_users = data[data['id'].isin(user_reviewed_products)]['reviews_username'].unique()
    recommended_products = data[data['reviews_username'].isin(similar_users)]['id'].value_counts().head(20).index.tolist()

    # Predict sentiments for the reviews of these products
    top_5_products = []
    for product_id in recommended_products:
        product_reviews = data[data['id'] == product_id]['reviews_text']
        if product_reviews.empty:
            continue

        # Transform reviews into TF-IDF features
        tfidf_features = tfidf_vectorizer.transform(product_reviews)
        
        # Predict sentiments using the sentiment model
        sentiments = sentiment_model.predict(tfidf_features)
        positive_sentiments = sum(sentiments)

        # Add the product name, positive sentiment percentage, and counts
        product_name = data[data['id'] == product_id]['name'].iloc[0]
        total_reviews = len(product_reviews)
        top_5_products.append((product_name, positive_sentiments / total_reviews))

    # Sort products by the percentage of positive sentiments
    top_5_products = sorted(top_5_products, key=lambda x: x[1], reverse=True)[:5]

    # Extract product names for display
    top_5_product_names = [prod[0] for prod in top_5_products]

    return render_template('index.html', username=username, recommendations=top_5_product_names)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
