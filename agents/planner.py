from crewai import Agent
from models.llm import get_model

# Retrieve the correct model and client
client, model = get_model("mistral")  # Default to Mistral, but can be changed

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You're a planner who outlines blog articles...",
    llm=model,  # ✅ Correctly passing the model name
    allow_delegation=False,
    verbose=True
)
