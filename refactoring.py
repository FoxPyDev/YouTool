import customtkinter
from PIL import Image
from tubefox import TubeFox


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x350")
        self.title("YouTool")
        self.create_widgets()

    def create_widgets(self):
        self.get_header()
        self.create_input_field()
        self.create_download_menu()

    def get_header(self):
        self.logo = customtkinter.CTkImage(dark_image=Image.open('./LOGO.png'), size=(600, 150))
        self.logo_label = customtkinter.CTkLabel(self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, columnspan=4)

    def create_input_field(self):
        self.grid_columnconfigure(1, weight=4)
        self.url_entry = customtkinter.CTkEntry(self)
        self.url_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=4)
        self.url_entry.bind("<FocusIn>", self.paste_from_clipboard)
        self.url_entry.bind("<Control-a>", lambda event: self.url_entry.select_range(0, 'end'))

    def create_download_menu(self):
        self.download_frame = customtkinter.CTkFrame(self)
        self.download_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew", columnspan=4)

        for frame_element in range(4):
            self.download_frame.grid_columnconfigure(frame_element, weight=1)

        self.checkbox_1 = customtkinter.CTkCheckBox(self.download_frame, text="Video")
        self.checkbox_1.grid(row=2, column=0, padx=20, pady=20, sticky="w", columnspan=1)

        self.checkbox_2 = customtkinter.CTkCheckBox(self.download_frame, text="Thumbnail")
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
            print("Downloads started.")

    def paste_from_clipboard(self, event):
        self.url_entry.delete(0, 'end')
        clipboard_content = self.clipboard_get()
        self.url_entry.insert('insert', clipboard_content)

    def process_url(self, event):
        # This method remains unchanged
        url = self.url_entry.get()
        if url:
            custom_instance = TubeFox(url)
            print("OK")


if __name__ == "__main__":
    app = App()
    app.mainloop()
