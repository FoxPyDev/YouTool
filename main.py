import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x520")
        self.title("YouTool")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=4)
        self.grid_columnconfigure(3, weight=4)
        self.grid_columnconfigure(4, weight=4)
        self.grid_columnconfigure(5, weight=4)
        self.grid_columnconfigure(6, weight=4)
        self.grid_columnconfigure(7, weight=4)

        self.entry_1 = customtkinter.CTkEntry(self)
        self.entry_1.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Video")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Thumbnail")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.checkbox_3 = customtkinter.CTkCheckBox(self, text="Subtitles")
        self.checkbox_3.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.button = customtkinter.CTkButton(self, text="Download", command=self.button_callback)
        self.button.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w", columnspan=1)

        self.label_2 = customtkinter.CTkLabel(self, text="Title:")
        self.label_2.grid(row=2, column=0, padx=(20, 0), sticky="w")

        self.entry_2 = customtkinter.CTkEntry(self, state="readonly")
        self.entry_2.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=4)

        self.label_3 = customtkinter.CTkLabel(self, text="Description:")
        self.label_3.grid(row=4, column=0, padx=(20, 0), sticky="w")

        self.textarea = customtkinter.CTkTextbox(self)
        self.textarea.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=4)

        self.label_4 = customtkinter.CTkLabel(self, text="Keywords:")
        self.label_4.grid(row=6, column=0, padx=(20, 0), sticky="w")

        self.entry_3 = customtkinter.CTkEntry(self, state="readonly")
        self.entry_3.grid(row=7, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=4)

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
