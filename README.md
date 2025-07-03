# Insurance-Cost-Prediction
# 🏥 Insurance Cost Prediction using Machine Learning

This repository contains an end-to-end machine learning project that predicts health insurance premium costs based on individual attributes. The project includes exploratory data analysis (EDA), hypothesis testing, model building, and deployment via a Streamlit web application.

---

## 📌 Problem Statement

Insurance companies need accurate ways to estimate premium charges based on a customer’s age, health conditions, and lifestyle factors. This project aims to:

- Predict insurance premiums using regression models.
- Identify the most influential factors driving premium costs.
- Deploy an interactive and user-friendly web app for premium estimation.

---

## 🎯 Objective

To build a regression model that predicts the insurance premium amount using features such as age, BMI, smoker status, and number of children, and deploy the model via a Streamlit-based web calculator.

---

## 📊 Exploratory Data Analysis (EDA)

- Visualized distributions of premium charges, BMI, and age.
- Boxplots used to identify outliers and compare groups (e.g., smoker vs. non-smoker).
- Correlation heatmap to examine relationships between numerical variables.

### 🔍 Key Findings

- Smoking significantly increases premium charges.
- BMI is positively correlated with charges.
- Age and number of children moderately affect the premium amount.

---

## 🧪 Hypothesis Testing

Statistical tests were used to validate assumptions:

- **T-test**: Premiums of smokers vs. non-smokers — significant difference found.
- **ANOVA**: Number of surgeries vs. premiums — variance in premiums observed.
- **Chi-Square**: Chronic illness and family history — used for categorical dependency check.
- **OLS Regression**: Evaluated the statistical significance of each predictor.

---

## 🤖 Machine Learning Models

### Models Implemented

- Linear Regression
- Random Forest Regressor *(Best Performing)*
- XGBoost (optional extension)

### Model Evaluation Metrics

| Model             | MAE    | RMSE   | R² Score |
| ----------------- | ------ | ------ | -------- |
| Linear Regression | \~4800 | \~6200 | 0.72     |
| Random Forest     | \~3200 | \~4100 | **0.88** |

### Final Model

Random Forest Regressor was selected based on its superior performance in capturing non-linear relationships and lower error values.

---

## 🚀 Deployment: Streamlit Web App

An interactive web application was developed using **Streamlit**. The app:

- Takes user input for age, BMI, smoker status, and children.
- Applies the trained model to predict the premium.
- Displays real-time predictions in a user-friendly format.

### 🔧 Technical Details

- Frontend: Streamlit
- Backend: Pickled Random Forest model
- Local/Colab Deployment supported via **ngrok**

---

## 📁 Repository Structure

```
insurance-cost-prediction/
├── insurance_eda_modeling.ipynb       # EDA, Hypothesis Testing, Modeling
├── app.py                             # Streamlit web app code
├── model.pkl                          # Saved Random Forest model
├── requirements.txt                   # Required libraries
├── README.md                          # Project documentation
```

---

## 💻 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/insurance-cost-prediction.git
cd insurance-cost-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🔍 Example Input and Output

| Input                 | Value        |
| --------------------- | ------------ |
| Age                   | 45           |
| BMI                   | 28.7         |
| Smoker                | Yes          |
| Number of Children    | 2            |
| **Predicted Premium** | **₹ 35,400** |

---

## 📚 Insights & Recommendations

- Smoking is the strongest driver of high premium costs.
- BMI and age are also important predictors.
- The app can help insurance agents quickly generate quotes and understand risk profiles.

---

## 📦 requirements.txt

```
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
statsmodels
pyngrok
```

---

## ✍️ Author

**Lenka Akhila**\*Data Analyst |
*Data Scientist | ML Enthusiast*\
🔗 [LinkedIn](www.linkedin.com/in/lenka-akhila-40097a192

) • 🌐 [Portfolio](https://www.datascienceportfol.io/lenkaakhila119) • 📝 [Medium Blog](https://medium.com/@lenkaakhila119)

---

## 📄 License

This project is intended for educational use only.

