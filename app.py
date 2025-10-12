import streamlit as st
import pickle
import numpy as np

# ================== PAGE CONFIG ==================
st.set_page_config(page_title="Zoo Classifier", page_icon="🐾", layout="centered")

# ================== CUSTOM CSS ==================
page_bg = """
<style>
/* Gradient background */
.stApp {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 50%, #fbc2eb 100%);
    background-size: cover;
    color: white;
}

/* Transparent container */
.block-container {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.3);
}

/* Title */
h1 {
    text-align: center;
    font-weight: bold;
    color: #ff4500;
    text-shadow: 2px 2px 4px #6a1b9a;
}

/* Inputs and labels */
label, p {
    color: #000000 !important;
    font-weight: bold;
}

/* Colorful selectboxes and number inputs */
div.stSelectbox, div.stNumberInput {
    background: linear-gradient(90deg, #ffecd2 0%, #fcb69f 100%);
    padding: 5px 10px;
    border-radius: 8px;
    margin-bottom: 10px;
    transition: all 0.3s ease;
}
div.stSelectbox:hover, div.stNumberInput:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

/* Button styling */
div.stButton > button {
    background: linear-gradient(90deg, #ff7e5f 0%, #feb47b 100%);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 30px;
    font-size: 16px;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 30px;
    font-size: 14px;
    color: #6a1b9a;
    font-weight: bold;
    text-shadow: 1px 1px 2px #ff4500;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ================== LOAD MODEL ==================
with open("knn_zoo_model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["scaler"]

# ================== APP TITLE ==================
st.markdown(
    "<h1>🐾 Zoo Animal Classifier</h1>",
    unsafe_allow_html=True
)
st.write("Predict the Animal Class based on physical traits.")

# ================== INPUT FEATURES ==================
col1, col2 = st.columns(2)

with col1:
    hair = st.selectbox("Hair", [0, 1])
    feathers = st.selectbox("Feathers", [0, 1])
    eggs = st.selectbox("Eggs", [0, 1])
    milk = st.selectbox("Milk", [0, 1])
    airborne = st.selectbox("Airborne", [0, 1])
    aquatic = st.selectbox("Aquatic", [0, 1])
    predator = st.selectbox("Predator", [0, 1])
    toothed = st.selectbox("Toothed", [0, 1])

with col2:
    backbone = st.selectbox("Backbone", [0, 1])
    breathes = st.selectbox("Breathes", [0, 1])
    venomous = st.selectbox("Venomous", [0, 1])
    fins = st.selectbox("Fins", [0, 1])
    legs = st.selectbox("Legs", [0, 2, 4, 5, 6, 8])
    tail = st.selectbox("Tail", [0, 1])
    domestic = st.selectbox("Domestic", [0, 1])
    catsize = st.selectbox("Catsize", [0, 1])

# ================== PREDICTION ==================
if st.button("Predict Animal Class"):
    features = np.array([[hair, feathers, eggs, milk, airborne, aquatic, predator,
                          toothed, backbone, breathes, venomous, fins, legs,
                          tail, domestic, catsize]])
    
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    class_names = {
        1: "🦁 Mammal",
        2: "🦅 Bird",
        3: "🦎 Reptile",
        4: "🐟 Fish",
        5: "🐸 Amphibian",
        6: "🦐 Bug",
        7: "🦂 Invertebrate"
    }

    st.success(f"Predicted Animal Class: {class_names.get(prediction, 'Unknown')}")

# ================== CREATED BY ==================
st.markdown("<div class='footer'>Created by Sunmathi</div>", unsafe_allow_html=True)
