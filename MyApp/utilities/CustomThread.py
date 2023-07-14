from threading import Thread
from tkinter import messagebox


class CustomThread(Thread):
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, daemon = None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        
    def run(self) -> None:
        try :
            return super().run()
        except Exception :
            acknowledgement = messagebox.askretrycancel("Internet Error","Unable To Upload\nPlease Cheack Your Internet Connection")
            if acknowledgement is True :
                self.run()
            quit()