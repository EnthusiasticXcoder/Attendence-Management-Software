from customtkinter import CTkButton, CTkImage

class ButtonData:
    def __init__(self, Button: CTkButton, text: str, Image: CTkImage ) -> None:
        self.Button = Button
        self.text = text
        self.Image = Image
