import pandas as pd
import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['api_key']

print(api_key)


print("app started!")

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

# df = pd.DataFrame(data)
# print(df)

excel_file_path = "Unprocessed Files/lines.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the DataFrame
# print(df)

for index, row in df.iterrows():
    for column in df.columns:
        cell_value = row[column]
        x = f"{column}: {cell_value}"  
        # locals()[x] = cell_value  
        print(x)

def display_voices(data):

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

    df = pd.DataFrame(voices)

    # Write the DataFrame to an Excel file
    df.to_excel('voices.xlsx', index=False)

    display_voices(response_json)
    
    return voices

# print(get_voices())

get_voices()



# print(get_voices())

payload = {
    "text": "<string>",
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

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)

  # Adjust the variable name as needed

# df_id = df["Line ID"]
# print(df_id)

# line_id_first_row = df.loc[0, "Line ID"]
# print(line_id_first_row)

# text_second_row = df.loc[1, "Text"]
# print(text_second_row)

# for index in df.iterrows():
#     print(df.loc[index, "Line ID"])