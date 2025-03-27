⁻¹
                
                **Step 3:** A = {st.session_state.trig_function}⁻¹({st.session_state.trig_value})
                
                **Step 4:** Using a calculator with the {st.session_state.trig_function}⁻¹ button:
                - Enter {st.session_state.trig_value}
                - Press {st.session_state.trig_function}⁻¹
                - Result: A = {st.session_state.angle_deg}°
                """)
            
            # Add button to generate a new question
            if st.button("Get a new question", key="new_q3"):
                # Store current values before regenerating
                old_function = st.session_state.trig_function
                old_value = st.session_state.trig_value
                # Generate a new problem ensuring it's different
                while True:
                    st.session_state.trig_function, st.session_state.trig_value, st.session_state.angle_deg = generate_trig_problem()
                    if (st.session_state.trig_function != old_function or st.session_state.trig_value != old_value):
                        break
                st.rerun()  # Only rerun after generating a new problem
    except ValueError:
        st.error("Please enter a numeric value for the angle.")

st.markdown("---")

# ASSESSMENT SUMMARY - ONLY SHOW WHEN QUESTION 3 IS COMPLETED
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
