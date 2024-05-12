import pandas as pd
import requests
import json

# Get API key from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['api_key']

print("app started!")


excel_file_path = "unprocessed_files/lines.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        x = f"{column}: {cell_value}"  
        # locals()[x] = cell_value  
        print(x)

def save_voices_to_file(data):

    for voice in data['voices']:
  # For each 'voice', the 'name' and 'voice_id' are printed out. 
  # These keys in the voice dictionary contain values that provide information about the specific voice.
        print(f"{voice['name']}; {voice['voice_id']}")

        with open('voices.txt', 'a') as file:
    # Iterate over each voice dictionary in the list
           
          file.write(f"{voice['name']}; {voice['voice_id']}\n")
    
    return

# Get the list of available voices from API
def get_voices():

    headers = {
        "Accept": "application/json",
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    url = "https://api.elevenlabs.io/v1/voices"

    response = requests.request("GET", url, params={"api_key": api_key}, headers=headers)

    response_json = response.json()

    voices = response_json["voices"]

    # Convert voices json into a DataFrame
    df = pd.DataFrame(voices)

    # Write the DataFrame to an Excel file
    df.to_excel('voices.xlsx', index=False)

    save_voices_to_file(response_json)
    
    return voices

get_voices()


def call_text_to_speech_api(voice_id, text, model_id):

    print(voice_id)
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    payload = {
        "text": text,
        "model_id": "<string>",
        "voice_settings": {
            "stability": 123,
            "similarity_boost": 123,
            "style": 123,
            "use_speaker_boost": True
        },
        "pronunciation_dictionary_locators": [
            {
                "pronunciation_dictionary_id": "<string>",
                "version_id": "<string>"
            }
        ],
        "seed": 123,
        "previous_text": "<string>",
        "next_text": "<string>",
        "previous_request_ids": ["<string>"],
        "next_request_ids": ["<string>"]
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    
    # print(response.text)
    return response.text

#call_text_to_speech_api(voice_id="2")

response_text = call_text_to_speech_api(
    voice_id="AZnzlk1XvdvUeBnXmlld",
    text="Hello World",
    model_id="eleven_monolingual_v1"
   
)

print(response_text)
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