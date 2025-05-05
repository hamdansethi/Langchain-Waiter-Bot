import json
import os

# Load the data files (menu.txt, faq.txt, policies.txt)
menu_file_path = "data/menu.txt"
faq_file_path = "data/faq.txt"
policies_file_path = "data/policies.txt"
reservations_file_path = "data/reservations.json"

# Ensure data files exist
os.makedirs("data", exist_ok=True)

# Function to load data from a file with error handling
def load_data_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
        return ""
    except Exception as e:
        print(f"Error loading {file_path}: {str(e)}")
        return ""

# Load Menu, Policies, and FAQs
menu_data = load_data_from_file(menu_file_path).splitlines()
faq_data = load_data_from_file(faq_file_path).splitlines()
policies_data = load_data_from_file(policies_file_path).splitlines()

# Read existing reservations from JSON file (if it exists)
def load_reservations():
    try:
        if os.path.exists(reservations_file_path):
            with open(reservations_file_path, "r") as file:
                return json.load(file)
    except Exception as e:
        print(f"Error loading reservations: {str(e)}")
    return []

# Save reservations to a JSON file
def save_reservation(name, time, people):
    reservations = load_reservations()
    reservation = {
        "name": name,
        "time": time,
        "people": people
    }
    reservations.append(reservation)
    try:
        with open(reservations_file_path, "w") as file:
            json.dump(reservations, file, indent=4)
        return f"Reservation for {name} at {time} for {people} people has been saved."
    except Exception as e:
        return f"Error saving reservation: {str(e)}"

# Check if a reservation exists
def check_reservation(name, time):
    reservations = load_reservations()
    for reservation in reservations:
        if reservation["name"].lower() == name.lower() and reservation["time"] == time:
            return f"Reservation for {name} at {time} already exists."
    return f"No reservation found for {name} at {time}."

# Function to calculate the total order cost
def calculate_total(order_items):
    if not order_items:
        return "No items in order."
    total = sum(item.get("price", 0) for item in order_items)
    return f"Your total is ${total:.2f}"

# Check availability of an item in the menu (case-insensitive)
def check_availability(item_name):
    if not item_name:
        return "Please provide an item name."
    available = any(item_name.lower() in item.lower() for item in menu_data)
    return f"Yes, {item_name} is available." if available else f"Sorry, {item_name} is not on the menu."

# Recommend a dish based on customer preference
def get_recommendation(preference):
    if not preference:
        return "Please tell me your preference (e.g., vegan, spicy, light, seafood)."
    recommendations = {
        "vegan": "You might like our Vegan Pizza or Fresh Garden Salad.",
        "spicy": "Try our Spicy Pepperoni Pizza!",
        "light": "The Caesar Salad is a great light option.",
        "seafood": "Our Grilled Salmon is a customer favorite.",
    }
    return recommendations.get(preference.lower(), "Can you tell me more about your preferences?")

# Make a reservation
def make_reservation(name, time, people):
    if not name or not time or not people:
        return "Please provide name, time, and number of people for the reservation."
    return save_reservation(name, time, people)

# Get allergen information
def allergy_info(item_name):
    if not item_name:
        return "Please provide an item name to check for allergens."
    allergens = {
        "pizza": "Contains gluten and dairy.",
        "salad": "Contains eggs and may contain traces of nuts.",
        "salmon": "May contain fish and soy."
    }
    for key, value in allergens.items():
        if key in item_name.lower():
            return f"{item_name.title()}: {value}"
    return f"No allergen info found for {item_name}."

# Update FAQs
def update_faq(question, answer):
    if not question or not answer:
        return "Please provide both a question and an answer."
    faq_data.append(f"Q: {question}\nA: {answer}")
    try:
        with open(faq_file_path, "a") as file:
            file.write(f"Q: {question}\nA: {answer}\n")
        return f"FAQ added: Q: {question}, A: {answer}"
    except Exception as e:
        return f"Error updating FAQ: {str(e)}"
