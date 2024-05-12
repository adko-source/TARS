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
# def save_voices_to_file(data):

#     for voice in data['voices']:
#   # For each 'voice', the 'name' and 'voice_id' are printed out. 
#   # These keys in the voice dictionary contain values that provide information about the specific voice.
#         # print(f"{voice['name']}; {voice['voice_id']}")

#         with open('voices.txt', 'a') as file:
#     # Iterate over each voice dictionary in the list
           
#           file.write(f"{voice['name']}; {voice['voice_id']}\n")
    
#     return

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

    # save_voices_to_file(response_json)
    
    return voices

get_voices()




#call_text_to_speech_api(voice_id="2")

# response_text = call_text_to_speech_api(
#     voice_id="AZnzlk1XvdvUeBnXmlld",
#     text="Hello World",
#     model_id="eleven_monolingual_v1"
   
# )

# print(response_text)
# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)

  # Adjust the variable name as needed

# df_id = df["line_id"]
# print(df_id)

# line_id_first_row = df.loc[0, "Line ID"]
# print(line_id_first_row)

# text_second_row = df.loc[1, "Text"]
# print(text_second_row)

# for index in df.iterrows():
#     print(df.loc[index, "Line ID"])