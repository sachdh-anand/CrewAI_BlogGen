from crewai import Agent
from models.llm import get_model  # Fetch user-specified model

# Unpack the client and model
client, model = get_model()  # Default to "mistral" or whichever model is set in get_model()

editor = Agent(
    role="Editor",
    goal="Edit the given blog post to align with the organization’s style.",
    backstory=(
        "You review the writer's work to ensure high quality, "
        "grammar correctness, and alignment with journalistic best practices."
    ),
    llm=model,  # ✅ Use the correct model string
    allow_delegation=False,
    verbose=True
)
