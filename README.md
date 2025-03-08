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
Step 1: Install Dependencies
Make sure you have a requirements.txt file in your project directory that contains all the necessary libraries (like Streamlit, pandas, scikit-learn, etc.).

Install the dependencies using the following command:
->pip install -r requirements.txt
This will install all the libraries listed in the requirements.txt file.

Step 2: Run the Streamlit App

Once the dependencies are installed, you can run the app by executing the following command:
->streamlit run app.py
This will start the Streamlit server, and you should see output like:

You can now view your Streamlit app in your browser.

  Network URL:  http://127.0.0.1:8501
  External URL: http://<your-machine-ip>:8501

Step 3: Access the App
Once the app is running, open your browser.
Go to http://localhost:8501.
You should now see the Personal Fitness Tracker app running locally on your machine.

Step 4: Interact with the App
You can now interact with the app by:

Entering your age, height, weight, activity time, etc.
The app will calculate your BMI, fitness level, calories burned, water intake, and provide recommendations and visualizations.
