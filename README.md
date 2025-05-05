# Langchain Waiter Bot

Welcome to the **Langchain Waiter Bot** project! This bot is an AI assistant designed to handle various customer queries related to a restaurant, such as checking menu availability, making reservations, providing dish recommendations, checking allergen information, and managing FAQs. It uses **LangChain** for agent-based automation and **LangGraph** for more flexible and powerful workflows.

---

## Features

The AI assistant can handle the following services:

1. **Check Availability**: Check if a specific item is available on the menu.
2. **Make Reservation**: Make a reservation by specifying the name, time, and number of people.
3. **Get Recommendation**: Get dish recommendations based on user preferences.
4. **Allergy Info**: Provide allergen information for dishes on the menu.
5. **Update FAQ**: Add or update an FAQ response to common customer questions.

---

## Prerequisites

To run the project, you will need the following:

- Python 3.x
- Libraries:
  - `langchain`
  - `langchain-groq`
  - `os`
  - `modules` (specific to your setup)
  - **Groq API Key** (for LangGroq model usage)

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
