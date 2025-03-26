# Fix for the syntax error on line 328
st.header("Question 3: Intro to Trigonometry")
st.markdown(f"**A right triangle has an angle A such that {st.session_state.trig_function}(A) = {st.session_state.trig_value}. Use your calculator to find angle A in degrees.**")

# Add embedded calculator for question 3
st.markdown("### 🧮 Calculator")
calc_cols = st.columns([2, 1])

with calc_cols[0]:
    # Create a simple calculator UI 
    st.markdown("""
    <style>
    .calc-btn {
        width: 50px;
        height: 50px;
        margin: 5px;
        font-size: 18px;
    }
    </style>
    
    <div>
    <script>
    function updateCalculation(val) {
        document.getElementById('calc-display').value += val;
    }
    
    function calculate() {
        try {
            const display = document.getElementById('calc-display');
            display.value = eval(display.value);
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    
    function clearDisplay() {
        document.getElementById('calc-display').value = '';
    }
    
    function calculateSin() {
        try {
            const display = document.getElementById('calc-display');
            display.value = Math.sin(display.value * Math.PI / 180); // Convert to radians
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    
    function calculateCos() {
        try {
            const display = document.getElementById('calc-display');
            display.value = Math.cos(display.value * Math.PI / 180); // Convert to radians
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    
    function calculateTan() {
        try {
            const display = document.getElementById('calc-display');
            display.value = Math.tan(display.value * Math.PI / 180); // Convert to radians
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    
    function calculateArcSin() {
        try {
            const display = document.getElementById('calc-display');
            display.value = (Math.asin(parseFloat(display.value)) * 180 / Math.PI).toFixed(2); // Convert to degrees
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    
    function calculateArcCos() {
        try {
            const display = document.getElementById('calc-display');
            display.value = (Math.acos(parseFloat(display.value)) * 180 / Math.PI).toFixed(2); // Convert to degrees
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    
    function calculateArcTan() {
        try {
            const display = document.getElementById('calc-display');
            display.value = (Math.atan(parseFloat(display.value)) * 180 / Math.PI).toFixed(2); // Convert to degrees
        } catch(e) {
            document.getElementById('calc-display').value = "Error";
        }
    }
    </script>
    
    <div style="width: 300px; border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
        <input type="text" id="calc-display" style="width: 100%; height: 40px; margin-bottom: 10px; font-size: 18px; text-align: right;">
        
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 5px;">
            <button class="calc-btn" onclick="clearDisplay()">C</button>
            <button class="calc-btn" onclick="updateCalculation('(')">(</button>
            <button class="calc-btn" onclick="updateCalculation(')')">)</button>
            <button class="calc-btn" onclick="updateCalculation('/')">/</button>
            
            <button class="calc-btn" onclick="updateCalculation('7')">7</button>
            <button class="calc-btn" onclick="updateCalculation('8')">8</button>
            <button class="calc-btn" onclick="updateCalculation('9')">9</button>
            <button class="calc-btn" onclick="updateCalculation('*')">×</button>
            
            <button class="calc-btn" onclick="updateCalculation('4')">4</button>
            <button class="calc-btn" onclick="updateCalculation('5')">5</button>
            <button class="calc-btn" onclick="updateCalculation('6')">6</button>
            <button class="calc-btn" onclick="updateCalculation('-')">-</button>
            
            <button class="calc-btn" onclick="updateCalculation('1')">1</button>
            <button class="calc-btn" onclick="updateCalculation('2')">2</button>
            <button class="calc-btn" onclick="updateCalculation('3')">3</button>
            <button class="calc-btn" onclick="updateCalculation('+')">+</button>
            
            <button class="calc-btn" onclick="updateCalculation('0')">0</button>
            <button class="calc-btn" onclick="updateCalculation('.')">.</button>
            <button class="calc-btn" onclick="calculate()">=</button>
            <button class="calc-btn" onclick="updateCalculation('**')">^</button>
        </div>
        
        <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 5px;">
            <button class="calc-btn" onclick="calculateSin()">sin</button>
            <button class="calc-btn" onclick="calculateCos()">cos</button>
            <button class="calc-btn" onclick="calculateTan()">tan</button>
            
            <button class="calc-btn" onclick="calculateArcSin()">sin⁻¹</button>
            <button class="calc-btn" onclick="calculateArcCos()">cos⁻¹</button>
            <button class="calc-btn" onclick="calculateArcTan()">tan⁻¹</button>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

with calc_cols[1]:
    st.markdown("""
    #### Calculator Instructions
    
    1. Enter the value ({trig_value})
    2. Press the {trig_function}⁻¹ button
    3. The result is the angle in degrees
    
    **Tip:** For this problem, you need to use the inverse trigonometric function (find an angle from its {trig_function} value).
    """.format(trig_value=st.session_state.trig_value, trig_function=st.session_state.trig_function))

# Fix for line 539 - Removing duplicated section that causes syntax error
answer3 = st.text_input("Your answer for angle A (in degrees):", key="q3")

# Improved AI tutor section for Question 3
if st.checkbox("🤖 Ask an AI tutor for help with this question", key="q3_ai_toggle"):
    st.info(f"You can ask questions like 'How do I find an angle from its {st.session_state.trig_function}?' or 'What buttons do I press on my calculator?'")
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
                            "content": f"I'm trying to find the angle A in degrees when {st.session_state.trig_function}(A) = {st.session_state.trig_value}. {q3_ai_input}"
                        }
                    ]
                )
                # Store AI response in session state
                st.session_state.q3_ai_response = response.choices[0].message.content
            
            # Display the response from session state in a nicer format
            st.markdown("### 👨‍🏫 AI Tutor Help")
            st.info(st.session_state.q3_ai_response)

# Continue with refresher sections - remove duplicated code
refresher_col3, practice_col3 = st.columns([1, 1])
with refresher_col3:
    if st.button("🔄 Need a refresher for Question 3", key="refresh_q3"):
        st.markdown(f"""
        ### 📘 Refresher: Using {st.session_state.trig_function.capitalize()} to Find Angles

        If you know the {st.session_state.trig_function} of an angle, like `{st.session_state.trig_function}(A) = {st.session_state.trig_value}`, you can find the angle using your calculator:

        **Step 1:** Press the `{st.session_state.trig_function}⁻¹` (also called `arc{st.session_state.trig_function}`) button  
        **Step 2:** Enter the value → `{st.session_state.trig_function}⁻¹({st.session_state.trig_value})`  
        **Result:** `A = {st.session_state.angle_deg}°`

        🧠 This is often used in right triangles when you know the ratio of sides.

        📺 [Watch on Khan Academy](https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-trig-ratios/v/using-trig-ratios-to-solve-right-triangles)
        """)
        # Using a placeholder image instead of external URL for better compatibility with Streamlit
        st.markdown("![Trig ratios](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Triangle_with_notations.svg/640px-Triangle_with_notations.svg.png)")

with practice_col3:
    if st.button("🎮 Practice Similar Problem", key="practice_q3"):
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
            
            **Step 1:** Use the inverse {practice_trig_function} function: B = {practice_trig_function}⁻¹({practice_trig_value})
            
            **Step 2:** Calculate using calculator: B = {practice_angle}°
            
            On most scientific calculators, press the `{practice_trig_function}⁻¹` button followed by {practice_trig_value}
            """)

# Fix for line 539 - Add the Submit button for Question 3
if st.button("✅ Submit Answer 3"):
    try:
        st.session_state.q3_attempts += 1
        # Convert answers to float and compare with a small tolerance for rounding errors
        if abs(float(answer3) - st.session_state.angle_deg) < 0.1:
            st.success(f"Correct! 🎉 Great job finding the angle {st.session_state.angle_deg}°.")
            st.session_state.q3_completed = True
            if "current_score" in st.session_state:
                if not st.session_state.get("q3_already_scored", False):
                    st.session_state.current_score += 1
                    st.session_state.q3_already_scored = True
            st.write("🎆") # Small firework celebration
        else:
            st.error(f"Oops! That's not quite right. The correct answer is {st.session_state.angle_deg}°.")
            
            # Provide detailed feedback for incorrect answers
            with st.expander("See Step-by-Step Solution"):
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
                    st.experimental_rerun()
                else:
                    st.info("Try again! You can edit your answer above and resubmit, or try a new question.")
    except ValueError:
        st.error("Please enter a numeric value for the angle.")
