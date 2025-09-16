# Rule-Based Chatbot Example

import re
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()  # normalize input

    # --- RULES ---

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif re.search(r"how are (you|u)", user_input):
        return "I'm doing great! Thanks for asking. How about you?"

    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot 🤖."

    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a wonderful day!"

    else:
        return "Sorry, I don’t understand that. Can you rephrase?"

# --- CHAT LOOP ---
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)

    if "bye" in user_input.lower():
        break
