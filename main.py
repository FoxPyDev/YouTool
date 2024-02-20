import customtkinter
from tkinter import filedialog
import json
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x800")
        self.title("YouTool")
        self.logo = customtkinter.CTkImage(dark_image=Image.open('./LOGO.png'), size=(600, 150))
        self.logo_lable = customtkinter.CTkLabel(self, text="", image=self.logo)
        self.logo_lable.grid(row=0, column=0, columnspan=4)
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)

        self.entry_1 = customtkinter.CTkEntry(self)
        self.entry_1.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Video")
        self.checkbox_1.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Thumbnail")
        self.checkbox_2.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.checkbox_3 = customtkinter.CTkCheckBox(self, text="Subtitles")
        self.checkbox_3.grid(row=2, column=2, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.button = customtkinter.CTkButton(self, text="Download", command=self.button_callback)
        self.button.grid(row=2, column=3, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.show_hide_metadata_button = customtkinter.CTkButton(self, text="Show Metadata",
                                                                 command=self.toggle_metadata)
        self.show_hide_metadata_button.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.show_hide_settings_button = customtkinter.CTkButton(self, text="Show Settings",
                                                                 command=self.toggle_settings)
        self.show_hide_settings_button.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.metadata_frame = customtkinter.CTkFrame(self)
        self.metadata_frame.grid(row=4, column=0, padx=20, pady=20, sticky="nsew", columnspan=4)

        for frame_element in range(4):
            self.metadata_frame.grid_columnconfigure(frame_element, weight=1)

        self.label_2 = customtkinter.CTkLabel(self.metadata_frame, text="Title:")
        self.label_2.grid(row=0, column=0, padx=(20, 0), sticky="w")

        self.entry_2 = customtkinter.CTkEntry(self.metadata_frame, state="readonly")
        self.entry_2.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=4)

        self.label_3 = customtkinter.CTkLabel(self.metadata_frame, text="Description:")
        self.label_3.grid(row=2, column=0, padx=(20, 0), sticky="w")

        self.textarea = customtkinter.CTkTextbox(self.metadata_frame)
        self.textarea.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=4)

        self.label_4 = customtkinter.CTkLabel(self.metadata_frame, text="Keywords:")
        self.label_4.grid(row=4, column=0, padx=(20, 0), sticky="w")

        self.entry_3 = customtkinter.CTkEntry(self.metadata_frame, state="readonly")
        self.entry_3.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=4)

        self.settings_frame = customtkinter.CTkFrame(self)
        self.settings_frame.grid(row=4, column=0, padx=20, pady=20, sticky="nsew", columnspan=4)

        self.settings_frame.grid_columnconfigure(0, weight=3)  # Поле вводу
        self.settings_frame.grid_columnconfigure(1, weight=1)  # Кнопка

        self.label_5 = customtkinter.CTkLabel(self.settings_frame, text="Path:")
        self.label_5.grid(row=0, column=0, padx=(20, 0), sticky="w")

        self.folder_entry = customtkinter.CTkEntry(self.settings_frame)
        self.folder_entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=3)

        self.browse_button = customtkinter.CTkButton(self.settings_frame, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="ew", columnspan=1)

        self.metadata_frame.grid_remove()
        self.settings_frame.grid_remove()

        self.load_config()

    def load_config(self):
        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
                folder_path = config.get("folder_path", "")
                self.folder_entry.insert(0, folder_path)
        except FileNotFoundError:
            pass

    def save_config(self):
        folder_path = self.folder_entry.get()
        config = {"folder_path": folder_path}
        with open("config.json", "w") as config_file:
            json.dump(config, config_file)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, customtkinter.END)
            self.folder_entry.insert(0, folder_path)
            self.save_config()

    def toggle_metadata(self):
        if self.metadata_frame.winfo_viewable():
            self.metadata_frame.grid_remove()
            self.show_hide_metadata_button.configure(text="Show Metadata")
        else:
            self.metadata_frame.grid()
            self.settings_frame.grid_remove()  # Закриваємо інший фрейм, якщо він відкритий
            self.show_hide_metadata_button.configure(text="Hide Metadata")
            self.show_hide_settings_button.configure(text="Show Settings")

    def toggle_settings(self):
        if self.settings_frame.winfo_viewable():
            self.settings_frame.grid_remove()
            self.show_hide_settings_button.configure(text="Show Settings")
        else:
            self.settings_frame.grid()
            self.metadata_frame.grid_remove()  # Закриваємо інший фрейм, якщо він відкритий
            self.show_hide_settings_button.configure(text="Hide Settings")
            self.show_hide_metadata_button.configure(text="Show Metadata")

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
