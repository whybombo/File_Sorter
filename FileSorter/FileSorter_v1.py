import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
documents_path = os.path.join(os.path.expanduser("~"), "Documents/AA-Unsorted")

# ~~~~~~ file types and path ~~~~~~
folder_paths = {
    'code_files': ['.py', '.js', '.java', '.cpp', '.html', '.css', '.csv', '.sh'],
    'image_files': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.tiff', '.tmp'],
    'text_files': ['.txt', '.md', '.pdf', '.docx', '.pptx'],
    'archive_files': ['.zip', '.tar', '.rar', '.gz', '.7z'],
    'video_files': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'audio_files': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
}
# ~~~~~~ ~~~~~~
class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_names = os.listdir(downloads_path)
        for file in file_names:
            moved = False
            for folder, extensions in folder_paths.items():
                if any(file.endswith(ext) for ext in extensions):
                    source = os.path.join(downloads_path, file)
                    destination = os.path.join(documents_path, folder, file)
                    if os.path.exists(source) and not os.path.exists(destination):
                        shutil.move(source, destination)
                        print(f"Moved: {file} to {folder}")
                        moved = True
                        break
            if not moved:
                print(f"No suitable folder for file: {file}")
# ~~~~~~ observer loop ~~~~~~
observer = Observer()
event_handler = DownloadHandler()
observer.schedule(event_handler, downloads_path, recursive=False)

observer.start()
print("Monitoring Downloads folder for new files...")

try:
    while True:
        pass  # Keep script running to monitor changes
except KeyboardInterrupt:
    observer.stop()

observer.join()
# ~~~~~~ ~~~~~~
