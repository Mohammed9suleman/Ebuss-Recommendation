# Ebuss Recommendation System

## Overview

The Ebuss Recommendation System is designed to enhance the e-commerce experience by providing users with personalized product suggestions. By analyzing user reviews and ratings, the system employs sentiment analysis and collaborative filtering techniques to recommend products that align with individual preferences.

## Features

- **Sentiment Analysis**: Evaluates user reviews to determine sentiment polarity, distinguishing between positive and negative feedback.
- **Collaborative Filtering**: Utilizes user-based and item-based collaborative filtering methods to suggest products based on user behavior and preferences.
- **Model Deployment**: Integrates machine learning models into a web application using Flask and Streamlit for real-time recommendations.

## Project Structure

The repository is organized as follows:

- `Sentiment_Based_Recommendation_System.ipynb`: Jupyter Notebook containing data analysis, model training, and evaluation processes.
- `app.py`: Flask application script for deploying the recommendation system.
- `streamlit_app.py`: Streamlit application script for an interactive user interface.
- `model.py`: Contains functions for building and evaluating machine learning models.
- `sample30.csv`: Dataset used for training and evaluation.
- `requirements.txt`: List of required Python packages.
- `templates/`: Directory containing HTML templates for the Flask application.
- `__pycache__/`: Directory containing cached Python files.
- `*.pkl` files: Serialized machine learning models and vectorizers.

## Installation

To set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mohammed9suleman/Ebuss-Recommendation.git
   cd Ebuss-Recommendation
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation:

- **Flask Application**:
  ```bash
  python app.py
  ```
  Access the application at `http://127.0.0.1:5000/`.

- **Streamlit Application**:
  ```bash
  streamlit run streamlit_app.py
  ```
  Access the application at the URL provided in the terminal.

## Technical Specifications

- **Programming Language**: Python 3.9
- **Libraries**:
  - Data Analysis: pandas, numpy
  - Natural Language Processing: nltk, scikit-learn
  - Machine Learning: scikit-learn, xgboost
  - Web Framework: Flask, Streamlit

- **Models**:
  - Sentiment Analysis: XGBoost Classifier
  - Recommendation System: Collaborative Filtering

## Dataset

The `sample30.csv` file contains user reviews and ratings, which serve as the foundation for training the sentiment analysis model and building the recommendation system.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## Acknowledgements

Special thanks to the open-source community for providing valuable resources and tools that made this project possible. 
