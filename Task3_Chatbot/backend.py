import requests
import json

GROQ_API_KEY = "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"  # Replace with your actual API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query_groq_api(user_input, chat_history):
    """Send user input along with chat history to Groq API"""
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    
    # Build conversation memory
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages.extend(chat_history)  # Add past messages
    messages.append({"role": "user", "content": user_input})  # Add new user input

    payload = {
        "model": "llama3-8b-8192",
        "messages": messages,
        "stream": True,  # Enable streaming
    }

    response = requests.post(GROQ_API_URL, json=payload, headers=headers, stream=True)

    if response.status_code != 200:
        yield f"Error: {response.json()}"  # Display error messages properly
        return

    full_response = ""  # Store full response
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8").replace("data: ", ""))
                if "choices" in data and data["choices"]:
                    chunk = data["choices"][0]["delta"].get("content", "")
                    full_response += chunk  # Append chunk to full response
                    yield chunk  # Stream chunk
            except json.JSONDecodeError:
                continue  # Skip malformed lines

    # ✅ Ensure only one final response is stored
    yield full_response
