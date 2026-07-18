import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_email(prompt, tone):

    tone_instruction = {
        "Professional": "Use professional business language.",
        "Formal": "Use highly formal corporate language.",
        "Friendly": "Use warm and friendly language.",
        "Polite": "Use respectful and polite language.",
        "Confident": "Use confident and assertive language.",
        "Apologetic": "Express sincere apology professionally.",
        "Thankful": "Express gratitude professionally.",
        "Persuasive": "Use convincing and persuasive language."
    }

    final_prompt = f"""
    You are a professional business communication expert.

    Task:
    Generate a complete ready-to-send email.

    Tone:
    {tone}

    Special Tone Instruction:
    {tone_instruction.get(tone)}

    User Requirement:
    {prompt}

    Rules:

    1. Do not use placeholders.
    2. Do not write [Your Name] or [Company Name].
    3. Generate realistic content.
    4. Use proper business communication.
    5. Keep email between 150 and 250 words.
    6. Include:
       - Subject
       - Greeting
       - Email Body
       - Closing
    7. Return only the email.

    Output Format:

    Subject:

    Greeting:

    Body:

    Closing:
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    return response.text