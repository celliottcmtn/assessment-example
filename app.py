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
    st.markdown("""
    **How to Solve a Linear Equation (like ax + b = c):**

    Example: `3x + 4 = 13`

    **Step 1:** Subtract 4 from both sides → `3x = 9`  
    **Step 2:** Divide both sides by 3 → `x = 3`

    🔍 You're trying to get `x` alone by undoing the operations in reverse order.
    """)
    st.image("https://cdn.kastatic.org/ka-perseus-images/cb9b0c6e574ac9f9cbd65a43d86d67c3db2f2d64.png", caption="Steps for solving linear equations")

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
if "r1" not in st.session_state:
    st.session_state.r1, st.session_state.r2 = random.choice([(1, 2), (2, 3), (3, 4), (-2, -3), (-1, 4)])
r1, r2 = st.session_state.r1, st.session_state.r2
trinomial_b = r1 + r2
trinomial_c = r1 * r2

st.header("Question 2: Factoring Quadratic Equations")
st.latex(f"x^2 + {trinomial_b}x + {trinomial_c}")

if st.button("🔄 Need a refresher for Question 2"):
    st.markdown("""
    **How to Factor a Quadratic (like x² + bx + c):**

    Example: `x² + 5x + 6`

    **Step 1:** Look for two numbers that multiply to 6 and add to 5.  
    **Answer:** 2 and 3 → because `2 × 3 = 6` and `2 + 3 = 5`

    **Step 2:** Write the factored form: `(x + 2)(x + 3)`

    ✅ Done! Always double-check by expanding to see if it matches the original.
    """)
    st.image("https://mathbitsnotebook.com/Algebra1/Factoring/FACimages/FactorGCF01.png", caption="Factoring trinomials diagram")

answer2 = st.text_input("Your factored expression:", key="q2")
correct_factored = [f"(x+{r1})(x+{r2})", f"(x+{r2})(x+{r1})"]

if st.button("✅ Submit Answer 2"):
    simplified = answer2.replace(" ", "")
    if any(simplified == ans.replace(" ", "") for ans in correct_factored):
        st.success("✅ Correct! Well done.")
    else:
        st.error(f"❌ Not quite. One correct answer is (x + {r1})(x + {r2}).")

# -------------------
# QUESTION 3: TRIGONOMETRY
# -------------------
value = round(random.uniform(0.3, 0.9), 2)
angle_deg = round(math.degrees(math.asin(value)), 2)

st.header("Question 3: Intro to Trigonometry")
st.markdown(f"A right triangle has an angle A such that sin(A) = {value}. Use your calculator to find angle A in degrees.")

if st.button("🔄 Need a refresher for Question 3"):
    st.markdown("""
    **How to Find an Angle from a Sine Value:**

    Example: `sin(A) = 0.5`

    **Step 1:** Use the `sin⁻¹` or `arcsin` button on your calculator.  
    **Step 2:** Input `0.5` and press equals → You should get `30°`

    🧠 This means angle A is 30 degrees.

    📏 Use this when you know a side ratio and want to find the angle.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Triangle_with_notations.svg/640px-Triangle_with_notations.svg.png", caption="Trig ratios in a right triangle")

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
