import os
import shutil
from datetime import date
import tkinter as tk
from tkinter import filedialog
import webbrowser
from tqdm import tqdm

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Prompt the user to select a source folder using a file dialog
source_folder = filedialog.askdirectory(title="Select the source folder")

# Prompt the user to select a destination folder using a file dialog
destination_folder = filedialog.askdirectory(title="Select the destination folder")

# Create a folder with the current date in the destination folder
current_date = date.today().strftime("%Y-%m-%d")
folder_path = os.path.join(destination_folder, current_date)
os.makedirs(folder_path)

# Prompt the user to enter the name for the subfolder
subfolder_name = input("Enter the name for the subfolder: ")

# Create a subfolder with the user-provided name inside the date folder
subfolder_path = os.path.join(folder_path, subfolder_name)
os.makedirs(subfolder_path)

# Get the total number of files in the source folder
file_count = sum([1 for file_name in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, file_name))])

# Copy files from the selected source folder to the subfolder,
# renaming them with the system date + existing name
for file_name in tqdm(os.listdir(source_folder), total=file_count, desc='Copying files'):
    file_path = os.path.join(source_folder, file_name)
    if os.path.isfile(file_path):
        new_file_name = f"{current_date}_{file_name}"
        new_file_path = os.path.join(subfolder_path, new_file_name)
        shutil.copy2(file_path, new_file_path)

# Open Safari and navigate to Vimeo.com
webbrowser.get("safari").open("https://vimeo.com")
