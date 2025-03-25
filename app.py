import streamlit as st
import openai

# Load the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📘 Grade 10 Math Placement Assessment")
st.markdown("Select the best answer or enter your solution. You can click 'Need a refresher?' for help before answering.")

# -------------------
# QUESTION 1
# -------------------
st.header("Question 1: Solving Linear Equations")
st.latex(r"3x - 7 = 11")

if st.button("🔄 Need a refresher for Question 1"):
    with st.spinner("AI is preparing a refresher lesson..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": "Explain how to solve 3x - 7 = 11 in a clear, step-by-step way for a high school student."
            }]
        )
        st.info(response.choices[0].message.content)

answer1 = st.text_input("Your answer for x:", key="q1")
if st.button("✅ Submit Answer 1"):
    if answer1.strip() == "6":
        st.success("Correct! 🎉 Great job solving for x.")
    else:
        st.error("Oops! That's not quite right. The correct answer is 6.")
        if st.button("🔁 Try a similar question", key="q1_retry"):
            st.write("Try this one: Solve 4x - 5 = 11")

# -------------------
# QUESTION 2
# -------------------
st.header("Question 2: Factoring Quadratic Equations")
st.markdown("Factor the following expression:")
st.latex(r"x^2 + 5x + 6")

if st.button("🔄 Need a refresher for Question 2"):
    with st.spinner("AI is preparing a refresher lesson..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": "How do you factor the quadratic x^2 + 5x + 6 step-by-step for a Grade 10 student?"
            }]
        )
        st.info(response.choices[0].message.content)

answer2 = st.text_input("Your factored expression:", key="q2")
if st.button("✅ Submit Answer 2"):
    valid_answers = ["(x+2)(x+3)", "(x + 2)(x + 3)", "(x+3)(x+2)", "(x + 3)(x + 2)"]
    if answer2.replace(" ", "") in [a.replace(" ", "") for a in valid_answers]:
        st.success("✅ Correct! Well done.")
    else:
        st.error("❌ Not quite. The correct answer is (x + 2)(x + 3).")
        if st.button("🔁 Try a similar question", key="q2_retry"):
            st.write("Try factoring: x^2 + 7x + 10")

# -------------------
# QUESTION 3
# -------------------
st.header("Question 3: Intro to Trigonometry")
st.markdown("A right triangle has an angle A such that sin(A) = 0.6. Use your calculator to find the measure of angle A in degrees.")

if st.button("🔄 Need a refresher for Question 3"):
    with st.spinner("AI is preparing a refresher lesson..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": "Explain how to find an angle when given sin(A) = 0.6 using a calculator, for a Grade 10 student."
            }]
        )
        st.info(response.choices[0].message.content)

answer3 = st.text_input("Your answer for angle A (in degrees):", key="q3")
if st.button("✅ Submit Answer 3"):
    try:
        user_val = float(answer3)
        if 36 <= user_val <= 38:
            st.success("✅ Correct! sin⁻¹(0.6) ≈ 36.87°")
        else:
            st.error("❌ That's not quite right. The correct answer is approximately 36.87°.")
            if st.button("🔁 Try a similar question", key="q3_retry"):
                st.write("Try this one: sin(B) = 0.8. Find angle B.")
    except ValueError:
        st.error("Please enter a numeric value.")

st.markdown("---")
st.markdown("✅ Once you've completed all three questions, you'll be given a recommendation for your placement level in math.")
