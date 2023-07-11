import customtkinter as ctk
import tkinter as tk
from PIL import Image

from services.cloud.DriveService import DriveService, TITLE

class DownloadListTile :
    @staticmethod
    def Builder(master: any):
        Frame = ctk.CTkFrame(master=master)

        service = DriveService.getInstance()
        if service.File_List == []:
            ctk.CTkLabel(master=Frame,text=" --- NO FILE TO DOWNLOAD ---").pack(expand=1,fill='x',padx=2,pady=2)
            
        else:
            for data in service.File_List :
                DownloadListTile(master=Frame, data=data[TITLE]) 
        
        return Frame

    def __init__(self, master: any, data: str) -> None:
        Frame = ctk.CTkFrame(master=master,corner_radius=0,fg_color='transparent')
        Frame.pack(expand=1,fill='x',padx=2,pady=2)

        Frame.grid_columnconfigure(0,weight=1)
        self.green = self.loadPhoto("assets/icons/green.png",20)
        self.red= self.loadPhoto("assets/icons/x red.png",20)
        
        tk.Frame(master=Frame,height=2,bg="black").grid(row=0,column=0,sticky='ew')
        ctk.CTkLabel(master=Frame,text=data,font=("times new roman",15),anchor='w').grid(row=1,column=0,padx=20,sticky='ew')
        tk.Frame(master=Frame,height=2,bg="black").grid(row=0,column=0,sticky='ew')

        ctk.CTkButton(master=Frame,text="",
                        fg_color=('#C0C2C5','#343638'),
                        image=self.green,width=20,border_width=2,
                        ).grid(row=1,column=1,padx=3)
        ctk.CTkButton(master=Frame,text="",
                        fg_color=('#C0C2C5','#343638'),
                        image=self.red,width=20,border_width=2,
                        command= lambda: DriveService.getInstance().Delete_file(data)
                        ).grid(row=1,column=2)
    
    def loadPhoto(self,path,size):
        return ctk.CTkImage(light_image=Image.open(path),
                            dark_image=Image.open(path),
                            size=(size,size))
