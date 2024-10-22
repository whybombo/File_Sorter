import os
import shutil
import logging
import tkinter as tk
from tkinter import filedialog, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Setup logging
logging.basicConfig(filename='file_sorter.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Folder paths and file types
folder_paths = {
    'code_files': ['.py', '.js', '.java', '.cpp', '.html', '.css', '.csv', '.sh'],
    'image_files': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.tiff', '.tmp'],
    'text_files': ['.txt', '.md', '.pdf', '.docx', '.pptx'],
    'archive_files': ['.zip', '.tar', '.rar', '.gz', '.7z'],
    'video_files': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'audio_files': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
}

# SORTER
class DownloadHandler(FileSystemEventHandler):
    def __init__(self, keywords):
        self.keywords = keywords

    def on_modified(self, event):
        file_names = os.listdir(downloads_path)
        for file in file_names:
            self.organize_by_keyword(file)

    def organize_by_keyword(self, file):
        moved = False
        for keyword in self.keywords:
            if keyword in file:
                source = os.path.join(downloads_path, file)
                destination = os.path.join(documents_path, file)
                try:
                    if os.path.exists(source) and not os.path.exists(destination):
                        shutil.move(source, destination)
                        logging.info(f"Moved: {file} to {documents_path}")
                        moved = True
                        break
                except Exception as e:
                    logging.error(f"Error moving file {file}: {e}")

        if not moved:
            logging.warning(f"No suitable folder for file: {file}")

# GUI for selecting paths and organizing files
class FileSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sorter")

        # Downloads path label and button
        self.downloads_label = tk.Label(root, text="Downloads Path:")
        self.downloads_label.pack()
        self.downloads_entry = tk.Entry(root, width=50)
        self.downloads_entry.pack()
        self.downloads_button = tk.Button(root, text="Browse", command=self.select_downloads_folder)
        self.downloads_button.pack()

        # Documents path label and button
        self.documents_label = tk.Label(root, text="Documents Path:")
        self.documents_label.pack()
        self.documents_entry = tk.Entry(root, width=50)
        self.documents_entry.pack()
        self.documents_button = tk.Button(root, text="Browse", command=self.select_documents_folder)
        self.documents_button.pack()

        # Heading for keyword entry
        self.keyword_heading = tk.Label(root, text="Enter Keywords (comma separated, no spaces):")
        self.keyword_heading.pack()

        # Keyword entry
        self.keyword_entry = tk.Entry(root, width=50)
        self.keyword_entry.pack()

        # Start sorting button
        self.start_button = tk.Button(root, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

        # Quit button
        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.pack()

    def select_downloads_folder(self):
        path = filedialog.askdirectory()
        self.downloads_entry.delete(0, tk.END)
        self.downloads_entry.insert(0, path)

    def select_documents_folder(self):
        path = filedialog.askdirectory()
        self.documents_entry.delete(0, tk.END)
        self.documents_entry.insert(0, path)

    def start_sorting(self):
        global downloads_path, documents_path
        downloads_path = self.downloads_entry.get() or downloads_path
        documents_path = self.documents_entry.get() or documents_path
        
        # Get keywords from entry, split by comma and strip spaces
        self.keywords = [keyword.strip().lower() for keyword in self.keyword_entry.get().split(',') if keyword]

        # Set up the file observer
        event_handler = DownloadHandler(self.keywords)
        self.observer = Observer()
        self.observer.schedule(event_handler, downloads_path, recursive=False)
        self.observer.start()
        logging.info("Monitoring started...")
        messagebox.showinfo("Info", "File sorting has started!")

        try:
            while True:
                self.root.update()
        except KeyboardInterrupt:
            self.observer.stop()
            self.observer.join()

    def quit_app(self):
        if hasattr(self, 'observer'):
            self.observer.stop()
            self.observer.join()
        self.root.quit()

# Setup Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = FileSorterApp(root)
    root.mainloop()
