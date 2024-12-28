from openai import OpenAI
from settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
# Set the OpenAI API key

def generate_response(system_prompt, user_input, examples=None, model="gpt-4o-mini"):
    """
    Generates a response from the OpenAI API.
    """
    messages = [{"role": "system", "content": system_prompt}]

    # Include few-shot examples if provided
    if examples:
        messages.append({"role": "user", "content": examples})

    messages.append({"role": "user", "content": user_input})

    # Call OpenAI API
    response = client.chat.completions.create(model=model,
    messages=messages,
    max_tokens=150,
    temperature=0.7)

    return response.choices[0].message.content.strip()
