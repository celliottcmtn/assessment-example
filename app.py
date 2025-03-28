import openai
import random
import math
import streamlit as st

# Load the OpenAI API key from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ----- DEFINE ALL FUNCTIONS FIRST -----

# QUESTION 1: LINEAR EQUATION
# Function to generate a new linear equation
def generate_linear_equation():
    coeff = random.randint(2, 8)
    solution = random.randint(-5, 10)  # Random solution value
    const = random.randint(-10, 15)
    rhs = coeff * solution + const
    return coeff, const, rhs, solution

# Function to generate new question for Q1 and store it
def generate_new_q1():
    old_solution = st.session_state.q1_solution
    while True:
        new_coeff, new_const, new_rhs, new_solution = generate_linear_equation()
        if new_solution != old_solution:
            break
    return new_coeff, new_const, new_rhs, new_solution

# QUESTION 2: FACTORING
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

# Function to generate new question for Q2 and store it
def generate_new_q2():
    old_r1, old_r2 = st.session_state.r1, st.session_state.r2
    while True:
        new_r1, new_r2, new_trinomial_b, new_trinomial_c = generate_factoring_problem()
        if (new_r1 != old_r1 or new_r2 != old_r2):
            break
    return new_r1, new_r2, new_trinomial_b, new_trinomial_c

# QUESTION 3: TRIGONOMETRY
# Function to generate a new trigonometry problem
def generate_trig_problem():
    # Random trig function (sin, cos, or tan)
    trig_function = random.choice(["sin", "cos", "tan"])
    
    # Generate appropriate values based on the function
    if trig_function == "sin":
        trig_value = round(random.uniform(0.1, 0.95), 2)
        angle_deg = round(math.degrees(math.asin(trig_value)), 2)
    elif trig_function == "cos":
        trig_value = round(random.uniform(0.1, 0.95), 2)
        angle_deg = round(math.degrees(math.acos(trig_value)), 2)
    else:  # tan
        trig_value = round(random.uniform(0.1, 2.0), 2)
        angle_deg = round(math.degrees(math.atan(trig_value)), 2)
    
    return trig_function, trig_value, angle_deg

# Function to generate new question for Q3 and store it
def generate_new_q3():
    old_function = st.session_state.trig_function
    old_value = st.session_state.trig_value
    while True:
        new_trig_function, new_trig_value, new_angle_deg = generate_trig_problem()
        if (new_trig_function != old_function or new_trig_value != old_value):
            break
    return new_trig_function, new_trig_value, new_angle_deg

# ----- APP BEGINS HERE -----

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

# Initialize feedback flags
if "showing_q1_feedback" not in st.session_state:
    st.session_state.showing_q1_feedback = False
if "showing_q2_feedback" not in st.session_state:
    st.session_state.showing_q2_feedback = False
if "showing_q3_feedback" not in st.session_state:
    st.session_state.showing_q3_feedback = False

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
if st.sidebar.button("🔄 Reset Assessment", key="reset_button"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Initialize random values in session state
if "coeff" not in st.session_state:
    st.session_state.coeff, st.session_state.const, st.session_state.rhs, st.session_state.q1_solution = generate_linear_equation()

# Initialize factoring problem
if "r1" not in st.session_state:
    st.session_state.r1, st.session_state.r2, st.session_state.trinomial_b, st.session_state.trinomial_c = generate_factoring_problem()

# Initialize trigonometry problem
if "trig_function" not in st.session_state:
    st.session_state.trig_function, st.session_state.trig_value, st.session_state.angle_deg = generate_trig_problem()

# ----- QUESTION 1 IMPLEMENTATION -----

st.header("Question 1: Solving Linear Equations")
st.markdown(f"**Solve for x in the equation below:**")
st.latex(f"{st.session_state.coeff}x + {st.session_state.const} = {st.session_state.rhs}")

refresher_col1, practice_col1 = st.columns([1, 1])
with refresher_col1:
    if st.button("🔄 Need a refresher for Question 1", key="refresh_q1_button"):
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
    if st.button("🎮 Practice Similar Problem", key="practice_q1_button"):
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

answer3 = st.text_input("Your answer for angle A (in degrees):", key="answer_q3_input")

# Improved AI tutor section for Question 3
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="ai_q3_checkbox"):
    st.info(f"You can ask questions like 'How do I find an angle from its {st.session_state.trig_function}?' or 'What buttons do I press on my calculator?'")
    q3_ai_input = st.text_area("What would you like to ask about Question 3?", key="ai_q3_text")
    
    if st.button("Ask AI about Question 3", key="ask_ai_q3_button"):
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
                            "content": f"I'm trying to find the angle A in degrees when {st.session_state.trig_function}(A) = {st.session_state.trig_value}. {q3_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q3_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q3_ai_response)

