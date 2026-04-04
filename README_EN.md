# 🚀 Customer Satisfaction Prediction (Olist E-commerce)

## 🧠 Executive Summary

Machine Learning project focused on predicting customer satisfaction in a real-world e-commerce dataset (Olist).

* 📊 Dataset: +100k real orders
* 🎯 Goal: Classify satisfied vs unsatisfied customers
* 🤖 Models: Logistic Regression, KNN, Decision Tree, Gradient Boosting, XGBoost
* 🏆 Best model: Logistic Regression
* 🔑 Key insight: Delivery delay is the strongest predictor of dissatisfaction
* 📈 Business value: Early identification of at-risk customers to improve retention

---

## 📌 Project Overview

This project analyzes customer behavior and service performance to understand what drives satisfaction in an e-commerce environment.

It covers the full data workflow:

* Data preparation (ETL)
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model training and evaluation
* Business-oriented insights and visualization

---

## 🎯 Objectives

* Identify key drivers of customer satisfaction
* Build and evaluate classification models
* Compare multiple machine learning approaches
* Translate technical results into actionable insights

---

## 📊 Dataset

* Source: Olist Brazilian E-Commerce Dataset (Kaggle)
* Size: ~100k orders
* Type: Real transactional data

**Target variable:**

* `satisfaction` (binary)

**Key features include:**

* Customer reviews
* Delivery time
* Order characteristics
* Seller information

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* Matplotlib / Seaborn
* Power BI
* Jupyter Notebooks
* Excel
* Git & GitHub

---

## 🧪 Project Structure & Methodology

This project follows an **iterative experimental approach**, with multiple notebooks exploring different models and feature configurations.

### Naming Convention

* `01_*` → Data preparation
* `02_*` → Exploratory Data Analysis
* `03_*` → Modeling experiments

---

### 🔹 Data Preparation

* `01_data_preparation.ipynb`
* `01_data_for_dashboard.ipynb`

Includes:

* Data cleaning and merging
* Handling missing values and outliers
* Final dataset generation

---

### 🔹 Exploratory Data Analysis

* `02_eda_general_analysis.py`
* `02_eda_feature_distributions.py`

Includes:

* Target distribution analysis
* Correlation analysis
* Feature exploration
* Data quality checks

---

### 🔹 Modeling

#### Logistic Regression

* `03_model_logistic_regression.ipynb`

#### KNN (multiple experiments)

* `03_model_knn_baseline.ipynb`
* `03_model_knn_experiment_1.ipynb`
* `03_model_knn_experiment_2.ipynb`
* `03_model_knn_experiment_3.ipynb`
* `03_model_knn_feature_1var.ipynb`
* `03_model_knn_feature_3var.ipynb`
* `03_model_knn_feature_5var.ipynb`

#### Tree-based Models

* `03_model_decision_tree.ipynb`

#### Boosting Models

* `03_model_gradient_boosting_2_features.ipynb`
* `03_model_gradient_boosting_3_features.ipynb`
* `03_model_xgboost.ipynb`

👉 Multiple notebooks reflect **controlled experimentation with different configurations and feature sets**

---

## 🤖 Model Evaluation

Models were evaluated using:

* Accuracy
* Recall (Sensitivity)
* Specificity ⚠️ *(key metric in this project)*
* F1-score
* ROC-AUC

### 🏆 Final Model: Logistic Regression

Selected due to:

* Best overall balance across metrics
* Strong specificity → reduces false positives

👉 This is critical to avoid incorrectly flagging satisfied customers as dissatisfied.

---

## 📈 Results

![Model comparison](olist-project-files/images/model_comparison_heatmap.jpg)

* Some models achieve higher accuracy but fail in recall or specificity
* Logistic Regression provides the most stable performance

---

## 🔍 Key Insights

* 🚚 **Delivery delay is the main driver of dissatisfaction**
* ⭐ Ratings are heavily skewed toward maximum values (imbalanced dataset)
* 📦 Product-related features (price, category, size) have low predictive power
* ❌ Late or failed deliveries strongly correlate with negative reviews

---

## 📊 Visualization (Power BI)

Two dashboards were developed:

* Business overview
* Delivery delay analysis

![Dashboard overview](olist-project-files/images/dashboard_overview.jpg)
![Delay analysis](olist-project-files/images/dashboard_delay_analysis.jpg)

---

## ⚠️ Limitations

* Imbalanced dataset (majority positive ratings)
* No use of textual review data
* Limited feature depth for behavioral analysis
* Potential improvement using NLP techniques

---

## 🚀 Future Improvements

* Incorporate NLP on customer reviews
* Use semantic embeddings
* Hyperparameter tuning
* Apply resampling techniques (SMOTE, etc.)
* Build a production-ready pipeline

---

## ▶️ How to Run

```bash
git clone <repository_url>
cd <repository>
pip install -r requirements.txt
```

Run notebooks in order:

1. `01_*` → Data preparation
2. `02_*` → EDA
3. `03_*` → Modeling

---

## 📁 Additional Resources

* Documentation files available in `/docs`
* Dashboard available in `/reports`
* Dataset available on Kaggle

---

## 💡 Conclusion

This project demonstrates the ability to:

* Work with complex real-world datasets
* Perform end-to-end data analysis
* Build and evaluate machine learning models
* Extract and communicate business insights

The main value lies in identifying critical factors affecting customer satisfaction and enabling data-driven decision-making.

---
