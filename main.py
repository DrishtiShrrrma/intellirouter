
from routers import primary_router, secondary_router, department_router
from system_messages import department_messages
from utils import openrouter_completion, colored_text

def run_assistant():
    print(colored_text("Welcome to MegaMart Customer Service!", "cyan"))

    while True:
        user_input = input(colored_text("How can I assist you today? (Type 'exit' to quit): ", "cyan"))
        if user_input.lower() == 'exit':
            print(colored_text("Thank you for choosing MegaMart. Have a great day!", "cyan"))
            break

        # Route the query to the appropriate model
        model = primary_router(user_input)

        # Select system message based on model or department
        if model == "llama3-70b-8192":
            system_message = secondary_router(user_input, model="code")
        elif model == "llama-3.1-70b-versatile":
            system_message = secondary_router(user_input, model="complex")
        elif model == "gemma-7b-it":
            system_message = secondary_router(user_input, model="simple")
        else:
            department = department_router(user_input)
            system_message = department_messages.get(department, "General customer service.")
            print(colored_text(f"Connecting you to {department.replace('_', ' ').title()} department.", "yellow"))

        # Generate response
        response = openrouter_completion(model, user_input, system_message)
        print(colored_text("Assistant:", "green"), response)
        print()  # Blank line for readability

if __name__ == "__main__":
    run_assistant()