# Modified Question 3 submit handler
if st.button("✅ Submit Answer 3", key="submit_q3_button"):
    try:
        st.session_state.q3_attempts += 1
        # Convert answers to float and compare with a small tolerance for rounding errors
        if abs(float(answer3) - st.session_state.angle_deg) < 0.1:
            st.success(f"Correct! Great job finding the angle {st.session_state.angle_deg}°.")
            st.session_state.q3_completed = True
            if not st.session_state.get("q3_already_scored", False):
                st.session_state.current_score += 1
                st.session_state.q3_already_scored = True
                st.rerun()  # Only rerun on correct answer
        else:
            # Store current problem details for feedback
            st.session_state.q3_last_function = st.session_state.trig_function
            st.session_state.q3_last_value = st.session_state.trig_value
            st.session_state.q3_last_angle = st.session_state.angle_deg
            
            # Generate and store new problem for next attempt
            new_trig_function, new_trig_value, new_angle_deg = generate_new_q3()
            st.session_state.q3_next_function = new_trig_function
            st.session_state.q3_next_value = new_trig_value
            st.session_state.q3_next_angle = new_angle_deg
            
            # Show feedback without rerunning
            st.session_state.showing_q3_feedback = True
            st.error(f"Oops! That's not quite right. The correct answer is {st.session_state.q3_last_angle}°.")
            
            # Provide detailed feedback for incorrect answers
            with st.expander("See Step-by-Step Solution", expanded=True):
                st.markdown(f"""
                ### Solution Walkthrough:
                
                **Step 1:** We know that {st.session_state.q3_last_function}(A) = {st.session_state.q3_last_value}
                
                **Step 2:** To find angle A, we need to use the inverse function {st.session_state.q3_last_function}^(-1)
                
                **Step 3:** A = {st.session_state.q3_last_function}^(-1)({st.session_state.q3_last_value})
                
                **Step 4:** Using a calculator with the {st.session_state.q3_last_function}^(-1) button:
                - Enter {st.session_state.q3_last_value}
                - Press {st.session_state.q3_last_function}^(-1)
                - Result: A = {st.session_state.q3_last_angle}°
                """)
    except ValueError:
        st.error("Please enter a numeric value for the angle.")
        
# Display the Next Question button for Q3 when showing feedback
if st.session_state.showing_q3_feedback:
    if st.button("➡️ Next Question", key="next_q3_button"):
        # Apply stored next question values
        st.session_state.trig_function = st.session_state.q3_next_function
        st.session_state.trig_value = st.session_state.q3_next_value
        st.session_state.angle_deg = st.session_state.q3_next_angle
        st.session_state.showing_q3_feedback = False
        st.rerun()

st.markdown("---")

# ----- ASSESSMENT SUMMARY -----
# Show assessment summary based on completed questions
if st.session_state.q1_completed or st.session_state.q2_completed or st.session_state.q3_completed:
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
        
        # Show which questions were correct
        correct_topics = []
        if st.session_state.get("q1_completed", False):
            correct_topics.append("Linear Equations")
        if st.session_state.get("q2_completed", False):
            correct_topics.append("Factoring Quadratics")
        if st.session_state.get("q3_completed", False):
            correct_topics.append("Trigonometry")
            
        if correct_topics:
            topics_str = ", ".join(correct_topics)
            st.markdown(f"You demonstrated understanding of **{topics_str}**. Focus on strengthening the other areas.")
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
            if st.button("Try new questions for practice", key="try_new_all_button"):
                # Reset appropriate session state values for regeneration
                if not st.session_state.q1_completed:
                    st.session_state.coeff, st.session_state.const, st.session_state.rhs, st.session_state.q1_solution = generate_linear_equation()
                
                if not st.session_state.q2_completed:
                    st.session_state.r1, st.session_state.r2, st.session_state.trinomial_b, st.session_state.trinomial_c = generate_factoring_problem()
                
                if not st.session_state.q3_completed:
                    st.session_state.trig_function, st.session_state.trig_value, st.session_state.angle_deg = generate_trig_problem()
                
                st.rerun()
    
answer1 = st.text_input("Your answer for x:", key="answer_q1_input")

