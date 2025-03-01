import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables
load_dotenv()

def test_mistral_connection():
    """Tests the Mistral API connection and returns the result."""
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("❌ MISTRAL_API_KEY is missing.")
        return False

    # Initialize Mistral client
    try:
        print("🔄 Testing Mistral API connection...")
        with Mistral(api_key=api_key) as client:
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=[{"role": "user", "content": "Hello, Mistral!"}]
            )

        print("✅ Mistral API is working!")
        print("Response:", response.choices[0].message.content)
        return True

    except Exception as e:
        print("❌ Error reaching Mistral API:", e)
        return False

def get_mistral_model():
    """Returns a configured Mistral AI model instance using the latest API client."""
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("❌ MISTRAL_API_KEY is missing. Please add it to your .env file.")

    # Ensure provider is included for CrewAI compatibility
    provider = "mistral"
    model = f"{provider}/mistral-large-latest"  # Format for CrewAI/LiteLLM

    # Create Mistral client instance
    client = Mistral(api_key=api_key)
    return client, model