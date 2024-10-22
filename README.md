# FileSorter

## Description

FileSorter is a Python script that organizes files within a specified directory into subfolders based on keywords. If you are looking for a more automatic approach, this tool helps keep your files organized by automatically moving them into pre-defined folders using Task Scheduler once a file is downloaded.

## Features

- Sorts files into a designated documents folder based on keywords the user enters.
- Allows the input of multiple keywords separated by commas (no spaces).
- Automatically creates subfolders if they do not already exist.
- It supports a GUI for selecting downloads and document paths.
- Includes a quit button to exit the application easily.

## Requirements

- Python 3.x
- Libraries:
  - `os`
  - `shutil`
  - `logging`
  - `tkinter`
  - `watchdog`

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure Python is installed on your machine.
4. Install the required dependencies:
   ```bash
   pip install watchdog
   ```

## Usage

1. Place the `FileSorter.py` script in the directory where you want to organize files.
2. Run the script using Python:
   ```bash
   python FileSorter.py
   ```
3. In the GUI, specify the Downloads and Documents paths.
4. Enter keywords (separated by commas) for sorting.
5. Click **Start Sorting** to begin organizing files based on the specified keywords.
6. Click **Quit** to exit the application.

## Automation ONLY for file extension and predetermined files - will be created automatically(Windows Task Scheduler)

To automate the script using Windows Task Scheduler:

### Open Task Scheduler:

- Press `Win + R`, type `taskschd.msc`, then press Enter.

### Create a Basic Task:

1. Click **Create Basic Task** on the right panel.
2. Name the task (e.g., "File Sorter Automation").
3. Set the trigger (e.g., "Daily" or "Weekly") and the time you want the script to run.

### Action:

1. Select **Start a program**.
2. Browse to the Python executable (e.g., `python.exe`).
3. In the **Add arguments** field, enter the path to your script, e.g.:
   ```bash
   C:\path\to\FileSorter_v1.py
   ```
![image](https://github.com/user-attachments/assets/6ba86760-7df3-489d-ad8a-c884cc02bc63)


## Customization

- Modify the `folder_paths` dictionary in the script to add more file categories or change the keywords associated with each category.
