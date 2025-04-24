import requests

class ConversationalAgent:
    def __init__(self):
        # Set up the API details here
        self.api_host = "chatgpt-42.p.rapidapi.com"
        self.api_key = "c591e3f981mshd09523bc19615a5p10749djsn16fc9a597cfe"
        self.url = "https://chatgpt-42.p.rapidapi.com/aitohuman"

    def get_ai_response(self, user_input: str) -> str:
        # Fallback responses for certain inputs
        if user_input.lower() in ["hello", "hi", "hey"]:
            return "Hi there! How can I assist you today?"
        
        elif user_input.lower() in ["how are you", "how's it going", "what's up"]:
            return "I'm doing well, thank you for asking! How about you?"

        # If the input doesn't match a fallback, call the API
        payload = {"text": user_input}
        headers = {
            "Content-Type": "application/json",
            "x-rapidapi-host": self.api_host,
            "x-rapidapi-key": self.api_key
        }

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            if response.status_code == 200:
                result = response.json()
                return result.get("text", "Sorry, I couldn't understand that.")
            else:
                return f"API error: {response.status_code}"

        except Exception as e:
            return f"Error: {str(e)}"
