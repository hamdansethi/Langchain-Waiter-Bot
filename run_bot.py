from waiter_agent import agent
import os
from dotenv import load_dotenv

load_dotenv()

def run_query(query):
    prompt = f"""
    You are a helpful restaurant assistant, and you can only provide answers related to the following tasks:
    1. Checking the availability of items on the menu.
    2. Making reservations (including name, time, and number of people).
    3. Providing allergen information for dishes.
    4. Offering recommendations based on user preferences.
    5. Adding or updating FAQ responses.

    If the query is unrelated to any of these tasks, respond with: "Sorry, I cannot assist with that request."
    
    Please process the following query: "{query}"
    """

    try:
        response = agent.invoke({"input": prompt}, handle_parsing_errors=True)
        return response
    except Exception as e:
        return f"Error: {str(e)}"



# query = "Is Grilled Salmon available?"
query = "Helicopter?"
response = run_query(query)
print(response)

# # Make a reservation
# query = "Make a reservation for Sarah,6:30 PM,3"
# response = run_query(query)
# print(response)

# # Check existing reservation
# query = "Check reservation for Sarah at 6:30 PM"
# response = run_query(query)
# print(response)

# # Get allergen info
# query = "Does the Caesar Salad contain nuts?"
# response = run_query(query)
# print(response)

# # Get a recommendation based on preference
# query = "Can you recommend something light?"
# response = run_query(query)
# print(response)

# # Update FAQ
# query = "Add a new FAQ, 'What are your operating hours?', 'We are open from 9 AM to 11 PM.'"
# response = run_query(query)
# print(response)
