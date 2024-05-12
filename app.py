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



url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

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

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

  # Adjust the variable name as needed

# df_id = df["Line ID"]
# print(df_id)

# line_id_first_row = df.loc[0, "Line ID"]
# print(line_id_first_row)

# text_second_row = df.loc[1, "Text"]
# print(text_second_row)

# for index in df.iterrows():
#     print(df.loc[index, "Line ID"])