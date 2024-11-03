

# **MegaMart Conversational Assistant**

The **MegaMart Conversational Assistant** is an AI-driven customer service tool designed to handle various queries related to an e-commerce platform. It dynamically routes user questions to different models based on complexity, query type, and department, ensuring that users receive accurate and contextually relevant responses. This project supports both a command-line interface (CLI) and a Streamlit web application.

## Table of Contents

- [Features](#features)
- [Tools and Models Used](#tools-and-models-used)
- [Workflow Diagram](#workflow-diagram)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Running the CLI](#running-the-cli)
  - [Running the Streamlit Web App](#running-the-streamlit-web-app)
- [Future Enhancements](#future-enhancements)
- [Additional Notes](#additional-notes)

---

## Features

- **Dynamic Model Routing**: Routes queries to the appropriate language model based on query complexity and type.
- **Department-Specific Customer Service**: Answers queries related to Electronics, Fashion, Home & Garden, and Books & Media.
- **Multi-Interface Support**: Provides both a CLI and a Streamlit-based web application for user interaction.
- **Context-Aware Responses**: Delivers personalized responses using system messages tailored to each query type and department.

---

## Tools and Models Used

- **Programming Language**: Python
- **Key Libraries**:
  - **LangChain**: Streamlines complex language model workflows.
  - **Groq**: Manages model integration and query routing.
  - **LangChain-Groq**: Combines LangChain with Groq to enable versatile model interaction.
  - **OpenAI API**: Provides access to various language models.
  - **Streamlit**: Builds a simple and interactive web interface for the assistant.
  - **Termcolor**: Adds color to terminal output, enhancing readability in the CLI.
- **Language Models**:
  - **Llama3-70b**:
    - **Llama3-70b-versatile**: For complex, in-depth queries.
    - **Llama3-70b-8192**: Specialized for code-related queries.
  - **Gemma-7b-it**: Optimized for handling simple, everyday conversational queries.

---

## Workflow Diagram

The following flowchart provides an overview of the assistant’s workflow, from receiving a user query to selecting the appropriate model, system message, and department (if applicable):

<img width="745" alt="image" src="https://github.com/user-attachments/assets/ada7a529-2a8c-4427-88d0-35607dd2bf26">

---

## Project Structure

```
MegaMart Conversational Assistant/
│
├── main.py                 # Command-line interface for the assistant
├── app.py                  # Streamlit app for a web-based interface
├── routers.py              # Routing functions for model and department selection
├── system_messages.py      # Predefined system messages for customer service departments
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/megacart-conversational-assistant.git
cd megacart-conversational-assistant
```

### Step 2: Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up API Keys

Set up your OpenAI and Groq API keys as environment variables:

```python
import os
os.environ['OPENAI_API_KEY'] = "your_openai_api_key"
os.environ['GROQ_API_KEY'] = "your_groq_api_key"
```

---

## Usage

### Running the CLI

To run the assistant in the command-line interface:

```bash
python main.py
```

After starting, you’ll see a welcome message from the assistant. Type your questions and press Enter. Type `exit` to end the session.

### Running the Streamlit Web App

To run the assistant in a web-based interface:

```bash
streamlit run app.py
```

This command will launch the Streamlit app, which will automatically open in the default web browser. Enter your question in the text box and click "Submit" to receive a response.

---

## Future Enhancements

- **Multilingual Support**: Detect and translate queries and responses for multilingual interaction.
- **Sentiment Analysis**: Adjust responses based on user sentiment to provide empathetic and relevant assistance.
- **Voice Interaction**: Add speech-to-text and text-to-speech capabilities for accessibility.
- **Enhanced Contextual Memory**: Allow the assistant to remember previous interactions for better continuity in responses.




