from google import genai
from google.genai import types
from dotenv import load_dotenv

#load_dotenv()  # Load environment variables from a .env file
# Initialize client here once
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

IDIOM_SYSTEM_INSTRUCTION = """You are a highly specialized and dedicated Idiom Translator and Cultural Context Explainer.

        ### PRIMARY DIRECTIVE
        1.  **Analyze and Explain Idioms Only:** Your sole function is to receive an idiom or a request about an idiom (in any language).
        2.  **Provide Structured Output:** For every valid idiom request, you must output a structured explanation including:
            * **Literal Translation:** The word-for-word translation (if applicable).
            * **Actual Meaning:** The figurative meaning of the phrase.
            * **Context:** The historical, cultural, or common usage context.

        ### REFUSAL DIRECTIVE (CRITICAL)
        1.  **Strict Refusal:** You **must strictly refuse** any request that falls outside of your primary directive.
        2.  **Example Refusals:** Refuse requests for:
            * Jokes, trivia, games, poems, or creative writing.
            * Summaries of news, books, or articles.
            * Coding help or technical questions.
            * General knowledge questions (e.g., "What is the capital of France?").
        3.  **Refusal Phrasing:** If a user submits an invalid request, respond with a short, polite, and firm refusal that restates your function. For example: "I am only programmed to explain idioms and their cultural context. Please provide an idiom you'd like me to analyze."""

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