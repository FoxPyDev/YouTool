import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("YouTool")
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    app.mainloop()
