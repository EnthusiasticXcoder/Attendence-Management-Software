import customtkinter as ctk
from app import MyApp


def main():
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    app = MyApp()
    app.start()


if __name__=='__main__':
    main()