# Improved AI tutor section for Question 1
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="ai_q1_checkbox"):
    st.info("You can ask questions like 'How do I isolate x?' or 'What's the first step to solve this?'")
    q1_ai_input = st.text_area("What would you like to ask about Question 1?", key="ai_q1_text")
    
    if st.button("Ask AI about Question 1", key="ask_ai_q1_button"):
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

# Modified Question 1 submit handler
if st.button("✅ Submit Answer 1", key="submit_q1_button"):
    try:
        st.session_state.q1_attempts += 1
        if abs(float(answer1) - st.session_state.q1_solution) < 0.01:
            st.success(f"Correct! Great job solving for x = {st.session_state.q1_solution}.")
            st.session_state.q1_completed = True
            if not st.session_state.get("q1_already_scored", False):
                st.session_state.current_score += 1
                st.session_state.q1_already_scored = True
                st.rerun()  # Only rerun on correct answer to update score
        else:
            # Store current problem details for feedback
            st.session_state.q1_last_coeff = st.session_state.coeff
            st.session_state.q1_last_const = st.session_state.const
            st.session_state.q1_last_rhs = st.session_state.rhs
            st.session_state.q1_last_solution = st.session_state.q1_solution
            
            # Generate and store new problem for next attempt
            new_coeff, new_const, new_rhs, new_solution = generate_new_q1()
            st.session_state.q1_next_coeff = new_coeff
            st.session_state.q1_next_const = new_const
            st.session_state.q1_next_rhs = new_rhs
            st.session_state.q1_next_solution = new_solution
            
            # Show feedback without rerunning
            st.session_state.showing_q1_feedback = True
            st.error(f"Oops! That's not quite right. The correct answer is {st.session_state.q1_last_solution}.")
            
            # Provide detailed feedback
            with st.expander("See Step-by-Step Solution", expanded=True):
                st.markdown(f"""
                ### Solution Walkthrough:
                
                **Step 1:** Subtract {st.session_state.q1_last_const} from both sides  
                `{st.session_state.q1_last_coeff}x + {st.session_state.q1_last_const} - {st.session_state.q1_last_const} = {st.session_state.q1_last_rhs} - {st.session_state.q1_last_const}`  
                `{st.session_state.q1_last_coeff}x = {st.session_state.q1_last_rhs - st.session_state.q1_last_const}`
                
                **Step 2:** Divide both sides by {st.session_state.q1_last_coeff}  
                `{st.session_state.q1_last_coeff}x ÷ {st.session_state.q1_last_coeff} = {st.session_state.q1_last_rhs - st.session_state.q1_last_const} ÷ {st.session_state.q1_last_coeff}`  
                `x = {st.session_state.q1_last_solution}`
                
                **Check:** Substitute x = {st.session_state.q1_last_solution} back into the original equation  
                `{st.session_state.q1_last_coeff} × {st.session_state.q1_last_solution} + {st.session_state.q1_last_const} = {st.session_state.q1_last_coeff * st.session_state.q1_last_solution + st.session_state.q1_last_const}`  
                `{st.session_state.q1_last_coeff * st.session_state.q1_last_solution + st.session_state.q1_last_const} = {st.session_state.q1_last_rhs}` ✓
                """)
    except ValueError:
        st.error("Please enter a numeric value.")

# Display the Next Question button for Q1 when showing feedback
if st.session_state.showing_q1_feedback:
    if st.button("➡️ Next Question", key="next_q1_button"):
        # Apply stored next question values
        st.session_state.coeff = st.session_state.q1_next_coeff
        st.session_state.const = st.session_state.q1_next_const
        st.session_state.rhs = st.session_state.q1_next_rhs
        st.session_state.q1_solution = st.session_state.q1_next_solution
        st.session_state.showing_q1_feedback = False
        st.rerun()

st.markdown("---")

# ----- QUESTION 2 IMPLEMENTATION -----

st.header("Question 2: Factoring Quadratic Equations")
st.markdown(f"**Factor the quadratic expression below:**")
st.latex(f"x^2 + {st.session_state.trinomial_b}x + {st.session_state.trinomial_c}")

refresher_col2, practice_col2 = st.columns([1, 1])
with refresher_col2:
    if st.button("🔄 Need a refresher for Question 2", key="refresh_q2_button"):
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
        # Using a placeholder image
        st.markdown("![Factoring quadratics](https://cdn.kastatic.org/ka-perseus-images/5ceff8a3e7416c1c798193baad3d24988a4f15f9.png)")

with practice_col2:
    if st.button("🎮 Practice Similar Problem", key="practice_q2_button"):
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

