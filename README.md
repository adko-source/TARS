# TARS
Tools 
-----
Python https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
Excel
Text-to-speech API (elevenlabs.io) https://elevenlabs.io/docs/api-reference/text-to-speech


Requirements
------------
Can read Excel files within an 'Unprocessed Files' folder

Excel file should contain some required columns such as the text needed and other columns
such as the voice used. Also set unique id for each roq

Use python to get the data from each Excel

Transform and send the data from the Excel spreadsheet to the elevenlabs.io API

Save the response from the API to an .mp3 file and output it to a 'Processed Files' folder

Naming convention: name output files in way that can be easily referenced in the Excel file. 
For example <id>_<voice_type>_<type(ai)>_line

# Running Project

cd into project folder

Open a new terminal and enter:
pip install -r requirements.txt

To start project 
python app.py -arg1
 