# PART 1: IMPORTS AND SETUP
import openai
import random
import math
import streamlit as st

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

# Track attempts for each question
if "q1_attempts" not in st.session_state:
    st.session_state.q1_attempts = 0
if "q2_attempts" not in st.session_state:
    st.session_state.q2_attempts = 0
if "q3_attempts" not in st.session_state:
    st.session_state.q3_attempts = 0

# Add solution display flags
if "show_q1_solution" not in st.session_state:
    st.session_state.show_q1_solution = False
if "show_q2_solution" not in st.session_state:
    st.session_state.show_q2_solution = False
if "show_q3_solution" not in st.session_state:
    st.session_state.show_q3_solution = False

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
    st.rerun()
# PART 2: QUESTION 1 - LINEAR EQUATION
# Function to generate a new linear equation
def generate_linear_equation():
    coeff = random.randint(2, 8)
    solution = random.randint(-5, 10)  # Random solution value
    const = random.randint(-10, 15)
    rhs = coeff * solution + const
    return coeff, const, rhs, solution

# Initialize random values in session state or regenerate when needed
if "coeff" not in st.session_state or st.session_state.get("regenerate_q1", False):
    st.session_state.coeff, st.session_state.const, st.session_state.rhs, st.session_state.q1_solution = generate_linear_equation()
    st.session_state.regenerate_q1 = False
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

# Submit button for Question 1
if st.button("✅ Submit Answer 1"):
    try:
        st.session_state.q1_attempts += 1
        if abs(float(answer1) - st.session_state.q1_solution) < 0.01:
            st.success(f"Correct! Great job solving for x = {st.session_state.q1_solution}.")
            st.session_state.q1_completed = True
            if "current_score" in st.session_state:
                if not st.session_state.get("q1_already_scored", False):
                    st.session_state.current_score += 1
                    st.session_state.q1_already_scored = True
                    st.rerun()
        else:
            # Set flag to show solution instead of regenerating immediately
            st.session_state.show_q1_solution = True
            st.rerun()  # This rerun is just to refresh the page with the solution visible
    except ValueError:
        st.error("Please enter a numeric value.")

# After the submit button, check if we need to show a solution
if st.session_state.show_q1_solution:
    st.error(f"Oops! That's not quite right. The correct answer is {st.session_state.q1_solution}.")
    
    # Provide detailed feedback for incorrect answers
    with st.expander("See Step-by-Step Solution", expanded=True):
        st.markdown(f"""
        ### Solution Walkthrough:
        
        **Step 1:** Subtract {st.session_state.const} from both sides  
        `{st.session_state.coeff}x + {st.session_state.const} - {st.session_state.const} = {st.session_state.rhs} - {st.session_state.const}`  
        `{st.session_state.coeff}x = {st.session_state.rhs - st.session_state.const}`
        
        **Step 2:** Divide both sides by {st.session_state.coeff}  
        `{st.session_state.coeff}x ÷ {st.session_state.coeff} = {st.session_state.rhs - st.session_state.const} ÷ {st.session_state.coeff}`  
        `x = {st.session_state.q1_solution}`
        
        **Check:** Substitute x = {st.session_state.q1_solution} back into the original equation  
        `{st.session_state.coeff} × {st.session_state.q1_solution} + {st.session_state.const} = {st.session_state.coeff * st.session_state.q1_solution + st.session_state.const}`  
        `{st.session_state.coeff * st.session_state.q1_solution + st.session_state.const} = {st.session_state.rhs}` ✓
        """)
    
    # Add button for new question
    if st.button("Try a new question", key="new_q1"):
        st.session_state.regenerate_q1 = True
        st.session_state.show_q1_solution = False  # Reset the solution flag
        st.rerun()

st.markdown("---")
# PART 3: QUESTION 2 - FACTORING
# Function to generate a new factoring problem
def generate_factoring_problem():
    # Generate factors with more variety
    factor_options = [
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 3), (2, 5), (2, 7),
        (3, 4), (3, 5),
        (-1, 2), (-1, 3), (-1, 4), (-1, 5),
        (-2, 3), (-2, 5), (-3, 2), (-3, 4)
    ]
    r1, r2 = random.choice(factor_options)
    trinomial_b = r1 + r2
    trinomial_c = r1 * r2
    return r1, r2, trinomial_b, trinomial_c

