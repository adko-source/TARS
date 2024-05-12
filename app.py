import pandas as pd # Used for working with Excel data in Python
import requests  # Used for making HTTP requests
import json  # Used for working with JSON data

# Get API key from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['api_key']

# Define constants
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = api_key  # Your API key for authentication
OUTPUT_PATH = "output.mp3"  # Path to save the output audio file

print("app started!")

excel_file_path = "unprocessed_files/lines.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        x = f"{column}: {cell_value}"  
        # locals()[x] = cell_value  
        # print(x)
def call_text_to_speech_api(voice_id, text):

    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
    }
     
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8,
        "style": 0.0,
        "use_speaker_boost": True
        }
    }
   
    response = requests.request("POST", url, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.ok:
        
        # Open the output file in write-binary mode
        with open(OUTPUT_PATH, "wb") as f:
            # Read the response in chunks and write to the file
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        # Inform the user of success
        print("Audio stream saved successfully.")
    else:
        # Print the error message if the request was not successful
        print(response.text)
        
    return response.text

response_text = call_text_to_speech_api(
    voice_id="5Q0t7uMcjvnagumLfvZi",
    text="Hello Ryan"
    )    

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
