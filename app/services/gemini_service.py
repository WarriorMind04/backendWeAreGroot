from google import genai
from google.genai import types
from dotenv import load_dotenv

#load_dotenv()  # Load environment variables from a .env file
# Initialize client here once
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

IDIOM_SYSTEM_INSTRUCTION = """... (Your full System Instruction goes here) ..."""

def get_idiom_explanation(idiom_text: str) -> str:
    """
    Core function to call the Gemini API with the specialized system instruction.
    
    Args:
        idiom_text: The idiom submitted by the user.
        
    Returns:
        The generated explanation text from the model.
    """
    
    # Configuration with the defined system instruction
    config = types.GenerateContentConfig(
        system_instruction=IDIOM_SYSTEM_INSTRUCTION
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=config,
        contents=idiom_text
    )
    
    return response.text