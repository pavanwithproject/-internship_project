# Personal Fitness Tracker

## Overview

The **Personal Fitness Tracker** is a web application built with **Streamlit** that helps users track their fitness and health goals. This app calculates the user's **BMI**, predicts their **fitness level**, and provides insights on **calories burned** and **recommended water intake** based on their activities. It also leverages a simple **machine learning model** to predict the fitness level based on age, weight, height, and activity time.

### Key Features:
- **BMI Calculation**: The app calculates your Body Mass Index (BMI) based on your height and weight.
- **Fitness Level Prediction**: The app predicts your fitness level using a trained machine learning model.
- **Calories Burned Calculation**: The app estimates the number of calories burned during various activities like running, swimming, cycling, etc.
- **Water Intake Recommendation**: The app calculates the amount of water you should drink based on your weight and physical activity.
- **Real-time Visualizations**: Interactive graphs are displayed to show calories burned vs. water intake and calories burned during different activities.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Technologies Used](#technologies-used)
4. [Machine Learning Model](#machine-learning-model)
5. [Future Improvements](#future-improvements)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)

---
Installation
Prerequisites
To run this project locally, you need Python and pip installed. You also need to install the following dependencies:
->pip install streamlit numpy pandas scikit-learn matplotlib

 Running the App
1.Clone this repository to your local machine:
->git clone https://github.com/yourusername/personal-fitness-tracker.git

2.Navigate into the project folder:
->cd personal-fitness-tracker

3.Run the Streamlit app:
->streamlit run app.py

Open the app in your browser (Streamlit will provide a local link).

4. Interact with the App
You can now interact with the app by:
Entering your age, height, weight, activity time, etc.
The app will calculate your BMI, fitness level, calories burned, water intake, and provide recommendations and visualizations.
