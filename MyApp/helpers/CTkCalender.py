from datetime import date
from customtkinter import get_appearance_mode,CTk
from tkinter import ttk
import tkcalendar as tc


class CTkDateEntry(tc.DateEntry):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        style = ttk.Style()
        style.theme_use('clam') 
        
        if get_appearance_mode()=='Light': 
            style.configure('DateEntry',
                    fieldbackground='white',
                    background='#979DA2',
                    foreground='black',
                    arrowcolor='black',
                    arrowsize=20)
            self.configure(selectmode="day",font=("Microsoft YaHei UI Light",10,"bold"),borderwidth=6,
                            showothermonthdays=False,showweeknumbers=False, 
                            bordercolor ="#E5E5E5",normalforeground="black",
                            maxdate=date.today(),width=13,date_pattern="dd-mm-y",
                            disabledbackground='white',
                            disableddaybackground='#E5E5E5',disableddayforeground='#515256',
                            selectbackground="#BFBFBF",selectforeground="black",
                            background='#979DA2',foreground='#333333',
                            headersbackground="#E5E5E5",headersforeground="black",
                            normalbackground='#E5E5E5',
                            weekendbackground ="#E5E5E5")
        
        if get_appearance_mode()=='Dark': 
            style.configure('DateEntry',
                    fieldbackground='#343638',
                    background='#565B5E',
                    foreground='white',
                    arrowcolor='#ADB4BC',
                    arrowsize=20)
            self.configure(selectmode="day",font=("Microsoft YaHei UI Light",10,"bold"),borderwidth=6,
                            showothermonthdays=False,showweeknumbers=False, 
                            bordercolor ="#565B5E",normalforeground="#D0D8E1",
                            maxdate=date.today(),width=13,date_pattern="dd-mm-y",
                            disabledbackground='white',
                            disableddaybackground='#565B5E',disableddayforeground='#515256',
                            selectbackground="#1F6AA5",selectforeground="black",
                            background='#333333',foreground='#D0D8E1',
                            headersbackground="#565B5E",headersforeground="black",
                            normalbackground='#565B5E',
                            weekendbackground ="#565B5E")
