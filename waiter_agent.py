from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq
import tools
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

os.environ["GROQ_API_KEY"] = groq_api_key


llm = ChatGroq(model_name="deepseek-r1-distill-llama-70b", temperature=0.3)

tool_list = [
    Tool(name="CheckAvailability", func=tools.check_availability, description="Check if an item is available."),
    Tool(name="GetRecommendation", func=tools.get_recommendation, description="Get a dish recommendation based on user preference."),
    Tool(name="MakeReservation", func=lambda x: tools.make_reservation(*x.split(",")), description="Make a reservation with name, time, people."),
    Tool(name="CheckReservation", func=lambda x: tools.check_reservation(*x.split(",")), description="Check if a reservation exists."),
    Tool(name="AllergyInfo", func=tools.allergy_info, description="Get allergen information for a dish."),
    Tool(name="UpdateFAQ", func=lambda x: tools.update_faq(*x.split(",")), description="Add or update an FAQ with a question and answer."),
]

agent = initialize_agent(
    tools=tool_list,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
