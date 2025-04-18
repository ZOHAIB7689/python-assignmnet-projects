import streamlit as st
import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a  tie"

    if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins"
    
# UI part

st.title("Rock Papper Scissors Game")
st.subheader("Select one option")


user_choice = st.radio("Select your choice", ["rock", "paper", "scissors"])

if st.button("Play"):
    compter_choice = random.choice(["rock", "paper", "scissors"])


    st.write(f"Computer choice: {compter_choice}")
    st.write(f"You Chose: {compter_choice}")

    result = determine_winner(user_choice, compter_choice)
    st.write(result)