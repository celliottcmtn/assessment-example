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
    ### 📘 Refresher: Solving Linear Equations

    A linear equation like `3x + 4 = 13` can be solved in two simple steps:

    **Step 1:** Subtract 4 from both sides  
    `3x + 4 - 4 = 13 - 4` → `3x = 9`

    **Step 2:** Divide both sides by 3  
    `3x / 3 = 9 / 3` → `x = 3`

    🧠 The goal is to isolate `x` by undoing the operations in reverse order.

    📺 [Watch on Khan Academy](https://www.khanacademy.org/math/algebra/solving-linear-equations)
    """)
    
answer1 = st.text_input("Your answer for x:", key="q1")
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q1_ai_toggle"):
    q1_ai_input = st.text_area("What would you like to ask about Question 1?", key="q1_ai_text")
    if st.button("Ask AI about Question 1"):
        if q1_ai_input.strip():
            with st.spinner("Asking AI..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": f"Help a Grade 10 student who says: {q1_ai_input}"
                    }]
                )
                st.markdown(f"**AI Response:**

{response.choices[0].message.content}")
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
    ### 📘 Refresher: Factoring Quadratic Expressions

    A quadratic trinomial looks like `x² + 5x + 6`. Here's how to factor it:

    **Step 1:** Find two numbers that multiply to the last number (6) and add to the middle number (5).  
    → `2 × 3 = 6` and `2 + 3 = 5`

    **Step 2:** Write the factored form using those numbers:  
    → `(x + 2)(x + 3)`

    ✅ Double-check by expanding to make sure it gives the original trinomial.

    📺 [Watch on Khan Academy](https://www.khanacademy.org/math/algebra/polynomial-factorization/factoring-quadratics-intro/v/factoring-quadratics-intro)
    """)
    st.image("https://cdn.kastatic.org/ka-perseus-images/5ceff8a3e7416c1c798193baad3d24988a4f15f9.png", caption="Factoring x² + 5x + 6 visually")

answer2 = st.text_input("Your factored expression:", key="q2")
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q2_ai_toggle"):
    q2_ai_input = st.text_area("What would you like to ask about Question 2?", key="q2_ai_text")
    if st.button("Ask AI about Question 2"):
        if q2_ai_input.strip():
            with st.spinner("Asking AI..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": f"Help a Grade 10 student who says: {q2_ai_input}"
                    }]
                )
                st.markdown(f"**AI Response:**

{response.choices[0].message.content}")
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
    ### 📘 Refresher: Using Sine to Find Angles

    If you know the sine of an angle, like `sin(A) = 0.5`, you can find the angle using your calculator:

    **Step 1:** Press the `sin⁻¹` (also called `arcsin`) button  
    **Step 2:** Enter the value → `sin⁻¹(0.5)`  
    **Result:** `A = 30°`

    🧠 This is often used in right triangles when you know the ratio of the opposite side to the hypotenuse.

    📺 [Watch on Khan Academy](https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-trig-ratios/v/using-trig-ratios-to-solve-right-triangles)
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Triangle_with_notations.svg/640px-Triangle_with_notations.svg.png", caption="Trig ratios in a right triangle")

answer3 = st.text_input("Your answer for angle A (in degrees):", key="q3")
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q3_ai_toggle"):
    q3_ai_input = st.text_area("What would you like to ask about Question 3?", key="q3_ai_text")
    if st.button("Ask AI about Question 3"):
        if q3_ai_input.strip():
            with st.spinner("Asking AI..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": f"Help a Grade 10 student who says: {q3_ai_input}"
                    }]
                )
                st.markdown(f"**AI Response:**

{response.choices[0].message.content}")
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


if st.button("📊 Get My Placement Recommendation"):
    score = 0
    try:
        if abs(float(st.session_state.get("q1", "0")) - 3) < 0.01:
            score += 1
    except:
        pass
    try:
        simplified = st.session_state.get("q2", "").replace(" ", "")
        if any(simplified == ans.replace(" ", "") for ans in correct_factored):
            score += 1
    except:
        pass
    try:
        user_val = float(st.session_state.get("q3", "0"))
        if abs(user_val - angle_deg) <= 1:
            score += 1
    except:
        pass

    st.subheader("📘 Your Placement Recommendation:")
    if score == 3:
        st.success("You're ready for Grade 11 math or higher! Great work.")
    elif score == 2:
        st.info("You’re close! A little review of core Grade 10 topics is recommended.")
    elif score == 1:
        st.warning("Consider reviewing foundational Grade 10 topics before moving forward.")
    else:
        st.error("We recommend placement in a fundamentals review course (Grade 7–9 topics).")
