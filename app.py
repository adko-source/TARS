import pandas as pd

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
        locals()[x] = cell_value  
        print(x)

  # Adjust the variable name as needed

# df_id = df["Line ID"]
# print(df_id)

# line_id_first_row = df.loc[0, "Line ID"]
# print(line_id_first_row)

# text_second_row = df.loc[1, "Text"]
# print(text_second_row)

# for index in df.iterrows():
#     print(df.loc[index, "Line ID"])