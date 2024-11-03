import json
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

def primary_router(user_input):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": """
                Decide the route:
                {"route": "route_name"}
                Options:
                - "llama-3.1-70b-versatile" for complex queries
                - "llama3-70b-8192" for code queries
                - "gemma-7b-it" for simple conversations
                """},
            {"role": "user", "content": user_input}
        ]
    )
    return json.loads(response.choices[0].message.content)["route"]

def secondary_router(user_input, model="complex"):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": """Choose system message based on query context."""},
            {"role": "user", "content": user_input}
        ]
    )
    return json.loads(response.choices[0].message.content)["system_message"]

def department_router(user_input):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": """Route to customer service department."""},
            {"role": "user", "content": user_input}
        ]
    )
    return json.loads(response.choices[0].message.content)["department"]
