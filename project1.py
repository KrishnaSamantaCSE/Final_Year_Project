import os
import pandas as pd
from fpdf import FPDF

# Specify the folder path
folder_path = "D:/FINAL YEAR PROJECT/part1"

# Get all file names in the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Sort file names numerically based on the first part of the file name (Age)
file_names.sort(key=lambda x: int(x.split('_')[0]))

# Initialize lists to store Age, Gender, Race, and File Path
ages, genders, races, file_paths = [], [], [], []

# Extract Age, Gender, Race, and full file path from each file name
for file_name in file_names:
    parts = file_name.split('_')  # Split by underscore ''
    
    if len(parts) >= 3:
        age = parts[0]               # First part is Age
        gender = parts[1]            # Second part is Gender
        race = parts[2].split('.')[0]  # Third part is Race, remove file extension
    
        # Append to respective lists
        ages.append(age)
        genders.append(gender)
        races.append(race)
        file_paths.append(os.path.join(folder_path, file_name))  # Full path of the file

# Create a DataFrame
data = {
    "Age": ages,
    "Gender": genders,
    "Race": races,
    "File Path": file_paths
}
df = pd.DataFrame(data)

# Save to Excel file
output_excel = "part1.xlsx"
df.to_excel(output_excel, index=False)

print(f"Excel file created successfully: {output_excel}")