import streamlit as st 

def start_game():
    return 1, 100

st.title("Computer Guess Number Game")
st.subheader("Think of  a number between 1 and 100 and the computer will try to guess it.")


def game():
    if "low" not in st.session_state:
        st.session_state.low,st.session_state.high = start_game()
        st.session_state.guess = (st.session_state.low +st.session_state.high)
        st.session_state.guess = 0


    st.write(f"Computer's guess: {st.session_state.guess}")
    feedback = st.radio("Is the guess too high, too low, or correct?", ["Too low", "Too high", "Correct"])


    if st.button("Submit Feedback"):


        if feedback == "Too low":
            st.session_state.low = st.session_state.guess +1
        elif feedback == "Too high":
            st.session_state.high = st.session_state.guess -1
        elif feedback == "Correct":
            st.write("Yay! The computer guessed the correct number.")
            st.write("Let's play again!")
            st.session_state.low, st.session_state.high = start_game()

        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

    if st.session_state.low > st.session_state.high:
        st.write("It seems there wa a mistake. let's restart")
        st.session_state.clear()

game()


if st.button("Restart Game"):
    st.session_state.clear()
    st.experimental_rerun()