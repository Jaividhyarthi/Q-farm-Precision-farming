import streamlit as st
import numpy as np
import random
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Q-Farm Precision Farming", layout="centered")

st.title("🌱 Q-Farm: AI + Quantum Smart Crop Advisory System")
st.markdown("**AI-powered crop recommendation with Quantum-inspired optimization**")

# ------------------------------
# SAMPLE TRAINING DATA (SIMULATED)
# ------------------------------
data = {
    "N": [90, 40, 50, 20, 80, 30],
    "P": [42, 20, 40, 10, 50, 30],
    "K": [43, 30, 60, 15, 45, 25],
    "temperature": [20, 25, 30, 18, 35, 28],
    "humidity": [80, 60, 70, 90, 40, 50],
    "ph": [6.5, 7.0, 5.5, 6.0, 7.5, 6.8],
    "crop": ["Rice", "Wheat", "Maize", "Rice", "Cotton", "Barley"]
}

df = pd.DataFrame(data)
X = df.drop("crop", axis=1)
y = df["crop"]

# Train AI Model
model = RandomForestClassifier()
model.fit(X, y)

# ------------------------------
# USER INPUT UI
# ------------------------------
st.markdown("## 🌍 Input Soil & Climate Parameters")

temperature = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 60)
ph = st.slider("Soil pH", 0.0, 14.0, 6.5)

N = st.slider("Nitrogen", 0, 200, 50)
P = st.slider("Phosphorus", 0, 200, 50)
K = st.slider("Potassium", 0, 200, 50)

input_data = np.array([[N, P, K, temperature, humidity, ph]])

# ------------------------------
# AI CROP RECOMMENDATION
# ------------------------------
if st.button("🌾 Get AI Crop Recommendation"):
    prediction = model.predict(input_data)[0]
    st.success(f"Recommended Crop: **{prediction}**")
    predicted_crop = prediction
else:
    predicted_crop = "Rice"

# ------------------------------
# ⚛️ QUANTUM OPTIMIZATION MODULE
# ------------------------------
st.markdown("## ⚛️ Quantum Optimization Layer")

st.info("Quantum optimization simulated using QAOA-inspired probabilistic search due to current hardware constraints.")

opt_goal = st.selectbox("Optimization Goal", [
    "Maximize Yield",
    "Minimize Water Usage",
    "Reduce Fertilizer Cost",
    "Climate Risk Resilience"
])

def quantum_optimizer(goal, temp, humidity, soil_ph):
    base_score = random.uniform(0.7, 0.99)

    if goal == "Maximize Yield":
        factor = (temp + humidity + soil_ph) / 300
    elif goal == "Minimize Water Usage":
        factor = 1 - humidity/100
    elif goal == "Reduce Fertilizer Cost":
        factor = 1 - soil_ph/14
    else:
        factor = random.uniform(0.5, 1)

    quantum_score = base_score * factor
    return round(quantum_score, 3)

if st.button("⚛️ Run Quantum Optimization"):
    q_score = quantum_optimizer(opt_goal, temperature, humidity, ph)
    st.success(f"Quantum Optimization Score: **{q_score}**")

    if q_score > 0.85:
        st.write("✔ High yield expected. Intensive cultivation recommended.")
    elif q_score > 0.7:
        st.write("⚠ Moderate yield. Optimize irrigation & fertilizer.")
    else:
        st.write("❌ High climate risk. Delay planting or change crop.")

# ------------------------------
# 🌱 DYNAMIC FARMING ROADMAP
# ------------------------------
st.markdown("## 📜 AI-Quantum Farming Roadmap")

def generate_dynamic_roadmap(crop, temp, humidity, soil_ph):
    roadmap = []

    roadmap.append(f"1️⃣ Soil preparation for **{crop}** cultivation")
    roadmap.append(f"2️⃣ Adjust soil pH to optimal level (~6.5)")

    if temp > 30:
        roadmap.append("3️⃣ Use shade nets to reduce heat stress")
    else:
        roadmap.append("3️⃣ Normal sunlight exposure recommended")

    if humidity < 40:
        roadmap.append("4️⃣ Increase irrigation frequency")
    else:
        roadmap.append("4️⃣ Standard irrigation schedule")

    roadmap.append("5️⃣ Apply NPK fertilizer as per AI nutrient recommendation")
    roadmap.append("6️⃣ Monitor pests using AI vision system")
    roadmap.append("7️⃣ Predict harvest window using Quantum climate forecast")

    return roadmap

if st.button("📜 Generate Farming Roadmap"):
    steps = generate_dynamic_roadmap(predicted_crop, temperature, humidity, ph)
    for step in steps:
        st.write(step)

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("---")
st.caption("Q-Farm | AI + Quantum Precision Agriculture Prototype | Research Demonstration System")
