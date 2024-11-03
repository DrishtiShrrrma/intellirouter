from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def openrouter_completion(model_name, user_query, system_message=None):
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": user_query})

    completion = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return completion.choices[0].message.content

def colored_text(text, color):
    # Adds color to text output for command line
    from termcolor import colored
    return colored(text, color)
