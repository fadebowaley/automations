import pandas as pd

# Read the Excel file
excel_file = 'report.xlsx'
xls = pd.ExcelFile(excel_file)

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through sheet names and read each sheet into a DataFrame
for sheet_name in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name)
    data_frames.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_data = pd.concat(data_frames, ignore_index=True)

# Write the merged DataFrame back to a new Excel sheet
merged_excel_file = 'merged_file.xlsx'
merged_data.to_excel(merged_excel_file, index=False)
