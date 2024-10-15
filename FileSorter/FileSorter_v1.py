import os
import shutil

# Define the path to the folder containing the files to sort
path = r"Put your file path to use"
file_names = os.listdir(path)

# Define folder names and their corresponding file extensions
folder_paths = {
    'code_files': ['.py', '.js', '.java', '.cpp', '.html', '.css', '.csv', '.sh'],  
    'image_files': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.tiff'],      
    'text_files': ['.txt', '.md', '.pdf', '.docx', '.pptx'],                        
    'archive_files': ['.zip', '.tar', '.rar', '.gz', '.7z'],                        
    'video_files': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],                        
    'audio_files': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],                       
}

# Create the folders if they do not exist
for folder in folder_paths.keys():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

# Move the files into their corresponding folders
for file in file_names:
    moved = False
    for folder, extensions in folder_paths.items():
        if any(file.endswith(ext) for ext in extensions):
            destination = os.path.join(path, folder, file)
            if not os.path.exists(destination):
                shutil.move(os.path.join(path, file), destination)
                print(f"Moved: {file} to {folder}")
                moved = True
                break  
    if not moved and not folder_paths:
        print(f"No suitable folder for file: {file}") 
