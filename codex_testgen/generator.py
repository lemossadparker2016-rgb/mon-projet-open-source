import os
import openai
from openai import OpenAI

def generate_tests(code_snippet: str, model: str = "gpt-4o") -> str:
    """
    Génère des tests unitaires pytest pour un extrait de code donné.
    """
    # Il est recommandé d'utiliser les variables d'environnement pour la clé API
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    prompt = f"""
    You are an expert Python developer. Write comprehensive pytest unit tests for the following Python code.
    Include edge cases and mock any external dependencies if necessary.
    Only return the Python code for the tests, no markdown formatting or extra text.

    Code to test:
    {code_snippet}
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful automated testing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2, # Température basse pour un code plus déterministe
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating tests: {str(e)}"
