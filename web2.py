import streamlit as st
import google.generativeai as genai


def get_recommendations(body_part, muscle_pain, workout_type):
    genai.configure(api_key='AIzaSyCvJ1kAUwogUcM1PgTt6E5-92zbdLLLyJk')
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"Recommend a workout for {body_part} focusing on {muscle_pain} for {workout_type} training. Include exercise name and sets/reps."
    
    response = model.generate_content(prompt)
    
    if response:
        # Parse the response text to extract exercise and sets/reps
        # This will depend on how you structure your prompt and how you want to format the output
        exercise = "Extracted exercise from response"
        sets_reps = "Extracted sets/reps from response"
        return exercise, sets_reps
    else:
        st.error("Failed to get recommendations from Gemini API")
        return "No recommendation", "N/A"

# App layout
st.title("Workout Recommendation")

# Step 1: Choose the part of the body
body_part = st.selectbox("Choose the Part of Body:",["arm","leg","chest","back","shoulder","abs"])

# Step 2: Where do you have muscle pain
muscle_pain = st.selectbox("Where do you have muscle pain?", ["triceps", "biceps", "leg", "shoulder", "back", "chest", "abs"])

# Step 3: What type of workout are you planning
workout_type = st.selectbox("What type of workout are you planning to?", ["hypertrophy", "strength", "interval"])

# Step 4: Show recommendation
if st.button("Recommended WOD"):
    exercise, sets_reps = get_recommendations(body_part, muscle_pain, workout_type)
    st.subheader("Recommended Exercise")
    st.write(f"Exercise: {exercise}")
    st.write(f"Sets and Reps: {sets_reps}")

if __name__ == "__main__":
    get_recommendations(body_part, muscle_pain, workout_type)
