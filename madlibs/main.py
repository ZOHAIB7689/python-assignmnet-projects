import streamlit as st 

st.title("Madlib's story game")
st.subheader("fill these blanks to generate your madlibs story")
story_template =  """
Once upon a time, in a land far, far away, a **[adjective]** **[noun]** named **[name]** embarked on a thrilling adventure to **[place]**. 
With a heart full of **[emotion]** and a spirit of **[adjective1]**, **[name]** set out to **[verb]** the unknown. 
As **[name]** wandered through the **[place]**, the **[adjective]** sun shone brightly, casting a warm glow over the entire journey.
"""

name = st.text_input("Enter a name: ")
adjective = st.text_input("Enter an adjective: ")
noun = st.text_input("Enter a noun: ")
place = st.text_input("Enter a place: ")
verb = st.text_input("Enter a verb: ")
adjective1 = st.text_input("Enter another adjective: ")
emotion = st.text_input("Enter an emotion: ")


if st.button("Generate Story"):
    story = story_template.replace("[name]", name)
    story = story.replace("[adjective]", adjective)
    story = story.replace("[noun]", noun)
    story = story.replace("[place]", place)
    story = story.replace("[verb]", verb)
    story = story.replace("[adjective1]", adjective1)
    story = story.replace("[emotion]", emotion)

    st.write("Here's your madlib story")
    st.write(story)