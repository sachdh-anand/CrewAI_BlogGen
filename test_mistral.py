import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    print("❌ MISTRAL_API_KEY is missing.")
    exit(1)

# Initialize Mistral client
try:
    with Mistral(api_key=api_key) as client:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": "Hello, Mistral!"}]
        )

    print("✅ Mistral API is working!")
    print("Response:", response.choices[0].message.content)

except Exception as e:
    print("❌ Error reaching Mistral API:", e)
