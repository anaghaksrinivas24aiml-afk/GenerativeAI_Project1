import ollama

print("=" * 50)
print("     MY GENERATIVE AI CHATBOT")
print("     Custom AI Chatbot with Memory")
print("=" * 50)
print("Type 'exit' to stop the chatbot.\n")

# Conversation memory
conversation_history = []

# Maximum number of messages stored in memory
MAX_HISTORY = 10

while True:
    user_input = input("You: ")

    # Exit command
    if user_input.lower().strip() == "exit":
        print("\nChatbot stopped. Goodbye!")
        break

    # Input validation
    if not user_input.strip():
        print("Please enter a message.\n")
        continue

    # Add user message to conversation history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    try:
        # Send conversation history to Ollama
        response = ollama.chat(
            model="llama3.2",
            messages=conversation_history
        )

        # Get AI response
        ai_response = response["message"]["content"]

        # Add AI response to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })

        # FIFO / sliding-window memory
        while len(conversation_history) > MAX_HISTORY:
            conversation_history.pop(0)

        # Display response
        print("AI:", ai_response)
        print()

    except Exception as e:
        print("Error:", e)
        print()