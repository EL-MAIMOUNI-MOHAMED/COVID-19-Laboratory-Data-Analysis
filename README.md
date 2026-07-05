<<<<<<< HEAD
# 🦠 COVID-19 Laboratory Data Analysis

> Exploratory Data Analysis (EDA) and Statistical Analysis of COVID-19 laboratory test results using Python.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-blue?style=for-the-badge)
![SciPy](https://img.shields.io/badge/SciPy-Statistics-8CAAE6?style=for-the-badge&logo=scipy)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📖 Overview

This project performs an **Exploratory Data Analysis (EDA)** on a COVID-19 clinical dataset containing laboratory test results from patients.

The objective is to:

- Clean and preprocess the dataset
- Explore missing values
- Visualize laboratory measurements
- Compare positive and negative COVID-19 patients
- Analyze correlations between biomarkers
- Perform statistical hypothesis testing
- Identify laboratory variables significantly associated with COVID-19 positivity

---

## 📂 Dataset

The dataset is stored as:

```
dataset.xlsx
```

It contains:

- Patient laboratory measurements
- SARS-CoV-2 test result
- Influenza test results
- Patient identifier
- Numerous blood biomarkers

---

## 🚀 Features

### 📊 Data Loading

- Load Excel dataset using Pandas
- Create a working copy of the data

---

### 🧹 Data Cleaning

- Remove columns with more than **90% missing values**
- Remove unnecessary identifiers (`Patient ID`)
- Analyze missing values percentage

---

### 📈 Exploratory Data Analysis

The notebook provides:

- Dataset dimensions
- Data types
- Missing value analysis
- Class distribution
- Histograms for every numerical variable
- Density plots comparing COVID-positive vs COVID-negative patients

---

### 🔬 Statistical Analysis

The project performs:

- Correlation analysis using a heatmap
- Cross-tabulation between Influenza and COVID-19
- Detection of patients with other recorded diseases
- Independent Welch's T-Test for every laboratory variable

Only variables with:

```
p-value < 0.05
```

are considered statistically significant.

---

## 📊 Visualizations

The notebook generates:

- Histogram distributions
- KDE plots
- Positive vs Negative comparisons
- Correlation heatmap

Example analyses include:

- Distribution of blood biomarkers
- COVID-positive vs COVID-negative laboratory values
- Biomarker correlations
- Significant laboratory features

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/EL-MAIMOUNI-MOHAMED/COVID-19-Laboratory-Data-Analysis.git
```

Go inside the project

```bash
cd covid-lab-analysis
```

Install dependencies

```bash
pip install pandas matplotlib seaborn scipy openpyxl
```

---

## ▶️ Usage

Place your dataset inside the project folder:

```
dataset.xlsx
```

Then run:

```bash
python analysis.py
```

or open the notebook in:

- Google Colab
- Jupyter Notebook

---

## 📁 Project Structure

```
COVID-19-Laboratory-Data-Analysis/
│
├── dataset.xlsx
├── analysis.ipynb
├── COVID-19-EDA.py
├── README.md
└── requirements.txt
```

---

## 📌 Statistical Methods

The project applies:

- Descriptive Statistics
- Exploratory Data Analysis (EDA)
- Correlation Matrix
- Welch's Independent T-Test
- Missing Data Analysis

---

## 🎯 Project Objectives

- Understand laboratory characteristics of COVID-19 patients
- Identify biomarkers associated with positive SARS-CoV-2 diagnosis
- Visualize medical laboratory data
- Prepare data for Machine Learning classification

---

## 📈 Future Improvements

- Data imputation
- Feature engineering
- Machine Learning models
  - Logistic Regression
  - Random Forest
  - XGBoost
  - Support Vector Machine
- Feature importance analysis
- Model evaluation
- ROC Curve & AUC
- Hyperparameter tuning

---

## 📚 References

- Hastie, T., Tibshirani, R., & Friedman, J. *The Elements of Statistical Learning.*
- SciPy Documentation: https://docs.scipy.org/doc/scipy/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Seaborn Documentation: https://seaborn.pydata.org/
- Matplotlib Documentation: https://matplotlib.org/

---

## 👨‍💻 Author

**Mohamed EL MAIMOUNI**

💼 Full-Stack Developer | AI & Machine Learning Engineer

- GitHub: https://github.com/EL-MAIMOUNI-MOHAMED
- LinkedIn: https://www.linkedin.com/in/mohamed-el-maimouni/

---

⭐ If you found this project useful, consider giving it a star!
=======
# COVID-19-Laboratory-Data-Analysis
🦠 Exploratory Data Analysis (EDA) of COVID-19 laboratory data using Python. This project cleans and analyzes clinical data, visualizes biomarker distributions, performs correlation analysis and Welch's t-tests, and identifies significant laboratory features associated with SARS-CoV-2 positive cases.
>>>>>>> d72419443b5f52a0195755034efce5554de6a816
