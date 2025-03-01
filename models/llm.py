import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables
load_dotenv()

def get_mistral_model():
    """Returns a configured Mistral AI model instance using the latest API client."""
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("❌ MISTRAL_API_KEY is missing. Please add it to your .env file.")

    # Ensure provider is included
    provider = "mistral"
    model = f"{provider}/mistral-large-latest"  # ✅ Now passing "mistral/mistral-large-latest"

    # Create Mistral client instance
    client = Mistral(api_key=api_key)
    return client, model  # ✅ Now returns a valid provider/model format

def get_model(model_type="mistral"):
    """
    Returns the configured LLM model based on user selection.
    Default: Mistral
    """
    if model_type == "mistral":
        return get_mistral_model()
    else:
        raise ValueError(f"❌ Unsupported model type: {model_type}")
