from crewai import Agent
from models.llm import get_model  # Fetch user-specified model

# Unpack the client and model
client, model = get_model()  # Default to "mistral" or whichever default you set in get_model()

writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate content on {topic}",
    backstory=(
        "You're writing a new piece about {topic}. "
        "You rely on the Planner’s outline to craft an engaging and "
        "structured article. Your work should balance objectivity with insights."
    ),
    llm=model,  # Use the model name from get_model()
    allow_delegation=False,
    verbose=True
)
