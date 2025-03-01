import os
import re
import markdown  # ✅ Ensure Markdown is properly converted
from dotenv import load_dotenv
from models.llm import get_model
from crewai import Crew
from tasks.plan_task import plan
from tasks.write_task import write
from tasks.edit_task import edit

# Load environment variables
load_dotenv()
print("✅ Environment variables loaded.")  # Debug log

# ✅ Debug flag - set to True to test model API connection before running
DEBUG_MODE = True

# Define paths for better organization
OUTPUT_FOLDER = "output"
TEMPLATE_FOLDER = os.path.join(OUTPUT_FOLDER, "templates")
TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, "blog_template.html")

# Ensure necessary folders exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(TEMPLATE_FOLDER, exist_ok=True)

# Allowed model choices
VALID_MODELS = ["mistral", "huggingface", "llama"]

# Choose LLM model with validation
model_choice = input("Choose LLM model (mistral / huggingface / llama): ").strip().lower()
if model_choice not in VALID_MODELS:
    print(f"❌ ERROR: Invalid model choice '{model_choice}'. Defaulting to 'mistral'.")
    model_choice = "mistral"

print(f"✅ Model selected: {model_choice}")

# Get model and client
try:
    # ✅ Pass the debug flag to run test when DEBUG_MODE is enabled
    client, model = get_model(model_choice, test=DEBUG_MODE)
    if model is None:
        raise ValueError("❌ ERROR: Model returned as None. Please check `get_model()` implementation.")
except Exception as e:
    print(f"❌ ERROR: Failed to load model: {e}")
    exit(1)

print(f"✅ Model initialized: {model}")  # Debug log

# Initialize CrewAI
try:
    crew = Crew(
        agents=[plan.agent, write.agent, edit.agent],
        tasks=[plan, write, edit],
        verbose=True
    )
    print("✅ Crew initialized.")  # Debug log
except Exception as e:
    print(f"❌ ERROR: Failed to initialize CrewAI: {e}")
    exit(1)

# Run CrewAI workflow
topic = input("Enter a topic: ").strip()
if not topic:
    print("❌ ERROR: No topic entered. Exiting.")
    exit(1)

print(f"✅ Topic received: {topic}")

# ✅ Generate a safe filename based on the topic
safe_topic = re.sub(r"[^\w\s-]", "", topic).strip().replace(" ", "_")
output_filename = f"{safe_topic}.html"
output_path = os.path.join(OUTPUT_FOLDER, output_filename)

# Execute CrewAI workflow with error handling
try:
    result = crew.kickoff(inputs={"topic": topic})  # CrewAI generates output
    print("✅ CrewAI execution complete.")

    # Convert CrewOutput to Markdown string
    result_text = str(result)  # ✅ Extract raw markdown text

    # ✅ Convert Markdown to HTML with fenced code blocks
    html_content = markdown.markdown(result_text, extensions=["fenced_code"])

    # Load HTML template
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders in the template
    final_html = template.replace("{{topic}}", topic).replace("{{title}}", topic).replace("{{content}}", html_content)

    # Save the final HTML file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ Blog saved to: {output_path}")

except Exception as e:
    print(f"❌ ERROR: CrewAI execution failed: {e}")
    exit(1)