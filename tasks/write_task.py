from crewai import Task
from agents.writer import writer

write = Task(
    description=(
        "1. Use the content plan to create a compelling blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
        "3. Ensure structured writing with an engaging introduction, body, and conclusion.\n"
        "4. Proofread for grammar errors and brand voice consistency."
    ),
    expected_output="A well-structured blog post in markdown format, ready for publication.",
    agent=writer
)