answer2 = st.text_input("Your factored expression:", key="answer_q2_input")

# Define correct factored answers for this problem
r1, r2 = st.session_state.r1, st.session_state.r2
correct_factored = [f"(x+{r1})(x+{r2})", f"(x+{r2})(x+{r1})", 
                   f"(x + {r1})(x + {r2})", f"(x + {r2})(x + {r1})",
                   f"(x{r1:+})(x{r2:+})", f"(x{r2:+})(x{r1:+})"]  # Format with + sign

# Improved AI tutor section for Question 2
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="ai_q2_checkbox"):
    st.info("You can ask questions like 'How do I factor this?' or 'What numbers multiply to give the constant term?'")
    q2_ai_input = st.text_area("What would you like to ask about Question 2?", key="ai_q2_text")
    
    if st.button("Ask AI about Question 2", key="ask_ai_q2_button"):
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
                            "content": f"I'm factoring this quadratic expression: x^2 + {st.session_state.trinomial_b}x + {st.session_state.trinomial_c}. {q2_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q2_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q2_ai_response)

# Modified Question 2 submit handler
if st.button("✅ Submit Answer 2", key="submit_q2_button"):
    try:
        st.session_state.q2_attempts += 1
        simplified = answer2.replace(" ", "")
        if any(simplified == ans.replace(" ", "") for ans in correct_factored):
            st.success("✅ Correct! Well done.")
            st.session_state.q2_completed = True
            if not st.session_state.get("q2_already_scored", False):
                st.session_state.current_score += 1
                st.session_state.q2_already_scored = True
                st.rerun()  # Only rerun on correct answer
        else:
            # Store current problem details for feedback
            st.session_state.q2_last_r1 = st.session_state.r1
            st.session_state.q2_last_r2 = st.session_state.r2
            st.session_state.q2_last_b = st.session_state.trinomial_b
            st.session_state.q2_last_c = st.session_state.trinomial_c
            
            # Generate and store new problem for next attempt
            new_r1, new_r2, new_trinomial_b, new_trinomial_c = generate_new_q2()
            st.session_state.q2_next_r1 = new_r1
            st.session_state.q2_next_r2 = new_r2
            st.session_state.q2_next_b = new_trinomial_b
            st.session_state.q2_next_c = new_trinomial_c
            
            # Show feedback without rerunning
            st.session_state.showing_q2_feedback = True
            st.error(f"❌ Not quite. One correct answer is (x + {st.session_state.q2_last_r1})(x + {st.session_state.q2_last_r2}).")
            
            # Provide detailed feedback
            with st.expander("See Step-by-Step Solution", expanded=True):
                st.markdown(f"""
                ### Solution Walkthrough:
                
                **Step 1:** For the trinomial `x² + {st.session_state.q2_last_b}x + {st.session_state.q2_last_c}`, find two numbers that:
                - Multiply to give {st.session_state.q2_last_c}
                - Add to give {st.session_state.q2_last_b}
                
                **Step 2:** The numbers {st.session_state.q2_last_r1} and {st.session_state.q2_last_r2} work because:
                - {st.session_state.q2_last_r1} × {st.session_state.q2_last_r2} = {st.session_state.q2_last_r1 * st.session_state.q2_last_r2}
                - {st.session_state.q2_last_r1} + {st.session_state.q2_last_r2} = {st.session_state.q2_last_r1 + st.session_state.q2_last_r2}
                
                **Step 3:** Write the factored form:
                - (x + {st.session_state.q2_last_r1})(x + {st.session_state.q2_last_r2})
                
                **Check:** Multiply it out to verify:
                - First term: x × x = x²
                - Middle terms: x × {st.session_state.q2_last_r2} + {st.session_state.q2_last_r1} × x = {st.session_state.q2_last_r2}x + {st.session_state.q2_last_r1}x = {st.session_state.q2_last_r1 + st.session_state.q2_last_r2}x
                - Last term: {st.session_state.q2_last_r1} × {st.session_state.q2_last_r2} = {st.session_state.q2_last_r1 * st.session_state.q2_last_r2}
                
                So (x + {st.session_state.q2_last_r1})(x + {st.session_state.q2_last_r2}) = x² + {st.session_state.q2_last_b}x + {st.session_state.q2_last_c} ✓
                """)
    except Exception as e:
        st.error(f"An error occurred: {e}. Please try again.")

