"CHATBOT PROJECT"
import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting responses
    if re.search(r'hello|hi|hey', user_input):
        return "Hello! How can I help you today?"
    
    # Asking for the bot's name
    elif re.search(r'what is your name|who are you', user_input):
        return "I am a simple rule-based chatbot created to assist you."

    # Farewell responses
    elif re.search(r'bye|goodbye|see you', user_input):
        return "Goodbye! Have a great day!"

    # Inquiries about the weather
    elif re.search(r'weather|temperature', user_input):
        return "I can't check the weather right now, but you can use a weather app or website."

    # Asking about the bot's purpose
    elif re.search(r'what can you do|what do you do', user_input):
        return "I can answer simple questions and have basic conversations with you."

    # Catch-all response for unknown queries
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Function to start the chatbot
def start_chatbot():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
start_chatbot()
