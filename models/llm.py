import os
from dotenv import load_dotenv
from models.config.mistral import get_mistral_model, test_mistral_connection

# Load environment variables
load_dotenv()

def get_model(model_type="mistral", test=False):
    """
    Returns the configured LLM model based on user selection.
    
    Parameters:
    - model_type: Type of model to use (mistral, huggingface, llama)
    - test: If True, run a connection test before returning the model
    
    Returns:
    - (client, model_name): Tuple containing the client instance and model name
    """
    if model_type == "mistral":
        # Optionally test the connection
        if test:
            test_result = test_mistral_connection()
            if not test_result:
                print("⚠️ Warning: Mistral connection test failed, but proceeding with model initialization.")
        
        # Return the model regardless of test result
        return get_mistral_model()
    elif model_type in ["huggingface", "llama"]:
        raise ValueError(f"❌ Model type '{model_type}' is not implemented yet.")
    else:
        raise ValueError(f"❌ Unsupported model type: {model_type}")