﻿# TARS (Code Name)
# Tools 
-----
* Python 
* Pandas https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
* Excel
* Text-to-speech API (elevenlabs.io) https://elevenlabs.io/docs/api-reference/text-to-speech

# Description
------------
Extracts cell values from an Excel .xlsx file and utilizes them to call a text-to-speech API, generating audio files in bulk for voice lines.


# Instructions
1. Clone and open repository
2. Open terminal and cd into project directory
3. Enter `python -m venv venv` in terminal to create a virtual python environment. This installs packages to the local project only intsead of globally
4. Enter `venv\Scripts\activate` in terminal to activate the virtual environment
5. Enter `python -m pip install -r requirements.txt` in terminal to install dependencies
6. Add your elevenlabs API key to config.json file:
{
    "api_key": "<your_elevenlabs_api_key>"
}
7. Enter `python getvoices.py` in terminal to get available voices from API. This generates the voices.xlsx file
8. Add (or replace) an .xlsx file named 'lines.xlsx' in the 'unprocessed_files' folder
   * Please see 'lines_example.xlsx' for the required columns
   * Please see 'voices.xlsx' for the available voice actors that can be used in the API (voice_id and name)
9. Enter `python generatefiles.py` in the terminal to start project and generate audio files
10. Access the completed audio files in the 'speech_files' folder. These will be grouped by voice actor name
