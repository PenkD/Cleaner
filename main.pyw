import os
import customtkinter as ctk
import shutil

FolderType = {
    (".jpg", ".png", ".gif", ".webp", ".jfif", ".jpeg"): "Images",
    (".jpg", ".png", ".gif", ".webp", ".jfif"): "Images",
    (".mp3", ".wav", ".ogg", ".wav", ".wma", ".3gp"): "Music",
    (".mp4", ".mov", ".avi", ".mkv"): "Videos",
    (".mp4", ".mov", ".avi"): "Videos",
    (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".csv", ".log", ".json", ".xml", ".yml", ".yaml", ".md", ".html", ".htm", ".ahk", ".js", ".css", ".ts", ".java", ".py", ".c", ".cpp", ".h", ".sh"): "Documents",
    (".exe", ".msi", ".cmd", ".bat", ".apk", ".com" ): "Executables",
    (".jar",): "JARs",
    (".zip", ".rar", ".gz", ".7z", ".iso"): "Archives"
}

FolderNames = ["Music", "Videos", "Executables", "Documents", "Archives", "JARs"]

class Main(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("File Cleaner")
        self.maxsize(width=300, height=300)
        self.minsize(width=300, height=300)
        ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("Themes\lavender.json")
        self.pathText = ctk.CTkEntry(self, width=300, height=20)
        self.pathText.insert("0", "Enter address here")
        self.pathText.place(x=0, y=50)
        self.console = ctk.CTkTextbox(self, width=300, height=100)
        self.console.place(x=0, y=100)
        self.console.insert("0.0", "Output\n")
        self.console.configure(self, state="disabled")
        button1 = ctk.CTkButton(self, text="Clean Directory", command=self.launcherCleaner)
        button1.place(x=85, y=210)
        themeButton = ctk.CTkButton(self, text="Switch Theme", command=self.next_theme) # delete this if you want to remove themes for a more portable experience. Delete the line below this
        themeButton.place(x=85, y=250) # delete this if you're going to delete the line above this
        self.themes = ["Themes\metal.json", "Themes\marsh.json", "Themes\lavender.json"]
        self.theme_index = 0

    def build_ui(self):
        self.pathText = ctk.CTkEntry(self, width=300, height=20)
        self.pathText.insert(0, "Enter address here")
        self.pathText.place(x=0, y=50)

        self.console = ctk.CTkTextbox(self, width=300, height=100)
        self.console.place(x=0, y=100)
        self.console.insert("0.0", "Output\n")
        self.console.configure(state="disabled")

        button1 = ctk.CTkButton(self, text="Clean Directory", command=self.launcherCleaner)
        button1.place(x=85, y=210)

        button2 = ctk.CTkButton(self, text="Switch Theme", command=self.next_theme)
        button2.place(x=85, y=250)

    def next_theme(self):

        self.theme_index = (self.theme_index + 1) % len(self.themes)
        new_theme = self.themes[self.theme_index]


        ctk.set_default_color_theme(new_theme)
        for widget in self.winfo_children():
            widget.destroy()
        self.build_ui()

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
