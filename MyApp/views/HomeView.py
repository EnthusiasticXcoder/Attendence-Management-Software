from typing import Tuple
import tkinter as tk
import customtkinter as ctk

try :
    import views.widgets.ToggelMenu as ToggelMenu
except ModuleNotFoundError :
    import widgets.ToggelMenu as ToggelMenu

class _HomeView(ctk.CTkFrame):
    def __init__(self, master: any, 
                 Username: str,
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
                     text= Username,
                     font=('Goudy old style',25,"bold"),
                     text_color='red',
                     ).grid(row=1,column=0,sticky='w')
        
        # Main Frame To Display Function Widgets
        self.BottomFrame = ctk.CTkFrame(master=self,fg_color=fg_color,corner_radius=0)
        self.BottomFrame.place(x=0,rely=0.15,relheight=0.85,relwidth=1)

        self.BottomFrame.grid_columnconfigure(1, weight=1)
        self.BottomFrame.grid_rowconfigure(0, weight=1)

        # Toggel Menu Widget 
        self.ToggelMenu = ToggelMenu.ToggelMenuWidget(master=self.BottomFrame)
        self.ToggelMenu.grid(row=0, column=0, sticky="nswe")
