from crewai import Task
from agents.editor import editor

edit = Task(
    description="Proofread and edit the blog post to ensure quality, grammar correctness, and brand voice alignment.",
    expected_output="A polished blog post in markdown format, publication-ready.",
    agent=editor
)
