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

**Source: Kaggle - Zoo Dataset, Class Dataset (https://www.kaggle.com/datasets/uciml/zoo-animal-classification) 

## Features:

hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, class_type  

## Steps Performed

### 1. Data Loading & Exploration

- Loaded dataset and checked data info, types, and summary statistics. 

- Checked unique values and distributions of categorical features.  

### 2. Exploratory Data Analysis (EDA)

- Count plots for categorical features like hair, feathers, milk, eggs, etc. 

- Histogram and boxplots for numerical feature legs.  

Visualizations: 

Distribution of Legs 

Feature Counts

### 3. Handling Skew & Outliers

- Checked skew of legs → skew = 0.139 (approximately symmetric).  

- No significant transformation required for legs due to low skew.

- Visualized outliers using boxplots and removed if necessary.  

Visualizations: 

Legs Boxplot

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

## Results:

- Best k = 3 

- CV Score = 0.9368  

- Test Accuracy = 1.0
