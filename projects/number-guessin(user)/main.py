import streamlit as st
import random
import time

# Function to start the game
def start_game():
    # Generate a random number between 50 to 100
    return random.randint(50, 100)

# UI part
st.title("🎯 Number Guessing Game") 
st.subheader("🤔 Try to guess the number between 50 to 100!")

# Function to initialize the game
def game():
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = start_game()
        st.session_state.attempts = 0

game()

# Input for user's guess
user_guess = st.number_input("🔢 Enter a number:", min_value=50, max_value=100, step=1)

if st.button("🚀 Submit Guess"):
    # Increase attempts counter
    st.session_state.attempts += 1

    # Check if the guess is correct
    if user_guess < st.session_state.secret_number:
        st.error(f"🔻 Your guess of {user_guess} is too low! Try a higher number.")
        st.warning(f"⚠️ You have {5 - st.session_state.attempts} attempts left.")
    elif user_guess > st.session_state.secret_number:
        st.error(f"🔼 Your guess of {user_guess} is too high! Try a lower number.")
        st.warning(f"⚠️ You have {5 - st.session_state.attempts} attempts left.")
    else:
        st.success(f"🎉 Congratulations! You've guessed the correct number {st.session_state.secret_number} in {st.session_state.attempts} attempts! 🎊")
        st.session_state.secret_number = start_game()  # Start a new game after winning
        st.session_state.attempts = 0

    # Check if attempts are exhausted
    if st.session_state.attempts >= 5 and user_guess != st.session_state.secret_number:
        st.error(f"💔 Sorry! You've exhausted the maximum number of attempts. The number was {st.session_state.secret_number}.")
        st.subheader("🔄 Restarting Game")
        time.sleep(3)  # Pause for 3 seconds before resetting
        
        st.session_state.clear()
        st.experimental_rerun()

# Button to restart the game
if st.button("🔄 Restart Game"):
    st.session_state.clear()
    st.experimental_rerun()
