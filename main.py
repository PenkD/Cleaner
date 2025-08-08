import os
import customtkinter as ctk
import shutil

FolderType = {
    (".jpg", ".png", ".gif", ".webp", ".jfif"): "Images",
    (".mp3", ".wav", ".ogg", ".wav", ".wma", ".3gp"): "Music",
    (".mp4", ".mov", ".avi"): "Videos",
    (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".csv", ".log", ".json", ".xml", ".yml", ".yaml", ".md", ".html", ".htm", ".ahk", ".js", ".css", ".ts", ".java", ".py", ".c", ".cpp", ".h", ".sh"): "Documents",
    (".exe", ".msi", ".cmd", ".bat", ".apk", ".com" ): "EXE-files",
    (".jar",): "JAR-files",
    (".zip", ".rar", ".gz", ".7z"): "Archives"
}

FolderNames = ["Music", "Videos", "EXE-files", "Documents", "Archives", "JAR-files"]

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("File Cleaner")
        self.maxsize(width=300, height=300)
        self.minsize(width=300, height=300)
        self.pathText = ctk.CTkEntry(self, width=300, height=20)
        self.pathText.place(x=0, y=50)
        self.console = ctk.CTkTextbox(self, width=300, height=100)
        self.console.place(x=0, y=100)
        self.console.configure(self, state="disabled")
        button1 = ctk.CTkButton(self, text="Launch", command=self.launcherCleaner)
        button1.place(x=85, y=210)

    def launcherCleaner(self):
        path = self.pathText.get()
        self.cleanUpDrive(path)

    def cleanUpDrive(self, path):
        if os.path.exists(path):
            for folder in FolderNames:
                os.makedirs(os.path.join(path, folder), exist_ok=True)
            self.console.configure(self, state="normal")
            self.console.insert("0.0", "Folders created or already exist\n")
            self.console.configure(self, state="disabled")
        else:
            self.console.configure(self, state="normal")
            self.console.insert("0.0", "Enter a valid path\n")
            self.console.configure(self, state="disabled")
            return

        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isdir(file_path):
                continue
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()

            for extensions, folder_name in FolderType.items():
                if ext in extensions:
                    target_folder = os.path.join(path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file_name))
                    self.console.configure(self, state="normal")
                    self.console.insert("end", f"Moved {file_name} to {folder_name}\n")
                    self.console.configure(self, state="disabled")
                    break

app = Main()
app.mainloop()
