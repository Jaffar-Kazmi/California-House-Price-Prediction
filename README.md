# 🏠 House Price Prediction App

A machine learning web application that predicts house prices based on user input features using a trained regression model and an interactive Streamlit interface.

## Features
- Predict house prices in real-time
- Uses a trained ML pipeline (preprocessing + model)
- Interactive UI built with Streamlit
- Handles:
    - Missing values
    - Feature scaling
    - Categorical encoding
    - Feature engineering

## Model Details
- Models tested:
    - Linear Regression
    - Ridge Regression
    - Lasso Regression
    - Decision Tree
    - Random Forest (Best)
    - Gradient Boosting
- Final model:
    - **RandomForestRegressor** (tuned with GridSearchCV)
- Evaluation Metrics:

| Metric | Value | Description |
|-----------|------------|------------|
| MAE | 33,159 | Mean Absolute Error – average prediction error |
| MAPE | 18.3% | Mean Absolute Percentage Error – average % error |
| RSME | 50,433 | Root Mean Squared Error – penalizes large errors more |
| R2 Score | 0.813 | Proportion of variance explained by the model |

## Dataset
- Based on [California Housing dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices?resource=download)
- Features used:
    - longitude
    - latitude
    - housing_median_age
    - total_rooms
    - total_bedrooms
    - population
    - households
    - median_income
    - ocean_proximity
- Engineered features:
    - rooms_per_household
    - bedrooms_per_room
    - population_per_household
## Tech Stack
- Python
- scikit-learn
- pandas / numpy
- Streamlit
- joblib

## Author

- Syed Jaffar Raza Kazmi

