if st.button("✅ Submit Answer 2"):
    simplified = answer2.replace(" ", "")
    if any(simplified == ans.replace(" ", "") for ans in correct_factored):
        st.success("✅ Correct! Well done.")
        st.session_state.q2_completed = True
        if "current_score" in st.session_state:
            if not st.session_state.get("q2_already_scored", False):
                st.session_state.current_score += 1
                st.session_state.q2_already_scored = True
        st.balloons()
    else:
        st.error(f"❌ Not quite. One correct answer is (x + {r1})(x + {r2}).")
        
        # Provide detailed feedback for incorrect answers
        with st.expander("See Step-by-Step Solution"):
            st.markdown(f"""
            ### Solution Walkthrough:
            
            **Step 1:** For the trinomial `x² + {trinomial_b}x + {trinomial_c}`, find two numbers that:
            - Multiply to give {trinomial_c}
            - Add to give {trinomial_b}
            
            **Step 2:** The numbers {r1} and {r2} work because:
            - {r1} × {r2} = {r1 * r2}
            - {r1} + {r2} = {r1 + r2}
            
            **Step 3:** Write the factored form:
            - (x + {r1})(x + {r2})
            
            **Check:** Multiply it out to verify:
            - First term: x × x = x²
            - Middle terms: x × {r2} + {r1} × x = {r2}x + {r1}x = {r1 + r2}x
            - Last term: {r1} × {r2} = {r1 * r2}
            
            So (x + {r1})(x + {r2}) = x² + {trinomial_b}x + {trinomial_c} ✓
            """)
            
            st.info("Try again! You can edit your answer above and resubmit.")st.markdown("---")

# Add some final feedback and navigation section
st.header("Assessment Summary")

# Create tabs for different sections of the summary
summary_tab, tips_tab, next_steps_tab = st.tabs(["Summary", "Study Tips", "Next Steps"])

with summary_tab:
    completed_count = sum([st.session_state.get("q1_completed", False), 
                          st.session_state.get("q2_completed", False), 
                          st.session_state.get("q3_completed", False)])
    
    if completed_count == 0:
        st.info("You haven't completed any questions yet. Try answering the questions above!")
    else:
        st.success(f"You've completed {completed_count} out of 3 questions!")
        
        # Show progress on specific topics
        st.subheader("Topic Mastery")
        topic_cols = st.columns(3)
        
        with topic_cols[0]:
            if st.session_state.get("q1_completed", False):
                st.markdown("📈 **Linear Equations**: Mastered ✓")
            else:
                st.markdown("📉 **Linear Equations**: Not yet mastered")
                
        with topic_cols[1]:
            if st.session_state.get("q2_completed", False):
                st.markdown("📈 **Factoring**: Mastered ✓") 
            else:
                st.markdown("📉 **Factoring**: Not yet mastered")
                
        with topic_cols[2]:
            if st.session_state.get("q3_completed", False):
                st.markdown("📈 **Trigonometry**: Mastered ✓")
            else:
                st.markdown("📉 **Trigonometry**: Not yet mastered")

with tips_tab:
    st.markdown("""
    ### 📚 Study Tips for Grade 10 Math
    
    1. **Practice Regularly**: Math skills improve with consistent practice
    2. **Use Visual Aids**: Draw diagrams to help understand problems
    3. **Learn Step-by-Step**: Break down complex problems into smaller steps
    4. **Check Your Work**: Always verify your answers
    5. **Study Groups**: Work with classmates to discuss challenging topics
    6. **Online Resources**: Use Khan Academy and other free resources
    7. **Ask for Help**: Don't hesitate to ask your teacher when you're stuck
    """)
    
