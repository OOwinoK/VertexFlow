import os
import vertexai
from dotenv import load_dotenv
from vertexai.generative_models import GenerativeModel

# Load variables from .env into the system environment
load_dotenv()

# Retrieve variables
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
LOCATION = os.getenv("GCP_REGION")

def initialize_app():
    """Initializes the Vertex AI SDK using environment variables."""
    if not PROJECT_ID:
        raise ValueError("GCP_PROJECT_ID not found in .env file")
    
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    return GenerativeModel("gemini-1.5-flash")

def main():
    try:
        model = initialize_app()
        response = model.generate_content("What is the benefit of using environment variables in AI apps?")
        
        print(f"Project: {PROJECT_ID}")
        print(f"Model Output: {response.text}")
        
    except Exception as e:
        print(f"Configuration Error: {e}")

if __name__ == "__main__":
    main()