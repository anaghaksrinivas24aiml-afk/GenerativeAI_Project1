from openai import OpenAI

client = OpenAI()

conversation_history = []

MAX_HISTORY = 10

print("My Generative AI Chatbot is starting!")
print("Type 'exit' to stop.")
print()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if not user_input.strip():
        print("Please enter a message.")
        continue

    # Add user message to memory
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=conversation_history
        )

        # Get AI response
        ai_response = response.output_text

        # Add AI response to memory
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })

        # Keep memory within the limit
        while len(conversation_history) > MAX_HISTORY:
            conversation_history.pop(0)

        print("AI:", ai_response)
        print()

    except Exception as e:
        print("Error:", e)
        print()