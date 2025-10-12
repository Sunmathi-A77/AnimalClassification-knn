# 🐾 Zoo Animal Classification Project

## 🐾 Zoo Animal Classifier App

Try the live app here: [Zoo Animal Classifier](https://animalclassification-kkn.streamlit.app/)

A simple web app built with Streamlit that classifies animals into their respective classes based on physical traits using a k-Nearest Neighbors (k-NN) model.

## Usage

1. Select physical traits for the animal using dropdowns and number inputs:  

   - Hair, Feathers, Eggs, Milk, Airborne, Aquatic, Predator, Toothed, Backbone, Breathes, Venomous, Fins, Legs, Tail, Domestic, Catsize  

2. Click Predict Animal Class.  

3. The app will show the predicted animal class:  
   - 🦁 Mammal  
   - 🦅 Bird  
   - 🦎 Reptile  
   - 🐟 Fish  
   - 🐸 Amphibian  
   - 🦐 Bug  
   - 🦂 Invertebrate  

## Project Overview

This project predicts the animal class based on physical traits such as hair, feathers, eggs, milk, legs, and other features.  
A k-NN classifier is trained on the dataset after performing preprocessing, scaling, and handling skewed numerical features (like legs).  

## Dataset

Source: Kaggle - Zoo Dataset, Class Dataset (https://www.kaggle.com/datasets/uciml/zoo-animal-classification) 

## Features:

hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, class_type  

## Steps Performed

### 1. Data Loading & Exploration

- Loaded dataset and checked data info, types, and summary statistics. 

- Checked unique values and distributions of categorical features.  

### 2. Exploratory Data Analysis (EDA)

- Count plots for number of animals per class.

  <img width="400" height="312" alt="image" src="https://github.com/user-attachments/assets/4b21e7a4-527a-4726-951c-8cb6dc756f31" />

- Histogram and boxplots for numerical feature legs.

  <img width="376" height="239" alt="image" src="https://github.com/user-attachments/assets/b660cac9-5a1a-4851-ba31-857ffaa219b9" />

  <img width="334" height="239" alt="image" src="https://github.com/user-attachments/assets/8b211792-241b-435f-9e5b-21db1d68b752" />

### 3. Check Skew and Correlation 

- Checked skew of legs → skew = 0.139 (approximately symmetric).  

- No significant transformation required for legs due to low skew.
  
- Visualized correlation using heatmap

### 4. Feature Selection

- All features selected for k-NN classifier.

- Target variable: class_type.  

### 5. Data Splitting

- Split dataset into train and test sets with stratification:

  - Train: 80%  

  - Test: 20%  

### 6. Feature Scaling

- Standardized features using StandardScaler to improve k-NN performance.  

### 7. Model Training

- Trained a k-Nearest Neighbors (k-NN) classifier. 

- Cross-validation (CV) to find the best k.    

### 8. Model Evaluation

- Confusion matrix to evaluate classification performance.  

### 9. Confusion Matrix:

<img width="425" height="312" alt="image" src="https://github.com/user-attachments/assets/239cb136-e580-4e88-9969-95115c7861c7" />

## Results:

- Best k = 3 

- CV Score = 0.9368  

- Test Accuracy = 1.0

## Technologies & Libraries Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn
