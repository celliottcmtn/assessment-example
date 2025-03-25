
import streamlit as st
import openai
import random
import math

# Load the OpenAI API key from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("📘 Grade 10 Math Placement Assessment")
st.markdown("Select the best answer or enter your solution. Click 'Need a refresher?' for help before answering.")

# -------------------
# QUESTION 1: LINEAR EQUATION
# -------------------
coeff = random.randint(2, 5)
const = random.randint(1, 10)
rhs = coeff * 3 + const

st.header("Question 1: Solving Linear Equations")
st.latex(f"{coeff}x + {const} = {rhs}")

if st.button("🔄 Need a refresher for Question 1"):
    st.info("To solve an equation like ax + b = c, subtract b from both sides, then divide by a.")

answer1 = st.text_input("Your answer for x:", key="q1")
if st.button("✅ Submit Answer 1"):
    try:
        if abs(float(answer1) - 3) < 0.01:
            st.success("Correct! 🎉 Great job solving for x.")
        else:
            st.error(f"Oops! That's not quite right. The correct answer is 3.")
    except ValueError:
        st.error("Please enter a numeric value.")

# -------------------
# QUESTION 2: FACTORING
# -------------------
a, b = random.choice([(1, 2), (1, 3), (1, 4)])
c, d = random.choice([(2, 3), (1, 6), (2, 5)])
m, n = a * c, b * d
middle = a * d + b * c

st.header("Question 2: Factoring Quadratic Equations")
st.latex(f"x^2 + {middle}x + {m * n}")

if st.button("🔄 Need a refresher for Question 2"):
    st.info("To factor x² + bx + c, find two numbers that multiply to c and add to b.")

answer2 = st.text_input("Your factored expression:", key="q2")
correct_factored = [f"(x+{a})(x+{b})", f"(x+{b})(x+{a})"]

if st.button("✅ Submit Answer 2"):
    simplified = answer2.replace(" ", "")
    if any(simplified == ans.replace(" ", "") for ans in correct_factored):
        st.success("✅ Correct! Well done.")
    else:
        st.error(f"❌ Not quite. One correct answer is (x + {a})(x + {b}).")

# -------------------
# QUESTION 3: TRIGONOMETRY
# -------------------
value = round(random.uniform(0.3, 0.9), 2)
angle_deg = round(math.degrees(math.asin(value)), 2)

st.header("Question 3: Intro to Trigonometry")
st.markdown(f"A right triangle has an angle A such that sin(A) = {value}. Use your calculator to find angle A in degrees.")

if st.button("🔄 Need a refresher for Question 3"):
    st.info("To find an angle when sin(A) = x, use the inverse sine button (sin⁻¹ or arcsin) on your calculator.")

answer3 = st.text_input("Your answer for angle A (in degrees):", key="q3")
if st.button("✅ Submit Answer 3"):
    try:
        user_val = float(answer3)
        if abs(user_val - angle_deg) <= 1:
            st.success(f"✅ Correct! sin⁻¹({value}) ≈ {angle_deg}°")
        else:
            st.error(f"❌ That's not quite right. The correct answer is approximately {angle_deg}°.")
    except ValueError:
        st.error("Please enter a numeric value.")

st.markdown("---")
st.markdown("✅ Once you've completed all three questions, you'll be given a recommendation for your placement level in math.")
