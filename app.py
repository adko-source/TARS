import pandas as pd

print("app started!")



data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)
print(df)

excel_file_path = "Unprocessed Files/lines.xlsx"

# Read the Excel file into a DataFrame
lines = pd.read_excel(excel_file_path)

# Display the DataFrame
print(lines)

for index, row in lines.iterrows():
    for column in lines.columns:
        cell_value = row[column]
        # Do something with the cell value (e.g., save it to a variable)
        variable_name = f"{column}_{index}"  # Example variable name
        locals()[variable_name] = cell_value  # Save value to a variable