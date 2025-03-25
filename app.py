import streamlit as st
import openai
import os

# Set your OpenAI key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Grade 10 Math Placement")

# Question 1
st.header("Question 1: Solve for x")
st.latex(r"3x - 7 = 11")

if st.button("Need a refresher?"):
    with st.spinner("AI is preparing an explanation..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": "Explain how to solve the equation 3x - 7 = 11 step-by-step for a Grade 10 student."
            }]
        )
        st.success(response.choices[0].message.content)

user_answer = st.text_input("Your answer:")

if st.button("Submit answer"):
    if user_answer.strip() == "6":
        st.success("✅ Correct! Great job.")
    else:
        st.error("❌ Not quite. The correct answer is 6.")
        if st.button("Try a similar question"):
            st.info("Try solving: 4x - 5 = 11")

