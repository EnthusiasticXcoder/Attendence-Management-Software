from typing import Tuple
import tkinter as tk
import customtkinter as ctk

from widgets.Toggel_Menu_Widget import ToggelMenuWidget

class AdminHomeView(ctk.CTkFrame):
    def __init__(self, master: any, 
                 width: int = 200, 
                 height: int = 200, 
                 corner_radius: int | str | None = None, 
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
        # Home View For Admin Level Login 
        #configuring widget Grid
        self.grid_columnconfigure(0,weight=1)

        # Head Frame To Display Logo and name
        HeadWidget = ctk.CTkFrame(master=self,fg_color=fg_color,corner_radius=0)
        HeadWidget.grid(row=0,column=0,sticky='ew')
        
        HeadWidget.grid_columnconfigure(0, weight=1)
        HeadWidget.grid_columnconfigure(0, weight=1)

        # Logo Image OF The Institute
        self.img= tk.PhotoImage(file='assets/images/logoies.png') 
        label=tk.Label(HeadWidget,image=self.img,bg=fg_color)
        label.grid(row=0,column=0,sticky='nw')
        
        # Username Widget
        Frame=ctk.CTkFrame(master=HeadWidget,fg_color=fg_color)
        Frame.grid(row=0,column=0,sticky='e')
        
        NameFrame=ctk.CTkFrame(master=Frame,fg_color=fg_color)
        NameFrame.pack(side=tk.RIGHT,padx=20,ipadx=50)
        ctk.CTkLabel(master=NameFrame,
                     text="Login as : ",
                     text_color='black',
                     font=('Goudy old style',18,"bold"),
                     anchor='w',
                    ).grid(row=0,column=0,sticky='w')
        ctk.CTkLabel(master=NameFrame,
                     text='Username',
                     font=('Goudy old style',25,"bold"),
                     text_color='red',
                     ).grid(row=1,column=0,sticky='w')

        # Main Frame To Display Function Widgets
        BottomFrame = ctk.CTkFrame(master=self,fg_color=fg_color,corner_radius=0)
        BottomFrame.place(x=0,rely=0.15,relheight=0.85,relwidth=1)

        BottomFrame.grid_columnconfigure(1, weight=1)
        BottomFrame.grid_rowconfigure(0, weight=1)

        # Toggel Menu Widget 
        self.ToggelMenu = ToggelMenuWidget(master=BottomFrame)
        self.ToggelMenu.grid(row=0, column=0, sticky="nswe")

        # adding Buttons to Toggel Menu Widget
        for ButtonData in ADMIN_BUTTONS:
            self.ToggelMenu.addButton(imagepath=ButtonData[ICONPATH],text=ButtonData[TEXT])

        # Main Frame Widget for Activities
        self.MainFrame = ctk.CTkFrame(master=BottomFrame)
        self.MainFrame.grid(row=0, column=1, sticky="nswe")
        

ICONPATH = 'IconPath'
TEXT = 'text'

ADMIN_BUTTONS = [
    {
        ICONPATH : 'assets/icons/home.png',
        TEXT : 'Home'
    },
    {
        ICONPATH : 'assets/icons/file-plus.png',
        TEXT : 'Create New Sheet'
    },
    {
        ICONPATH : 'assets/icons/arrow-down-circle.png',
        TEXT : 'Import Workbook'
    },
    {
        ICONPATH : 'assets/icons/edit.png',
        TEXT : 'Enter Attendence'
    },
    {
        ICONPATH : 'assets/icons/file-text.png',
        TEXT : 'Download Excel'
    },
    {
        ICONPATH : 'assets/icons/user-plus.png',
        TEXT : 'Create New Admin'
    },
    {
        ICONPATH : 'assets/icons/users.png',
        TEXT : 'Create New User'
    },
    {
        ICONPATH : 'assets/icons/change.webp',
        TEXT : 'Change Password'
    },{
        ICONPATH : 'assets/icons/delete.png',
        TEXT : 'Delete Entry'
    },
    {
        ICONPATH : 'assets/icons/log-out.png',
        TEXT : 'Log Out'
    },
]
if __name__=='__main__':
    r=ctk.CTk()
    r.rowconfigure(0,weight=1)
    r.columnconfigure(0,weight=1)
    r.geometry('1000x700+0+0')
    AdminHomeView(master=r).grid(row=0,column=0,sticky='nsew')
    r.mainloop()