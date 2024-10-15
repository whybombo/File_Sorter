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

## Requirements

- Python 3.x
- Libraries:
  - `os`
  - `shutil`

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Make sure you have Python installed on your machine.

## Usage

1. Place the `FileSorter.py` script in the directory where you want to organize files.
2. Update the `path` variable in the script to point to the target folder.
3. Run the script using Python:

   ```bash
   python FileSorter.py
