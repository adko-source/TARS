import json  # Used for working with JSON data
import pandas as pd # Used for working with Excel data in Python
import requests  # Used for making HTTP requests

# Get API key from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['api_key']

XI_API_KEY = api_key

# Get the list of available voices from API
def get_voices():

    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY,
        "Content-Type": "application/json"
    }

    url = "https://api.elevenlabs.io/v1/voices"

    response = requests.request("GET", url, params={"api_key": api_key}, headers=headers)

    response_json = response.json()

    voices = response_json["voices"]
    
    # Convert voices json into a DataFrame
    df = pd.DataFrame(voices)

    # Save the available voices returned from the api to an Excel file
    df.to_excel('voices.xlsx', index=False)
    
    return voices

get_voices()