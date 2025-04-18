import streamlit as st
import random

# List of words for the game
word_list = ["python", "hangman", "streamlit", "developer", "machine", "algorithm"]

# Function to start a new game
def start_game():
    secret_word = random.choice(word_list)
    return secret_word, ['_'] * len(secret_word), 6  # secret_word, current progress, lives left

# Function to update the game after each guess
def update_game(secret_word, current_progress, lives_left, guessed_letter):
    if guessed_letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guessed_letter:
                current_progress[i] = guessed_letter
    else:
        lives_left -= 1  # Lose a life if the letter is not in the word
    return current_progress, lives_left

# UI Part
st.title("Hangman Game")
st.subheader("Guess the secret word")

# Initialize the game state if not already in session state
if 'secret_word' not in st.session_state:
    st.session_state.secret_word, st.session_state.current_progress, st.session_state.lives_left = start_game()

# Display current progress and lives left
st.write(f"Current word: {' '.join(st.session_state.current_progress)}")
st.write(f"Lives left: {st.session_state.lives_left}")

# Get user input for guessing a letter
guessed_letter = st.text_input("Enter a letter", max_chars=1).lower()

# When the guess button is pressed
if st.button("Guess"):
    if guessed_letter and len(guessed_letter) == 1:  # Ensure a valid letter is entered
        # Update the game state based on the guess
        st.session_state.current_progress, st.session_state.lives_left = update_game(
            st.session_state.secret_word, st.session_state.current_progress, st.session_state.lives_left, guessed_letter
        )
        
        # If the letter is incorrect, show a warning
        if guessed_letter not in st.session_state.secret_word:
            st.warning(f"Incorrect guess! You have {st.session_state.lives_left} lives remaining. Try again!")
        
        # Check if the game is won
        if '_' not in st.session_state.current_progress:
            st.write(f"Congratulations! You've guessed the word: {''.join(st.session_state.current_progress)}")
            st.session_state.secret_word, st.session_state.current_progress, st.session_state.lives_left = start_game()
        
        # Check if the game is lost
        elif st.session_state.lives_left == 0:
            st.write(f"Game over! The secret word was: {st.session_state.secret_word}")
            st.session_state.secret_word, st.session_state.current_progress, st.session_state.lives_left = start_game()

# Button to restart the game manually
if st.button("Restart Game"):
    st.session_state.clear()
    st.experimental_rerun()
