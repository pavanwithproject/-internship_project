import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 

# Configuration
st.set_page_config(
    page_title="Personal Fitness Tracker",
    layout="centered",
)

# BMI Calculation
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

# Fitness Level
def get_fitness_level(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Calories Burned
def calculate_calories(activity_type, weight, time):
    activity_calories_per_minute = {
        "Gym": 7, 
        "Cycling": 5,
        "Running": 10,
        "Walking": 3,
        "Swimming": 8,
        "Yoga": 4,
        "Jump Rope": 12
    }
    calories_burned = activity_calories_per_minute.get(activity_type, 0) * time
    return calories_burned

# Water Intake
def calculate_water_intake(weight, activity_time):
    water_intake = weight * 30  
    extra_water = activity_time * 10  
    return water_intake + extra_water

# Model Training
def train_model():
    data = {
        "age": [22, 34, 45, 23, 55, 30, 25, 40, 60, 35],
        "height": [175, 165, 180, 170, 160, 180, 167, 172, 158, 162],
        "weight": [70, 80, 95, 65, 100, 75, 72, 85, 110, 90],
        "activity_time": [30, 45, 20, 60, 15, 40, 50, 30, 10, 25],
        "fitness_level": ["Normal weight", "Overweight", "Obese", "Normal weight", "Obese", "Normal weight", "Normal weight", "Overweight", "Obese", "Overweight"]
    }
    df = pd.DataFrame(data)

    X = df[["age", "height", "weight", "activity_time"]]
    y = df["fitness_level"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

    return model

# Title
st.title("🏋️‍♂️ Personal Fitness Tracker")

# Sidebar Inputs
st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=25)
height = st.sidebar.slider("Height (in cm)", min_value=100, max_value=250, value=170)
weight = st.sidebar.slider("Weight (in kg)", min_value=30, max_value=200, value=70)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
activity_time = st.sidebar.slider("Activity Time (min)", min_value=1, max_value=180, value=30)
body_temp = st.sidebar.slider("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=36.5)
heart_rate = st.sidebar.slider("Heart Rate (bpm)", min_value=40, max_value=200, value=70)
activity_type = st.sidebar.selectbox("Activity Type", ["Gym", "Cycling", "Running", "Walking", "Swimming", "Yoga", "Jump Rope"])

# BMI and Fitness Level
bmi = calculate_bmi(weight, height)
fitness_level = get_fitness_level(bmi)

# Model Training
if 'model' not in st.session_state:
    st.session_state['model'] = train_model()

user_input = np.array([[age, height, weight, activity_time]])
predicted_fitness_level = st.session_state['model'].predict(user_input)[0]

calories_burned = calculate_calories(activity_type, weight, activity_time)
recommended_water = calculate_water_intake(weight, activity_time)

# Results Display
st.header("Your Results")
st.write(f"**BMI**: {bmi:.2f}")
st.write(f"**Fitness Level (Based on BMI):** {fitness_level}")
st.write(f"**Predicted Fitness Level (ML):** {predicted_fitness_level}")
st.write(f"**Calories Burned:** {calories_burned:.2f} kcal")
st.write(f"**Recommended Water Intake:** {recommended_water:.2f} ml")

# Stacked Bar Chart
st.subheader("📊 Calories Burned vs Water Intake")
fig, ax = plt.subplots()
categories = ['Calories Burned', 'Water Intake']
values = [calories_burned, recommended_water]

ax.bar(categories, values, color=['#ff9999', '#66b3ff'])
ax.set_ylabel('Amount')
ax.set_title('Calories vs Water Intake')

st.pyplot(fig)

# Area Chart
st.subheader("📈 Calories Burn Over Different Activities")
activity_calories = {
    "Gym": calculate_calories("Gym", weight, activity_time),
    "Cycling": calculate_calories("Cycling", weight, activity_time),
    "Running": calculate_calories("Running", weight, activity_time),
    "Walking": calculate_calories("Walking", weight, activity_time),
    "Swimming": calculate_calories("Swimming", weight, activity_time),
    "Yoga": calculate_calories("Yoga", weight, activity_time),
    "Jump Rope": calculate_calories("Jump Rope", weight, activity_time)
}

fig, ax = plt.subplots()
ax.fill_between(activity_calories.keys(), activity_calories.values(), color="#66b3ff", alpha=0.5)
ax.set_title("Calories Burn Over Different Activities")
ax.set_ylabel("Calories")
ax.set_xlabel("Activity Type")

st.pyplot(fig)

# Fitness Tip
st.subheader("💡 Fitness Tip")
tips = {
    "Underweight": "Consider increasing calorie intake with nutrient-dense foods.",
    "Normal weight": "Maintain a balanced diet and regular exercise.",
    "Overweight": "Incorporate cardio and strength training.",
    "Obese": "Seek guidance from a healthcare provider."
}
st.write(tips[fitness_level])

# Workout Plan
st.subheader("🏃‍♀️ Example Workout Plan")
st.write("Activity: Running")
st.write("Duration: 30 minutes")
st.write("Calories Burned: 300 kcal")

# Meal Plan
st.subheader("🍽️ Example Meal Plan")
if fitness_level == "Underweight":
    st.write("**Breakfast**: High-protein smoothie with bananas, oats, and almond butter.")
    st.write("**Lunch**: Grilled chicken with quinoa, avocado, and mixed vegetables.")
    st.write("**Dinner**: Salmon with sweet potatoes, spinach, and a side of rice.")
elif fitness_level == "Normal weight":
    st.write("**Breakfast**: Oats with fruits and nuts.")
    st.write("**Lunch**: Grilled chicken breast with quinoa and vegetables.")
    st.write("**Dinner**: Salmon with sweet potatoes and spinach.")
elif fitness_level == "Overweight":
    st.write("**Breakfast**: Greek yogurt with berries and chia seeds.")
    st.write("**Lunch**: Grilled chicken with a large salad of mixed greens and olive oil dressing.")
    st.write("**Dinner**: Grilled fish with steamed vegetables and a small serving of brown rice.")
else:  # Obese
    st.write("**Breakfast**: Scrambled eggs with spinach and tomatoes.")
    st.write("**Lunch**: Grilled turkey breast with steamed broccoli and quinoa.")
    st.write("**Dinner**: Grilled salmon with roasted asparagus and cauliflower rice.")

# Footer
st.write("**Stay healthy! 💪**")
