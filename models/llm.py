import os
from dotenv import load_dotenv
from models.config.mistral import get_mistral_model, test_mistral_connection
from models.config.huggingface import get_huggingface_model, test_huggingface_connection, list_recommended_models as list_hf_models
from models.config.openai import get_openai_model, test_openai_connection, list_recommended_models as list_openai_models

# Load environment variables
load_dotenv()

def get_model(model_type="mistral", test=False):
    """
    Returns the configured LLM model based on user selection.
    Falls back to Mistral if the selected model's connection test fails.
    
    Parameters:
    - model_type: Type of model to use (mistral, huggingface, openai)
    - test: If True, run a connection test before returning the model
    
    Returns:
    - (client, model_name): Tuple containing the client instance and model name
    """
    # First check if Mistral would work as a fallback
    mistral_viable = True
    if test and model_type != "mistral":
        # Silently test Mistral connection without printing messages
        try:
            mistral_api_key = os.getenv("MISTRAL_API_KEY")
            if not mistral_api_key:
                mistral_viable = False
        except:
            mistral_viable = False

    # Try the selected model type
    if model_type == "mistral":
        # Optionally test the connection
        if test:
            test_result = test_mistral_connection()
            if not test_result:
                print("⚠️ Warning: Mistral connection test failed.")
                return None, None
        
        # Return the model
        return get_mistral_model()
    
    elif model_type == "huggingface":
        # List recommended models if in test mode
        if test:
            list_hf_models()
            test_result = test_huggingface_connection()
            if not test_result:
                print("⚠️ Warning: Hugging Face connection test failed.")
                if mistral_viable:
                    print("🔄 Falling back to Mistral API...")
                    return get_model("mistral", test=True)
                else:
                    print("❌ Cannot fall back to Mistral API (key missing or invalid).")
                    return None, None
        
        # Return the model
        return get_huggingface_model()
    
    elif model_type == "openai":
        # List recommended models if in test mode
        if test:
            list_openai_models()
            test_result = test_openai_connection()
            if not test_result:
                print("⚠️ Warning: OpenAI connection test failed.")
                if mistral_viable:
                    print("🔄 Falling back to Mistral API...")
                    return get_model("mistral", test=True)
                else:
                    print("❌ Cannot fall back to Mistral API (key missing or invalid).")
                    return None, None
        
        # Return the model
        return get_openai_model()
    
    else:
        raise ValueError(f"❌ Unsupported model type: {model_type}")