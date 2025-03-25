import streamlit as st
import zxcvbn

background_image = "./bg.img"
st.markdown(
    f"""
    <style>
    body {{
        background-image: url({background_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Function to evaluate password strength
def evaluate_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']  # score ranges from 0 (weak) to 4 (strong)
    feedback = result['feedback']['suggestions']
    return score, feedback

# Function to display password strength
def get_strength_color(score):
    if score == 0:
        return "red", "Weak 💔"
    elif score == 1:
        return "orange", "Weak 💔"
    elif score == 2:
        return "yellow", "Medium 💪"
    elif score == 3:
        return "lightgreen", "Strong 💪"
    else:
        return "green", "Very Strong 💥"

# Streamlit UI setup
st.title("Password Strength Meter 🔍")

# Get password input from the user
password = st.text_input("Enter your password:", type="password")

# Evaluate the password strength
if password:
    score, feedback = evaluate_password_strength(password)
    strength_color, strength_label = get_strength_color(score)
    
    # Display password strength bar and label
    st.markdown(f"<div style='background-color:{strength_color};height: 20px;width:{score * 25}%;'></div>", unsafe_allow_html=True)
    
    # Display password strength text and suggestions
    st.write(f"Strength: {strength_label}")
    
    if feedback:
        st.write("Suggestions to improve your password:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

# Instructions for a strong password
st.write("""
### Password Guidelines:
- At least 8 characters
- Should include uppercase letters, lowercase letters, numbers, and special characters
""")
