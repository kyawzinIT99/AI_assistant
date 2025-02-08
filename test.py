import logging
import os
import google.generativeai as genai
import streamlit as st

# Logger configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def gemini_model(user_input):
    """Generate a response using the Gemini model."""
    genai.configure(api_key="AIzaSyDc4i0KI1rNvIbVYUw0I0zr--ox0eH1JgM")  # Replace with your actual API key
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    return response.text

def main():
    #Display the company logo 
    st.logo("sunfar.JPG", size="large")
    st.title("AI Assistant by SUNFAR ")

    # Initialize session state for input fields if not already done
    if 'input_fields' not in st.session_state:
        st.session_state.input_fields = ['']

    # Function to add a new input field
    def add_input_field():
        st.session_state.input_fields.append('')

    # Display existing input fields
    for i, _ in enumerate(st.session_state.input_fields):
        st.session_state.input_fields[i] = st.text_input(f"Question {i + 1}", st.session_state.input_fields[i])

    # Button to add a new input field
    st.button("Add another question", on_click=add_input_field)

    # Process the inputs when the user is ready
    if st.button("Submit"):
        for i, question in enumerate(st.session_state.input_fields):
            if question.strip():  # Ensure the question is not empty
                response = gemini_model(question)
                st.text_area(label=f"Response to Question {i + 1}:", value=response, height=150)

if __name__ == "__main__":
    main()