# Display the Next Question button for Q2 when showing feedback
if st.session_state.showing_q2_feedback:
    if st.button("➡️ Next Question", key="next_q2_button"):
        # Apply stored next question values
        st.session_state.r1 = st.session_state.q2_next_r1
        st.session_state.r2 = st.session_state.q2_next_r2
        st.session_state.trinomial_b = st.session_state.q2_next_b
        st.session_state.trinomial_c = st.session_state.q2_next_c
        st.session_state.showing_q2_feedback = False
        st.rerun()

st.markdown("---")

# ----- QUESTION 3 IMPLEMENTATION -----

st.header("Question 3: Intro to Trigonometry")
st.markdown(f"**A right triangle has an angle A such that {st.session_state.trig_function}(A) = {st.session_state.trig_value}. Find angle A in degrees.**")

# Provide hint for calculation and link to online calculator
st.info(f"""
To solve this problem:
1. You need to find the inverse {st.session_state.trig_function} of {st.session_state.trig_value}
2. That is, calculate {st.session_state.trig_function}^(-1)({st.session_state.trig_value})
3. Use the online calculator linked below (make sure it's in degree mode)
""")

st.markdown("#### Online Calculator Tools")
st.markdown("""
[Desmos Scientific Calculator](https://www.desmos.com/scientific)

[GeoGebra Scientific Calculator](https://www.geogebra.org/scientific)

[web2.0calc Scientific Calculator](https://web2.0calc.com/)
""")

# Option to reveal the answer
if st.button("Show me the calculation result", key="show_result_q3_button"):
    st.session_state.calculated_angle = st.session_state.angle_deg
    st.success(f"Result: {st.session_state.angle_deg}°")

if "calculated_angle" in st.session_state:
    st.info(f"You can use this value as your answer: {st.session_state.calculated_angle}°")

# Calculator tips
st.markdown(f"""
### Calculator Tips

On a scientific calculator:
1. Enter {st.session_state.trig_value}
2. Press the {st.session_state.trig_function}^(-1) button (or 2nd function + {st.session_state.trig_function})
3. Read the angle in degrees (make sure calculator is in degree mode)
""")

refresher_col3, practice_col3 = st.columns([1, 1])
with refresher_col3:
    if st.button("🔄 Need a refresher for Question 3", key="refresh_q3_button"):
        st.markdown(f"""
        ### 📘 Refresher: Using {st.session_state.trig_function.capitalize()} to Find Angles

        If you know the {st.session_state.trig_function} of an angle, like `{st.session_state.trig_function}(A) = {st.session_state.trig_value}`, you can find the angle using your calculator:

        **Step 1:** Press the `{st.session_state.trig_function}^(-1)` (also called `arc{st.session_state.trig_function}`) button  
        **Step 2:** Enter the value → `{st.session_state.trig_function}^(-1)({st.session_state.trig_value})`  
        **Result:** `A = {st.session_state.angle_deg}°`

        🧠 This is often used in right triangles when you know the ratio of sides.

        📺 [Watch on Khan Academy](https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-trig-ratios/v/using-trig-ratios-to-solve-right-triangles)
        """)
        # Using a placeholder image
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Triangle_with_notations.svg/640px-Triangle_with_notations.svg.png", caption="Trigonometric ratios in a right triangle")

with practice_col3:
    if st.button("🎮 Practice Similar Problem", key="practice_q3_button"):
        # Generate a practice trig problem
        practice_trig_function = random.choice(["sin", "cos", "tan"])
        
        if practice_trig_function == "sin":
            practice_trig_value = round(random.uniform(0.1, 0.95), 2)
            practice_angle = round(math.degrees(math.asin(practice_trig_value)), 2)
        elif practice_trig_function == "cos":
            practice_trig_value = round(random.uniform(0.1, 0.95), 2)
            practice_angle = round(math.degrees(math.acos(practice_trig_value)), 2)
        else:  # tan
            practice_trig_value = round(random.uniform(0.1, 2.0), 2)
            practice_angle = round(math.degrees(math.atan(practice_trig_value)), 2)
        
        st.markdown(f"**Practice Problem:** Find angle B in degrees where {practice_trig_function}(B) = {practice_trig_value}")
        
        with st.expander("See Solution"):
            st.markdown(f"""
            To find angle B when {practice_trig_function}(B) = {practice_trig_value}:
            
            **Step 1:** Use the inverse {practice_trig_function} function: B = {practice_trig_function}^(-1)({practice_trig_value})
            
            **Step 2:** Calculate using calculator: B = {practice_angle}°
            
            On most scientific calculators, press the `{practice_trig_function}^(-1)` button followed by {practice_trig_value}
            """)
