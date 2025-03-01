from crewai import Task
from agents.planner import planner

plan = Task(
    description=(
        "1. Prioritize latest trends, key players, and noteworthy news on {topic}.\n"
        "2. Identify the target audience and their pain points.\n"
        "3. Develop a content outline, including an introduction, key points, and CTA.\n"
        "4. Include SEO keywords and relevant data sources."
    ),
    expected_output="A detailed content plan document with outline, audience analysis, SEO keywords, and resources.",
    agent=planner
)