with next_steps_tab:
    st.markdown("""
    ### 🚀 Next Steps
    
    Based on your performance in this assessment:
    
    1. **Review incorrect answers** using the step-by-step solutions
    2. **Practice similar problems** to strengthen your understanding
    3. **Use the AI tutor** to get personalized help on challenging concepts
    4. **Take the assessment again** after reviewing to see your improvement
    """)
    
    if st.button("📊 Get My Placement Recommendation", key="final_rec"):
        score = st.session_state.current_score
        st.subheader("📘 Your Placement Recommendation:")
        if score == 3:
            st.success("You're ready for Grade 11 math or higher! Great work.")
            st.balloons()
        elif score == 2:
            # Track which question was incorrect
            missed_topics = []
            try:
                if not (abs(float(st.session_state.get("q1", "0")) - 3) < 0.01):
                    missed_topics.append("Linear Equations")
            except:
                missed_topics.append("Linear Equations")
                
            try:
                simplified = st.session_state.get("q2", "").replace(" ", "")
                if not any(simplified == ans.replace(" ", "") for ans in correct_factored):
                    missed_topics.append("Factoring Quadratics")
            except:
                missed_topics.append("Factoring Quadratics")# -------------------
# QUESTION 2: FACTORING
# -------------------
if "r1" not in st.session_state:
    st.session_state.r1, st.session_state.r2 = random.choice([(1, 2), (2, 3), (3, 4), (-2, -3), (-1, 4)])
r1, r2 = st.session_state.r1, st.session_state.r2
trinomial_b = r1 + r2
trinomial_c = r1 * r2

st.header("Question 2: Factoring Quadratic Equations")
st.markdown(f"**Factor the quadratic expression below:**")
st.latex(f"x^2 + {trinomial_b}x + {trinomial_c}")

refresher_col2, practice_col2 = st.columns([1, 1])
with refresher_col2:
    if st.button("🔄 Need a refresher for Question 2", key="refresh_q2"):
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
        # Using a placeholder image instead of external URL for better compatibility with Streamlit
        st.markdown("![Factoring quadratics](https://cdn.kastatic.org/ka-perseus-images/5ceff8a3e7416c1c798193baad3d24988a4f15f9.png)")

with practice_col2:
    if st.button("🎮 Practice Similar Problem", key="practice_q2"):
        # Generate a simple practice problem
        practice_r1, practice_r2 = random.choice([(1, 3), (2, 4), (2, 5), (-1, -3), (-2, 5)])
        practice_b = practice_r1 + practice_r2
        practice_c = practice_r1 * practice_r2
        
        st.markdown(f"**Practice Problem:** Factor x² + {practice_b}x + {practice_c}")
        
        with st.expander("See Solution"):
            st.markdown(f"""
            **Step 1:** Find two numbers that:
            - Multiply to give {practice_c}
            - Add to give {practice_b}
            
            The numbers {practice_r1} and {practice_r2} work because:
            - {practice_r1} × {practice_r2} = {practice_c}
            - {practice_r1} + {practice_r2} = {practice_b}
            
            **Step 2:** The factored form is (x + {practice_r1})(x + {practice_r2})
            """)

answer2 = st.text_input("Your factored expression:", key="q2")

