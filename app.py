import streamlit as st
from waiter_agent import agent
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Waiter Bot", page_icon="🍴")

st.title("Welcome to the Waiter Assistant 🍽️")
st.write("""
    Hello! I am here to assist you with various services. 
    You can ask me about:
    1. Menu availability
    2. Reservations
    3. Dish recommendations
    4. Allergen information
    5. FAQ updates
""")

def run_query(query):
    try:
        response = agent.invoke({"input": query}, handle_parsing_errors=True)

        if "Final Answer:" in response:
            response = response.split("Final Answer:")[1].strip()
        return response
    except Exception as e:
        return f"Error: {str(e)}"


query = st.text_input("Ask your question:")

if st.button("Submit"):
    if query:
        with st.spinner("Processing your request..."):
            response = run_query(query)
        st.write("Response:")
        st.write(response)
    else:
        st.warning("Please enter a query.")

