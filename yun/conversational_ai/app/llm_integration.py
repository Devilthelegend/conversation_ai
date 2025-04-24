import httpx
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class LLMIntegration:
    def __init__(self, model="runwayml"):
        self.model = model
        self.config = self.load_config()

    def load_config(self):
        # Configuration for connecting to the RapidAPI service
        config = {
            "runwayml": {
                "api_key": "c591e3f981mshd09523bc19615a5p10749djsn16fc9a597cfe",  
                "host": "runwayml.p.rapidapi.com"  
            }
        }
        return config

    async def get_response(self, user_message: str):
        if self.model == "runwayml":
            return await self.runwayml_chat(user_message)
        else:
            raise ValueError("Unsupported model")

    async def runwayml_chat(self, user_message: str):
        url = "https://runwayml.p.rapidapi.com/status"  # Correct API endpoint
        headers = {
            "X-RapidAPI-Key": self.config["runwayml"]["api_key"],  # Your RapidAPI key
            "X-RapidAPI-Host": self.config["runwayml"]["host"]  # The correct host URL
        }

        # UUID you provided
        querystring = {"uuid": "2858de6f-364c-481e-988a-b930af469aa9"}

        logging.debug(f"Making request to URL: {url} with headers: {headers} and query: {querystring}")
        
        # Making the request asynchronously with httpx
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=querystring)

        logging.debug(f"Response status code: {response.status_code}")
        logging.debug(f"Response text: {response.text}")

        # Handle the response
        if response.status_code == 200:
            response_data = response.json()
            logging.debug(f"API Response: {response_data}")
            return "AI Response: " + response_data.get("message", "No response available.")
        else:
            logging.error(f"Error with API request: {response.status_code} - {response.text}")
            raise Exception(f"Error with API request: {response.status_code} - {response.text}")