# Improved AI tutor section for Question 2
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q2_ai_toggle"):
    st.info("You can ask questions like 'How do I factor this?' or 'What numbers multiply to give the constant term?'")
    q2_ai_input = st.text_area("What would you like to ask about Question 2?", key="q2_ai_text")
    
    if st.button("Ask AI about Question 2"):
        if q2_ai_input.strip():
            with st.spinner("Asking AI tutor for help..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful math tutor for a Grade 10 student. Provide clear, step-by-step guidance without giving away the complete answer. Use encouraging language and scaffold your explanation so the student understands the process. Keep explanations under 150 words, use simple language, and focus on building understanding rather than just the solution."
                        },
                        {
                            "role": "user",
                            "content": f"I'm factoring this quadratic expression: x^2 + {trinomial_b}x + {trinomial_c}. {q2_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q2_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q2_ai_response)
import openai
import random
import math

# Load the OpenAI API key from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("📘 Grade 10 Math Placement Assessment")
st.markdown("Select the best answer or enter your solution. Click 'Need a refresher?' for help before answering.")

# Add progress tracking
# Display progress tracking in sidebar
st.sidebar.header("Your Progress")
col1, col2, col3 = st.sidebar.columns(3)

# Track question completion in session state
if "q1_completed" not in st.session_state:
    st.session_state.q1_completed = False
if "q2_completed" not in st.session_state:
    st.session_state.q2_completed = False
if "q3_completed" not in st.session_state:
    st.session_state.q3_completed = False

# Display progress indicators
with col1:
    if st.session_state.q1_completed:
        st.markdown("✅ Q1")
    else:
        st.markdown("⬜ Q1")
        
with col2:
    if st.session_state.q2_completed:
        st.markdown("✅ Q2")
    else:
        st.markdown("⬜ Q2")
        
with col3:
    if st.session_state.q3_completed:
        st.markdown("✅ Q3")
    else:
        st.markdown("⬜ Q3")

# Display score tracking in the sidebar
st.sidebar.header("Your Score")
if "current_score" not in st.session_state:
    st.session_state.current_score = 0
    
score_display = st.sidebar.progress(float(st.session_state.current_score) / 3)
st.sidebar.markdown(f"**Current Score:** {st.session_state.current_score}/3")

st.sidebar.markdown("---")
st.sidebar.markdown("### Need Help?")
st.sidebar.markdown("""
- Click the 'Need a refresher?' button for a quick lesson
- Use the AI tutor for personalized help
- Step-by-step solutions appear after submitting
""")

# Add reset assessment button
if st.sidebar.button("🔄 Reset Assessment"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
    else:
        st.markdown("⬜ Q2")
        
with col3:
    if st.session_state.q3_completed:
        st.markdown("✅ Q3")
    else:
        st.markdown("⬜ Q3")

st.sidebar.markdown("---")
st.sidebar.markdown("### Need Help?")
st.sidebar.markdown("""
- Click the 'Need a refresher?' button for a quick lesson
- Use the AI tutor for personalized help
- Step-by-step solutions appear after submitting
""")

# Track score in session state
if "current_score" not in st.session_state:
    st.session_state.current_score = 0

# -------------------
# QUESTION 1: LINEAR EQUATION
# -------------------
# Initialize random values in session state to keep them consistent across reruns
if "coeff" not in st.session_state:
    st.session_state.coeff = random.randint(2, 5)
    st.session_state.const = random.randint(1, 10)
    st.session_state.rhs = st.session_state.coeff * 3 + st.session_state.const

st.header("Question 1: Solving Linear Equations")
st.markdown(f"**Solve for x in the equation below:**")
st.latex(f"{st.session_state.coeff}x + {st.session_state.const} = {st.session_state.rhs}")

refresher_col1, practice_col1 = st.columns([1, 1])
with refresher_col1:
    if st.button("🔄 Need a refresher for Question 1", key="refresh_q1"):
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

with practice_col1:
    if st.button("🎮 Practice Similar Problem", key="practice_q1"):
        practice_coeff = random.randint(2, 5)
        practice_const = random.randint(1, 10)
        solution = random.randint(2, 5)
        practice_rhs = practice_coeff * solution + practice_const
        
        st.markdown(f"**Practice Problem:** Solve for x in {practice_coeff}x + {practice_const} = {practice_rhs}")
        
        with st.expander("See Solution"):
            st.markdown(f"""
            **Step 1:** Subtract {practice_const} from both sides  
            `{practice_coeff}x + {practice_const} - {practice_const} = {practice_rhs} - {practice_const}`  
            `{practice_coeff}x = {practice_rhs - practice_const}`
            
            **Step 2:** Divide both sides by {practice_coeff}  
            `{practice_coeff}x ÷ {practice_coeff} = {practice_rhs - practice_const} ÷ {practice_coeff}`  
            `x = {solution}`
            """)
    
answer1 = st.text_input("Your answer for x:", key="q1")

# Improved AI tutor section for Question 1
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q1_ai_toggle"):
    st.info("You can ask questions like 'How do I isolate x?' or 'What's the first step to solve this?'")
    q1_ai_input = st.text_area("What would you like to ask about Question 1?", key="q1_ai_text")
    
    if st.button("Ask AI about Question 1"):
        if q1_ai_input.strip():
            with st.spinner("Asking AI tutor for help..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful math tutor for a Grade 10 student. Provide clear, step-by-step guidance without giving away the complete answer. Use encouraging language and scaffold your explanation so the student understands the process. Keep explanations under 150 words, use simple language, and focus on building understanding rather than just the solution."
                        },
                        {
                            "role": "user",
                            "content": f"I'm solving this linear equation: {st.session_state.coeff}x + {st.session_state.const} = {st.session_state.rhs}. {q1_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q1_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q1_ai_response)

if st.button("✅ Submit Answer 1"):
    try:
        if abs(float(answer1) - 3) < 0.01:
            st.success("Correct! 🎉 Great job solving for x.")
            st.session_state.q1_completed = True
            if "current_score" in st.session_state:
                if not st.session_state.get("q1_already_scored", False):
                    st.session_state.current_score += 1
                    st.session_state.q1_already_scored = True
            st.balloons()
        else:
            st.error(f"Oops! That's not quite right. The correct answer is 3.")
            
            # Provide detailed feedback for incorrect answers
            with st.expander("See Step-by-Step Solution"):
                st.markdown(f"""
                ### Solution Walkthrough:
                
                **Step 1:** Subtract {st.session_state.const} from both sides  
                `{st.session_state.coeff}x + {st.session_state.const} - {st.session_state.const} = {st.session_state.rhs} - {st.session_state.const}`  
                `{st.session_state.coeff}x = {st.session_state.rhs - st.session_state.const}`
                
                **Step 2:** Divide both sides by {st.session_state.coeff}  
                `{st.session_state.coeff}x ÷ {st.session_state.coeff} = {st.session_state.rhs - st.session_state.const} ÷ {st.session_state.coeff}`  
                `x = 3`
                
                **Check:** Substitute x = 3 back into the original equation  
                `{st.session_state.coeff} × 3 + {st.session_state.const} = {st.session_state.coeff * 3 + st.session_state.const}`  
                `{st.session_state.coeff * 3 + st.session_state.const} = {st.session_state.rhs}` ✓
                """)
                
                st.info("Try again! You can edit your answer above and resubmit.")
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
    # Using a placeholder image instead of external URL for better compatibility with Streamlit
    st.markdown("![Factoring quadratics](https://cdn.kastatic.org/ka-perseus-images/5ceff8a3e7416c1c798193baad3d24988a4f15f9.png)")

answer2 = st.text_input("Your factored expression:", key="q2")

# Improved AI tutor section for Question 2
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q2_ai_toggle"):
    st.info("You can ask questions like 'How do I factor this?' or 'What numbers multiply to give the constant term?'")
    q2_ai_input = st.text_area("What would you like to ask about Question 2?", key="q2_ai_text")
    
    if st.button("Ask AI about Question 2"):
        if q2_ai_input.strip():
            with st.spinner("Asking AI tutor for help..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful math tutor for a Grade 10 student. Provide clear, step-by-step guidance without giving away the complete answer. Use encouraging language and scaffold your explanation so the student understands the process. Keep explanations under 150 words, use simple language, and focus on building understanding rather than just the solution."
                        },
                        {
                            "role": "user",
                            "content": f"I'm factoring this quadratic expression: x^2 + {trinomial_b}x + {trinomial_c}. {q2_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q2_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q2_ai_response)

correct_factored = [f"(x+{r1})(x+{r2})", f"(x+{r2})(x+{r1})"]


# -------------------
# QUESTION 3: TRIGONOMETRY
# -------------------
if "trig_value" not in st.session_state:
    st.session_state.trig_value = round(random.uniform(0.3, 0.9), 2)
    st.session_state.angle_deg = round(math.degrees(math.asin(st.session_state.trig_value)), 2)

st.header("Question 3: Intro to Trigonometry")
st.markdown(f"**A right triangle has an angle A such that sin(A) = {st.session_state.trig_value}. Use your calculator to find angle A in degrees.**")

refresher_col3, practice_col3 = st.columns([1, 1])
with refresher_col3:
    if st.button("🔄 Need a refresher for Question 3", key="refresh_q3"):
        st.markdown("""
        ### 📘 Refresher: Using Sine to Find Angles

        If you know the sine of an angle, like `sin(A) = 0.5`, you can find the angle using your calculator:

        **Step 1:** Press the `sin⁻¹` (also called `arcsin`) button  
        **Step 2:** Enter the value → `sin⁻¹(0.5)`  
        **Result:** `A = 30°`

        🧠 This is often used in right triangles when you know the ratio of the opposite side to the hypotenuse.

        📺 [Watch on Khan Academy](https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-trig-ratios/v/using-trig-ratios-to-solve-right-triangles)
        """)
        # Using a placeholder image instead of external URL for better compatibility with Streamlit
        st.markdown("![Trig ratios](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Triangle_with_notations.svg/640px-Triangle_with_notations.svg.png)")

with practice_col3:
    if st.button("🎮 Practice Similar Problem", key="practice_q3"):
        practice_trig_value = round(random.uniform(0.4, 0.8), 2)
        practice_angle = round(math.degrees(math.asin(practice_trig_value)), 2)
        
        st.markdown(f"**Practice Problem:** Find angle B in degrees where sin(B) = {practice_trig_value}")
        
        with st.expander("See Solution"):
            st.markdown(f"""
            To find angle B when sin(B) = {practice_trig_value}:
            
            **Step 1:** Use the inverse sine function: B = sin⁻¹({practice_trig_value})
            
            **Step 2:** Calculate using calculator: B = {practice_angle}°
            
            On most scientific calculators, press the `sin⁻¹` button followed by {practice_trig_value}
            """)

answer3 = st.text_input("Your answer for angle A (in degrees):", key="q3")

# Improved AI tutor section for Question 3
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q3_ai_toggle"):
    st.info("You can ask questions like 'How do I find an angle from its sine?' or 'What buttons do I press on my calculator?'")
    q3_ai_input = st.text_area("What would you like to ask about Question 3?", key="q3_ai_text")
    
    if st.button("Ask AI about Question 3"):
        if q3_ai_input.strip():
            with st.spinner("Asking AI tutor for help..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful math tutor for a Grade 10 student. Provide clear, step-by-step guidance without giving away the complete answer. Use encouraging language and scaffold your explanation so the student understands the process. Keep explanations under 150 words, use simple language, and focus on building understanding rather than just the solution."
                        },
                        {
                            "role": "user",
                            "content": f"I'm trying to find the angle A in degrees when sin(A) = {st.session_state.trig_value}. {q3_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q3_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q3_ai_response)

if st.button("✅ Submit Answer 3"):
    try:
        user_val = float(answer3)
        if abs(user_val - st.session_state.angle_deg) <= 1:
            st.success(f"✅ Correct! sin⁻¹({st.session_state.trig_value}) ≈ {st.session_state.angle_deg}°")
            st.session_state.q3_completed = True
            if "current_score" in st.session_state:
                if not st.session_state.get("q3_already_scored", False):
                    st.session_state.current_score += 1
                    st.session_state.q3_already_scored = True
            st.balloons()
        else:
            st.error(f"❌ That's not quite right. The correct answer is approximately {st.session_state.angle_deg}°.")
            
            # Provide detailed feedback for incorrect answers
            with st.expander("See Step-by-Step Solution"):
                st.markdown(f"""
                ### Solution Walkthrough:
                
                **Step 1:** We know that sin(A) = {st.session_state.trig_value}
                
                **Step 2:** To find angle A, use the inverse sine function (sin⁻¹ or arcsin):  
                A = sin⁻¹({st.session_state.trig_value})
                
                **Step 3:** Calculate using a calculator:  
                A = {st.session_state.angle_deg}°
                
                **Verification:** If sin(A) = {st.session_state.trig_value}, then A = sin⁻¹({st.session_state.trig_value}) = {st.session_state.angle_deg}°
                
                > 📌 **Tip:** On most scientific calculators, find angle A by pressing the `sin⁻¹` button (sometimes labeled as `arcsin` or `asin`), then entering {st.session_state.trig_value}.
                """)
                
                st.info("Try again! You can edit your answer above and resubmit.")
    except ValueError:
        st.error("Please enter a numeric value.")

st.markdown("---")

# Calculate score and display recommendation
if st.button("📊 Get My Placement Recommendation", key="main_rec_btn"):
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
        if abs(user_val - st.session_state.angle_deg) <= 1:
            score += 1
    except:
        pass

    # Update session state score for consistency
    st.session_state.current_score = score

    st.subheader("📘 Your Placement Recommendation:")
    if score == 3:
        st.success("You're ready for Grade 11 math or higher! Great work.")
        st.balloons()
    elif score == 2:
        # Track which question was incorrect
        missed_topics = []
        try:
            if not (abs(float(st.session_state.get("q1", "0")) - 3) < 0.01):
                missed_topics.append("Linear Equations")
        except:
            missed_topics.append("Linear Equations")
            
        try:
            simplified = st.session_state.get("q2", "").replace(" ", "")
            if not any(simplified == ans.replace(" ", "") for ans in correct_factored):
                missed_topics.append("Factoring Quadratics")
        except:
            missed_topics.append("Factoring Quadratics")
            
        try:
            user_val = float(st.session_state.get("q3", "0"))
            if not (abs(user_val - st.session_state.angle_deg) <= 1):
                missed_topics.append("Trigonometry")
        except:
            missed_topics.append("Trigonometry")
            
        topic_to_review = ", ".join(missed_topics)
        st.info(f"You can proceed to Grade 11 math, but should first review: {topic_to_review}. Your understanding of other topics is strong!")
        
        # Provide specific resources for review
        with st.expander("Resources for Review"):
            for topic in missed_topics:
                if topic == "Linear Equations":
                    st.markdown("""
                    ### Linear Equations Resources
                    - [Khan Academy: Solving Linear Equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities)
                    - Practice with isolating variables and solving step-by-step
                    """)
                elif topic == "Factoring Quadratics":
                    st.markdown("""
                    ### Factoring Quadratics Resources
                    - [Khan Academy: Factoring Quadratics](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring)
                    - Try writing out all pairs of factors for the constant term
                    """)
                elif topic == "Trigonometry":
                    st.markdown("""
                    ### Trigonometry Resources
                    - [Khan Academy: Basic Trigonometry](https://www.khanacademy.org/math/trigonometry/trigonometry-right-triangles)
                    - Practice using your calculator's inverse trigonometric functions
                    """)
    elif score == 1:
        st.warning("Consider reviewing foundational Grade 10 topics before moving forward.")
        
        # Show which question was correct
        correct_question = None
        try:
            if abs(float(st.session_state.get("q1", "0")) - 3) < 0.01:
                correct_question = "Linear Equations"
        except:
            pass
            
        try:
            simplified = st.session_state.get("q2", "").replace(" ", "")
            if any(simplified == ans.replace(" ", "") for ans in correct_factored):
                correct_question = "Factoring Quadratics"
        except:
            pass
            
        try:
            user_val = float(st.session_state.get("q3", "0"))
            if abs(user_val - st.session_state.angle_deg) <= 1:
                correct_question = "Trigonometry"
        except:
            pass
            
        if correct_question:
            st.markdown(f"You demonstrated understanding of **{correct_question}**. Focus on strengthening the other areas.")
        
    else:
        st.error("We recommend placement in a fundamentals review course (Grade 7–9 topics).")
