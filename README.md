Generative AI Chatbot with Conversation Memory

A Python-based Generative AI chatbot developed as part of Generative AI Project 1. The chatbot uses Ollama with the Llama 3.2 model and maintains conversation history so that it can use information from earlier messages.

Project Objective

The main objective of this project is to understand how a conversational AI system maintains state and context during a conversation.

The chatbot:

Connects a Python application to an LLM
Accepts user messages
Stores conversation history
Stores both user and AI messages
Sends previous conversation context to the model
Maintains memory during the current session
Uses FIFO/sliding-window memory management
Technologies Used
Python 3.10
Ollama
Llama 3.2
Python Ollama Library
Visual Studio Code
PowerShell
Project Structure
GenerativeAI_Project1/
│
├── chatbot_ollama.py
├── chatbot_openai.py
└── README.md
chatbot_ollama.py

This is the working chatbot implementation.

It uses Ollama and Llama 3.2 to generate responses and maintains conversation memory.

chatbot_openai.py

This is an additional implementation using the OpenAI Python SDK.

During development, the OpenAI API returned a 429 insufficient_quota error because the API account had no available API balance. The working demonstration therefore uses the Ollama implementation.

How the Chatbot Works

The chatbot follows this process:

User Input
     ↓
Input Validation
     ↓
Store User Message
     ↓
Send Conversation History to LLM
     ↓
Generate AI Response
     ↓
Store AI Response
     ↓
Apply FIFO Memory Limit
     ↓
Display Response
Conversation Memory

The chatbot maintains an in-memory list:

conversation_history = []

When the user sends a message, it is added to the history:

conversation_history.append({
    "role": "user",
    "content": user_input
})

After the AI generates a response, the response is also added:

conversation_history.append({
    "role": "assistant",
    "content": ai_response
})

This allows the chatbot to use previous messages as context.

FIFO / Sliding-Window Memory

The project limits the amount of conversation stored in memory:

MAX_HISTORY = 10

When the limit is exceeded, the oldest message is removed:

while len(conversation_history) > MAX_HISTORY:
    conversation_history.pop(0)

This keeps the most recent conversation available to the model.

Example
You: My favorite color is purple.


AI: That's a nice choice!


You: What is my favorite color?


AI: You mentioned earlier that your favorite color is purple.

This demonstrates the chatbot's conversation-memory functionality.

Input Validation

The chatbot checks whether the user has entered an empty message.

Example:

You:


Please enter a message.
Exit Command

The chatbot can be stopped by entering:

exit

Example:

You: exit


Chatbot stopped. Goodbye!
Testing

The chatbot was tested for:

Test	Result
Chatbot starts successfully	Passed
User name memory	Passed
Favorite color memory	Passed
Empty input handling	Passed
Exit command	Passed
Conversation history	Passed
FIFO/sliding-window memory	Implemented
How to Run
1. Install Ollama

Install Ollama on your computer and make sure it is running.

2. Install the Python library

Open the terminal and run:

pip install ollama
3. Make sure the model is available
ollama list

The project uses:

llama3.2
4. Run the chatbot
python chatbot_ollama.py
Important Note

The chatbot's conversation memory is in-memory, which means the history is maintained during the current session. It is not stored permanently in a database.

Conclusion

This project demonstrates the basic architecture of a stateful Generative AI chatbot. The implementation connects Python with an LLM, maintains conversation history, preserves context between messages, validates user input, and uses FIFO memory management to control the size of the active conversation history.

How to put this on GitHub

Since you're already on your repository page:

Click README.md
Click the pencil ✏️ Edit button
Select all the existing text
Delete it
Paste the README above
Scroll down
Click Commit changes

After that, your GitHub page will look much more like a proper project submission rather than just a folder containing code.
