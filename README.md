# FileSorter

## Description

FileSorter is a Python script designed to organize files within a specified directory into subfolders based on their file extensions. This tool helps keep your files organized by automatically moving them into predefined categories.

## Features

- Automatically creates subfolders if they do not already exist.
- Sorts files into the following categories:
  - **Code Files**: Includes programming and scripting files.
  - **Image Files**: Organizes various image formats.
  - **Text Files**: Sorts text documents and other related file types.
  - **Archive Files**: Groups compressed files.
  - **Video Files**: Categorizes video formats.
  - **Audio Files**: Organizes audio files.
- Can be automated to run automatically using Task Scheduler.

## Requirements

- Python 3.x
- Libraries:
  - `os`
  - `shutil`
  - `watchdog`

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure Python is installed on your machine.
4. Install the required dependencies:
   ```bash
   pip install watchdog

## Usage
1. Place the FileSorter.py script in the directory where you want to organize files.
2. Update the downloads_path and documents_path variables in the script to point to your respective folders.
3. Run the script using Python:
  '''bash
python FileSorter.py

## Automation (Windows Task Scheduler)

To automate the script using Windows Task Scheduler:

### Open Task Scheduler:

- Press `Win + R` and type `taskschd.msc`, then press Enter.

### Create a Basic Task:

1. Click **Create Basic Task** on the right panel.
2. Name the task (e.g., "File Sorter Automation").
3. Set the trigger (e.g., "Daily" or "Weekly") and the time you want the script to run.

### Action:

1. Select **Start a program**.
2. Browse to the Python executable (e.g., `python.exe`).
3. In the **Add arguments** field, enter the path to your script, e.g.:

   ```bash
   C:\path\to\FileSorter.py

## Customization

- Modify the folder_paths dictionary in the script to add more file categories or change the file extensions associated with each category.

