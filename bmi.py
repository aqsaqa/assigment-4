import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1, max_value=300, step=1)
height = st.number_input("Enter your height (cm):", min_value=1, max_value=300, step=1)

if weight > 0 and height > 0:
    height_in_meters = height / 100 
    bmi = weight / (height_in_meters ** 2)

    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
