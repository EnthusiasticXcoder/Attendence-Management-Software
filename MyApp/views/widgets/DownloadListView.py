import customtkinter as ctk
import tkinter as tk
from PIL import Image

from views.ShowExcelView import ShowExcelView

from utilities.constants import TITLE, NO_FILE_TO_DOWNLOAD, TIMES_NEW_ROMAN
from utilities.constants.routes import OPEN_FILE_ICON, CLOASE_ICON
import utilities

class DownloadListTile :
    @staticmethod
    def Builder(master: any):
        Frame = ctk.CTkFrame(master=master)

        file_list = utilities.get_files()
        if file_list == []:
            ctk.CTkLabel(master=Frame,text= NO_FILE_TO_DOWNLOAD).pack(expand=1,fill='x',padx=2,pady=2)
        else:
            for data in file_list :
                DownloadListTile(master=Frame, wbName=data[TITLE]) 

        return Frame

    def __init__(self, master: any, wbName: str) -> None:
        Frame = ctk.CTkFrame(master=master,corner_radius=0,fg_color='transparent')
        Frame.pack(expand=1,fill='x',padx=2,pady=2)

        Frame.grid_columnconfigure(0,weight=1)
        self.green = self.loadPhoto(OPEN_FILE_ICON, 20)
        self.red= self.loadPhoto(CLOASE_ICON, 20)
        
        tk.Frame(master=Frame,height=2,bg="black").grid(row=0,column=0,sticky='ew')
        ctk.CTkLabel(master=Frame,text=wbName,font=(TIMES_NEW_ROMAN,15),anchor='w').grid(row=1,column=0,padx=20,sticky='ew')
        tk.Frame(master=Frame,height=2,bg="black").grid(row=0,column=0,sticky='ew')

        ctk.CTkButton(master=Frame,text="",
                        fg_color=('#C0C2C5','#343638'),
                        image=self.green,width=20,border_width=2,
                        command= lambda: ShowExcelView(wbName)
                        ).grid(row=1,column=1,padx=3)
        ctk.CTkButton(master=Frame,text="",
                        fg_color=('#C0C2C5','#343638'),
                        image=self.red,width=20,border_width=2,
                        command= lambda: utilities.download_file(wbName)
                        ).grid(row=1,column=2)
    
    def loadPhoto(self,path,size):
        return ctk.CTkImage(light_image=Image.open(path),
                            dark_image=Image.open(path),
                            size=(size,size))
