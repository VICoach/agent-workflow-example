import streamlit as st
import os
import sys

# Add the parent directory to the system path to allow imports from the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import necessary modules and functions
from src.crew import Demo
from streamlitHelpers import create_sidebar, create_streamlit_UI, create_streamlit_callback

# Set the Streamlit page configuration to wide layout
st.set_page_config(layout="wide")

def main():
    # Create the Streamlit UI with a title and description
    create_streamlit_UI("CrewAI Agent Workflow", "Interactively test your CrewAI agents and tasks.")

    # Create a text input field for the user to enter a topic
    user_input = st.text_input("Enter a topic for the crew to research:", "AI LLMs")
    # Create a button for running the crew
    run_button = st.button("Run Crew")

    # If the run button is clicked and there is user input
    if run_button and user_input:
        # Prepare the inputs for the crew
        inputs = {"topic": user_input, "current_year": "2025"}
        
        # Create an instance of the Demo class and get the crew
        crew_instance = Demo().crew()
        # Display a header for the crew execution log
        st.write("### Crew Execution Log")
        
        try:
            # Execute the crew and capture the output
            result = crew_instance.kickoff(inputs=inputs)
            
            # Display the report output in the Streamlit UI
            st.write("### Report Output")
            st.markdown(result)
        except Exception as e:
            # Display an error message if an exception occurs
            st.error(f"An error occurred: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()