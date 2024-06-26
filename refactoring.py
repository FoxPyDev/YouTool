import customtkinter
from PIL import Image
from tubefox import TubeFox
import license
import json


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False, False)
        self.title("YouTool")
        self.create_widgets()

        # Завантаження збереженого ключа при запуску
        self.load_saved_license()

    def create_widgets(self):
        self.get_header()
        self.create_input_field()
        self.create_license_verification_frame()

    def get_header(self):
        self.logo = customtkinter.CTkImage(dark_image=Image.open('logo.png'), size=(600, 150))
        self.logo_label = customtkinter.CTkLabel(self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, columnspan=4)

    def create_input_field(self):
        self.grid_columnconfigure(1, weight=4)
        self.url_entry = customtkinter.CTkEntry(self)
        self.url_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=4)
        self.url_entry.bind("<FocusIn>", self.paste_from_clipboard)
        self.url_entry.bind("<Control-a>", lambda event: self.url_entry.select_range(0, 'end'))

    def create_license_verification_frame(self):
        self.license_frame = customtkinter.CTkFrame(self)
        self.license_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew", columnspan=4)

        self.license_entry_label = customtkinter.CTkLabel(self.license_frame, text="Enter License Key:")
        self.license_entry_label.grid(row=0, column=0, padx=10, pady=10)

        # Відображення збереженого ключа, якщо він є
        self.saved_license = self.load_saved_license()
        self.license_entry = customtkinter.CTkEntry(self.license_frame)
        self.license_entry.grid(row=0, column=1, padx=10, pady=10)
        self.license_entry.insert(0, self.saved_license)

        self.verify_button = customtkinter.CTkButton(self.license_frame, text="Verify License", command=self.verify_license)
        self.verify_button.grid(row=0, column=2, padx=10, pady=10)

    def create_info_block(self):
        self.license_frame = customtkinter.CTkFrame(self)
        self.license_frame.grid(row=4, column=0, padx=20, pady=20, sticky="nsew", columnspan=4)

        # Create and configure CTkLabels
        labels_texts = [
            "The program works in test mode.",
            "Support and operation of this software will end on 13.07.2024",
            "Expect a new version.",
            "Current information at the link: https://t.me/socialtools_foxpydev"
        ]
        for row, text in enumerate(labels_texts):
            label = customtkinter.CTkLabel(self.license_frame, text=text)
            label.grid(row=row)
            label.configure(justify="center")

        # Adjust the row and column configurations of the license_frame
        self.license_frame.grid_rowconfigure(0, weight=1)
        self.license_frame.grid_columnconfigure(0, weight=1)

    def load_saved_license(self):
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
                return config.get("license_key", "")
        except FileNotFoundError:
            return ""

    def save_license(self, license_key):
        with open("config.json", "w") as file:
            json.dump({"license_key": license_key}, file)

    def verify_license(self):
        key = self.license_entry.get()
        if license.check_license(key):
            self.save_license(key)  # Зберігання ключа
            self.create_download_menu()
            self.license_frame.grid_forget()
            self.create_info_block()
        else:
            print("Invalid license key!")

    def create_download_menu(self):
        self.download_frame = customtkinter.CTkFrame(self)
        self.download_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew", columnspan=4)

        for frame_element in range(4):
            self.download_frame.grid_columnconfigure(frame_element, weight=1)

        self.checkbox_1 = customtkinter.CTkCheckBox(self.download_frame, text="Video")
        self.checkbox_1.grid(row=2, column=0, padx=20, pady=20, sticky="w", columnspan=1)

        self.checkbox_2 = customtkinter.CTkCheckBox(self.download_frame, text="Cover")
        self.checkbox_2.grid(row=2, column=1, padx=20, pady=20, sticky="w", columnspan=1)

        self.checkbox_3 = customtkinter.CTkCheckBox(self.download_frame, text="Subtitles")
        self.checkbox_3.grid(row=2, column=2, padx=20, pady=20, sticky="w", columnspan=1)

        self.button = customtkinter.CTkButton(self.download_frame, text="Download", command=self.start_download)
        self.button.grid(row=2, column=3, padx=20, pady=20, columnspan=1)

    def start_download(self):
        url = self.url_entry.get()
        if url:
            tubefox_instance = TubeFox(url)
            if self.checkbox_1.get():
                tubefox_instance.download_video()
            if self.checkbox_2.get():
                tubefox_instance.download_thumbnail()
            if self.checkbox_3.get():
                tubefox_instance.download_subtitles()

    def paste_from_clipboard(self, event):
        self.url_entry.delete(0, 'end')
        clipboard_content = self.clipboard_get()
        self.url_entry.insert('insert', clipboard_content)


if __name__ == "__main__":
    app = App()
    app.mainloop()