# Initialize or regenerate factoring problem
if "r1" not in st.session_state or st.session_state.get("regenerate_q2", False):
    st.session_state.r1, st.session_state.r2, trinomial_b, trinomial_c = generate_factoring_problem()
    st.session_state.trinomial_b = trinomial_b
    st.session_state.trinomial_c = trinomial_c
    st.session_state.regenerate_q2 = False
else:
    trinomial_b = st.session_state.trinomial_b
    trinomial_c = st.session_state.trinomial_c

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

# Define correct factored answers for this problem
r1, r2 = st.session_state.r1, st.session_state.r2
correct_factored = [f"(x+{r1})(x+{r2})", f"(x+{r2})(x+{r1})", 
                   f"(x + {r1})(x + {r2})", f"(x + {r2})(x + {r1})",
                   f"(x{r1:+})(x{r2:+})", f"(x{r2:+})(x{r1:+})"]  # Format with + sign

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

# Submit button for Question 2
if st.button("✅ Submit Answer 2"):
    st.session_state.q2_attempts += 1
    simplified = answer2.replace(" ", "")
    if any(simplified == ans.replace(" ", "") for ans in correct_factored):
        st.success("✅ Correct! Well done.")
        st.session_state.q2_completed = True
        if "current_score" in st.session_state:
            if not st.session_state.get("q2_already_scored", False):
                st.session_state.current_score += 1
                st.session_state.q2_already_scored = True
                st.rerun()
    else:
        # Set flag to show solution instead of regenerating immediately
        st.session_state.show_q2_solution = True
        st.rerun()  # This rerun is just to refresh the page with the solution visible

# After the submit button, check if we need to show a solution
if st.session_state.show_q2_solution:
    st.error(f"❌ Not quite. One correct answer is (x + {r1})(x + {r2}).")
    
    # Provide detailed feedback for incorrect answers
    with st.expander("See Step-by-Step Solution", expanded=True):
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
    
    # Add button for new question
    if st.button("Try a new question", key="new_q2"):
        st.session_state.regenerate_q2 = True
        st.session_state.show_q2_solution = False  # Reset the solution flag
        st.rerun()

st.markdown("---")
.message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q3_ai_response)

# Submit button for Question 3
if st.button("✅ Submit Answer 3"):
    try:
        st.session_state.q3_attempts += 1
        # Convert answers to float and compare with a small tolerance for rounding errors
        if abs(float(answer3) - st.session_state.angle_deg) < 0.1:
            st.success(f"Correct! Great job finding the angle {st.session_state.angle_deg}°.")
            st.session_state.q3_completed = True
            if "current_score" in st.session_state:
                if not st.session_state.get("q3_already_scored", False):
                    st.session_state.current_score += 1
                    st.session_state.q3_already_scored = True
                    st.rerun()
        else:
            # Set flag to show solution instead of regenerating immediately
            st.session_state.show_q3_solution = True
            st.rerun()  # This rerun is just to refresh the page with the solution visible
    except ValueError:
        st.error("Please enter a numeric value for the angle.")

# After the submit button, check if we need to show a solution
if st.session_state.show_q3_solution:
    st.error(f"Oops! That's not quite right. The correct answer is {st.session_state.angle_deg}°.")
    
    # Provide detailed feedback for incorrect answers
    with st.expander("See Step-by-Step Solution", expanded=True):
        st.markdown(f"""
        ### Solution Walkthrough:
        
        **Step 1:** We know that {st.session_state.trig_function}(A) = {st.session_state.trig_value}
        
        **Step 2:** To find angle A, we need to use the inverse function {st.session_state.trig_function}⁻¹
        
        **Step 3:** A = {st.session_state.trig_function}⁻¹({st.session_state.trig_value})
        
        **Step 4:** Using a calculator with the {st.session_state.trig_function}⁻¹ button:
        - Enter {st.session_state.trig_value}
        - Press {st.session_state.trig_function}⁻¹
        - Result: A = {st.session_state.angle_deg}°
        """)
    
    # Add button for new question
    if st.button("Try a new question", key="new_q3"):
        st.session_state.regenerate_q3 = True
        st.session_state.show_q3_solution = False  # Reset the solution flag
        st.rerun()

