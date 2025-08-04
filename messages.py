import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define valid messages (system role hata diya gaya hai)
messages = [
    {"role": "user", "parts": ["You are a helpful assistant. Tell me about LangChain."]}
]

# Generate response
response = model.generate_content(messages)

# Append AI response
messages.append({"role": "model", "parts": [response.text]})

# Print messages
for msg in messages:
    print(f"{msg['role'].capitalize()}: {msg['parts'][0]}")
