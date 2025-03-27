import streamlit as st 

def calculate_bmi(weight , height):
    return weight/(height**2)


# UI part

st.title("BMI calculator")

st.subheader("Enter your weight and height to calculate your bmi")
weight = st.number_input("Enter your weight in kg" ,)
height = st.number_input("Enter your height in meters")


if st.button("Calculate BMI"):

    if height>0 and weight > 0:
     bmi = calculate_bmi(weight , height)
     st.write(f"Your BMI is {bmi :.2f}")

    if bmi < 18.5:
       st.write("Category: Underweight")
       st.warning("You are underweight, It may be a good idea to consult with a doctor or a nutritionist")
    elif 18.5 <= bmi< 24.9 :
        st.write("Category: Normal weight")
        st.success("You are in the normal weight range for your height")
    elif 25 <= bmi <29.9:
       st.write("Category: Overweight")
       st.warning("You are overweight, consider consulting with a doctor or a nutritionist")
    else:
        st.write("Category: Obesity")
        st.error("You are obese, consider consulting with a doctor or a nutritionist")

