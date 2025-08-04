import os
import google.generativeai as genai
from dotenv import load_dotenv
import transformers 

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

chat_history=[]

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Start chatbot loop
while True:
    user_input = input("you: ")
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break

    # Generate content using Gemini
    response = model.generate_content(chat_history)
    chat_history.append(response.content)
    # Print response from AI
    print("Ai:", response.text)  # .text gives plain string response

    print(chat_history)