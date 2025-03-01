import os
from dotenv import load_dotenv
from models.config.mistral import get_mistral_model, test_mistral_connection
from models.config.huggingface import get_huggingface_model, test_huggingface_connection, list_recommended_models

# Load environment variables
load_dotenv()

def get_model(model_type="mistral", test=False):
    """
    Returns the configured LLM model based on user selection.
    
    Parameters:
    - model_type: Type of model to use (mistral, huggingface)
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
    
    elif model_type == "huggingface":
        # List recommended models if in test mode
        if test:
            list_recommended_models()
            test_result = test_huggingface_connection()
            if not test_result:
                print("⚠️ Warning: Hugging Face connection test failed, but proceeding with model initialization.")
        
        # Return the model regardless of test result
        return get_huggingface_model()
    
    else:
        raise ValueError(f"❌ Unsupported model type: {model_type}")