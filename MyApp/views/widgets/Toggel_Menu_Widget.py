from typing import Tuple
import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk


class ToggelMenuWidget(ctk.CTkFrame):

    _Buttonarray = []

    def __init__(self, master: any, 
                 width: int = 200, 
                 height: int = 200, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = 'skyblue3', 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, 
                         width, 
                         height, 
                         corner_radius, 
                         border_width, 
                         bg_color, 
                         fg_color, 
                         border_color, 
                         background_corner_colors, 
                         overwrite_preferred_drawing_method, **kwargs)
        # Toggel Menu Widget configure Button
        self.grid_rowconfigure(1, minsize=20)   # empty row with minsize as spacing
        self.grid_rowconfigure(12, weight=1)  # empty row as spacing
        self.grid_rowconfigure(14, minsize=15)    # empty row with minsize as spacing
        self.grid_rowconfigure(16, minsize=30)

        self.grid_columnconfigure(2,minsize=15)

        # Toggel Buttons
        self.imgmenu = ImageTk.PhotoImage(Image.open('assets/icons/menu.png').resize((35,35)))
        self.imgx = ImageTk.PhotoImage(Image.open('assets/icons/x.png').resize((35,35)))
        
        self.toggelButton=tk.Label(self,image=self.imgmenu,text=None,bg=fg_color,cursor='hand2')
        self.toggelButton.grid(row=0,column=0,sticky='w',padx=20)
        self.toggelButton.bind("<Button-1>",self.open)

        # Mode Change Menu
        self.ModeChange = ctk.CTkOptionMenu(master=self,
                                            values=["Light", "Dark", "System"],
                                            command=ctk.set_appearance_mode)
        self.ModeChange.set('System')
        self.ModeSwitch = ctk.CTkSwitch(master=self,text="",command= lambda :self.change_mode(self.ModeSwitch),width=0)
        self.ModeSwitch.grid(row=15, column=0,sticky='e',columnspan=3,padx=20)
    
    def addButton(self,image,text):
        row=ToggelMenuWidget._Buttonarray.__len__()
        button =ctk.CTkButton(master=self,text="",image=self.loadImage(image,30),width=30,compound='right',fg_color='transparent')
        button.grid(row=row+2,column=0,padx=20,pady=3)
        ToggelMenuWidget._Buttonarray.append([button,text,self.loadImage(image,30)])
        return button
    
    def close(self,e =None):
        self.toggelButton.configure(image=self.imgmenu)
        if (ToggelMenuWidget._Buttonarray):
            for button in ToggelMenuWidget._Buttonarray :
                button[0].configure(text="",
                                    image=button[2],
                                    width=30,
                                    fg_color='transparent')
                button[0].grid_configure(column=0,pady=3)
        self.ModeChange.grid_forget()
        self.ModeSwitch.grid(row=15, column=0,sticky='e',columnspan=3,padx=20)
        self.toggelButton.bind("<Button-1>",self.open)

    def open(self,e = None):
        self.toggelButton.configure(image=self.imgx)
        if (ToggelMenuWidget._Buttonarray):
            for button in ToggelMenuWidget._Buttonarray :
                button[0].configure(text=button[1],
                                    image=self.loadImage('assets/images/blank.png',size=1),
                                    width=130,
                                    fg_color=ctk.ThemeManager.theme['CTkButton']['fg_color'])
                button[0].grid_configure(column=1,pady=6)
        self.ModeSwitch.grid_forget()
        self.ModeChange.grid(row=15, column=1,padx=20,sticky='ew',columnspan=3)
        self.toggelButton.bind("<Button-1>",self.close)
    
    def change_mode(self,ModeSwitch):
        if ModeSwitch.get() == 0:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
    
    def loadImage(self,path,size):
        return ctk.CTkImage(light_image=Image.open(path),
                            dark_image=Image.open(path),
                            size=(size,size)) 


if __name__=='__main__':
    r=ctk.CTk(fg_color='blue')
    r.rowconfigure(0,weight=1)
    r.columnconfigure(0,weight=0)
    ToggelMenuWidget(master=r).grid(row=0,column=0,sticky='nsew')
    r.mainloop()