import random

responses = [
    "Hello, how can I help you?", 
    "What do you want to talk about?", 
    "I'm not sure what you mean.", 
    "Can you repeat that?", 
    "I'm sorry, I don't understand.", 
    "Goodbye!"
]

def get_response():
    return random.choice(responses)

def start_chatbot():
    print("Hello, I'm a chatbot. What do you want to talk about?")
    
    while True:
        user_input = input()
        response = get_response()
        print(response)

start_chatbot()
