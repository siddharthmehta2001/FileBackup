import os
import shutil
from datetime import date
from tkinter import Tk, filedialog, simpledialog, messagebox
import webbrowser
from tqdm import tqdm
import platform

# Set the fixed destination folder path
destination_folder = "/Volumes/SOM_Techroom_May_2023/Acting Classes"

# Create a Tkinter window
root = Tk()
root.withdraw()

# Display a message dialog to the user
messagebox.showinfo("Message", "Now please select the source folder.")

# Prompt the user to select a source folder using a file dialog
source_folder = filedialog.askdirectory(title="Select the source folder")

# Create a folder with the current date in the destination folder
current_date = date.today().strftime("%Y-%m-%d")
folder_path = os.path.join(destination_folder, current_date)

try:
    # Attempt to create the folder
    os.makedirs(folder_path)
except FileExistsError:
    # Handle the case when the folder already exists
    pass

# Prompt the user to enter the name for the subfolder using a dialog box
subfolder_name = simpledialog.askstring("Subfolder Name", "Enter the name for the subfolder:")
if subfolder_name is None or subfolder_name.strip() == "":
    messagebox.showinfo("Error", "Invalid subfolder name. Exiting.")
    exit()

subfolder_path = os.path.join(folder_path, subfolder_name)

try:
    # Attempt to create the subfolder
    os.makedirs(subfolder_path)
except FileExistsError:
    # Handle the case when the subfolder already exists
    pass

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

# Open Chrome and navigate to Vimeo.com in the same user session
if platform.system() == "Darwin":
    script = f'tell application "Google Chrome" to make new tab at end of tabs of window 1 with properties {{URL:"https://vimeo.com/home"}}'
    os.system(f"osascript -e '{script}'")
else:
    webbrowser.get("chrome").open("https://vimeo.com/home")
