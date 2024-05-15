# TARS (Code Name)
# Tools 
-----
Python 
Pandas https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
Excel
Text-to-speech API (elevenlabs.io) https://elevenlabs.io/docs/api-reference/text-to-speech

# Description
------------
Extracts cell values from an Excel .xlsx file and utilizes them to call a text-to-speech API, generating audio files in bulk for voice lines.


# Instructions
1. Clone and open repository
2. Add your elevenlabs API key to config.json file:
{
    "api_key": "<your_elevenlabs_api_key>"
}
3. Add (or replace) an .xlsx file named 'lines.xlsx' in the 'unprocessed_files' folder
   * Please see 'lines_example.xlsx' for the required columns
   * Please see 'voices.xlsx' for the available voice actors that can be used in the API (voice_id and name)
4. Right-click 'app.exe' and click 'Reveal in File Explorer'
5. Double left-click app.exe
6. Access the completed audio files in the 'speech_files' folder