st.markdown("---")
# PART 5: ASSESSMENT SUMMARY - ONLY SHOW WHEN QUESTION 3 IS COMPLETED
# Only show assessment summary if all questions are completed or at least question 3 is completed
if st.session_state.q3_completed:
    st.header("Assessment Summary")

    # Calculate the final score and progress information
    completed_count = sum([st.session_state.get("q1_completed", False), 
                          st.session_state.get("q2_completed", False), 
                          st.session_state.get("q3_completed", False)])
    score = st.session_state.current_score

    # Display overall assessment result first
    st.subheader("📊 Your Placement Recommendation:")
    if score == 3:
        st.success("You're ready for Grade 11 math or higher! Great work.")
    elif score == 2:
        # Track which question was incorrect
        missed_topics = []
        
        # Check which questions were missed
        if not st.session_state.get("q1_completed", False):
            missed_topics.append("Linear Equations")
        if not st.session_state.get("q2_completed", False):
            missed_topics.append("Factoring Quadratics")
        if not st.session_state.get("q3_completed", False):
            missed_topics.append("Trigonometry")
            
        topic_to_review = ", ".join(missed_topics)
        st.info(f"You can proceed to Grade 11 math, but should first review: {topic_to_review}. Your understanding of other topics is strong!")
    elif score == 1:
        st.warning("Consider reviewing foundational Grade 10 topics before moving forward.")
        
        # Show which question was correct
        correct_topic = None
        if st.session_state.get("q1_completed", False):
            correct_topic = "Linear Equations"
        elif st.session_state.get("q2_completed", False):
            correct_topic = "Factoring Quadratics"
        elif st.session_state.get("q3_completed", False):
            correct_topic = "Trigonometry"
            
        if correct_topic:
            st.markdown(f"You demonstrated understanding of **{correct_topic}**. Focus on strengthening the other areas.")
    else:
        st.error("We recommend placement in a fundamentals review course (Grade 7–9 topics).")

    # Show detailed assessment information
    st.markdown("### Assessment Details")

    # Show progress information
    if completed_count == 0:
        st.info("You haven't completed any questions yet. Try answering the questions above!")
    else:
        st.success(f"You've completed {completed_count} out of 3 questions!")
        
        # Show attempts information
        st.markdown("#### Attempts Information")
        st.markdown(f"""
        - Question 1: {st.session_state.get("q1_attempts", 0)} attempt(s)
        - Question 2: {st.session_state.get("q2_attempts", 0)} attempt(s)
        - Question 3: {st.session_state.get("q3_attempts", 0)} attempt(s)
        """)
        
        # Show progress on specific topics
        st.markdown("#### Topic Mastery")
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
# PART 6: ADDITIONAL RESOURCES AND TABS
# Only show these tabs when the assessment summary is shown (when Q3 is completed)
if st.session_state.q3_completed:
    # Create tabs for additional information
    study_tips_tab, resources_tab, next_steps_tab = st.tabs(["Study Tips", "Resources", "Next Steps"])

    with study_tips_tab:
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

    with resources_tab:
        # Provide specific resources for review based on missed topics
        st.markdown("### 📖 Resources for Your Math Journey")
        
        if score < 3:
            missed_topics = []
            if not st.session_state.get("q1_completed", False):
                missed_topics.append("Linear Equations")
            if not st.session_state.get("q2_completed", False):
                missed_topics.append("Factoring Quadratics")
            if not st.session_state.get("q3_completed", False):
                missed_topics.append("Trigonometry")
                
            for topic in missed_topics:
                if topic == "Linear Equations":
                    st.markdown("""
                    #### Linear Equations Resources
                    - [Khan Academy: Solving Linear Equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities)
                    - Practice with isolating variables and solving step-by-step
                    """)
                elif topic == "Factoring Quadratics":
                    st.markdown("""
                    #### Factoring Quadratics Resources
                    - [Khan Academy: Factoring Quadratics](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring)
                    - Try writing out all pairs of factors for the constant term
                    """)
                elif topic == "Trigonometry":
                    st.markdown("""
                    #### Trigonometry Resources
                    - [Khan Academy: Basic Trigonometry](https://www.khanacademy.org/math/trigonometry/trigonometry-right-triangles)
                    - Practice using your calculator's inverse trigonometric functions
                    """)
        else:
            st.markdown("""
            Congratulations on mastering all the topics! Here are some advanced resources to further your math skills:
            
            - [Khan Academy: Pre-calculus](https://www.khanacademy.org/math/precalculus)
            - [Khan Academy: Calculus](https://www.khanacademy.org/math/calculus-1)
            - [Desmos Graphing Calculator](https://www.desmos.com/calculator) for exploring functions
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
        
        # Offer options based on score
        if score < 3:
            # Offer a chance to try new questions
            if st.button("Try new questions for practice", key="try_new_all"):
                st.session_state.regenerate_q1 = True
                st.session_state.regenerate_q2 = True
                st.session_state.regenerate_q3 = True
                st.rerun()
