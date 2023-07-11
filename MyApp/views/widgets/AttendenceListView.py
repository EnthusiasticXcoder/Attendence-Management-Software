from typing import Callable
import customtkinter as ctk

from services.cloud.DriveService import DriveService


class AttendenceListTile :
    @staticmethod
    def Builder(master: any, enrollment: list, names: list, status: list, command: Callable, workbook: str):
        Frame = ctk.CTkFrame(master=master,fg_color='transparent')
        Frame.grid(row=10,column=0,sticky='nsew',columnspan=4,pady=50)

        for serial, enroll, name, PorA in zip(range(1,len(status+1)), enrollment, names, status):
            AttendenceListTile(master=Frame,serial=serial, enroll=enroll, name=name, status=PorA) 

        ctk.CTkButton(master=Frame,
                      text="Submit",
                      command= lambda : AttendenceListTile._Onsubmit(Frame, command, workbook)
                      ).pack(side='right',pady=50,padx=10)
        
        ctk.CTkButton(master=Frame,
                      text="Cancel",
                      command= Frame.destroy
                      ).pack(pady=50)
        
        return Frame

    def __init__(self, master: any, serial: str, enroll: str, name: str, status: str) -> None:
        Frame = ctk.CTkFrame(master=master)
        Frame.pack()

        self.AddCell(Frame=Frame, text=serial)
        self.AddCell(Frame=Frame, text=enroll[0].value,width=250)
        self.AddCell(Frame=Frame, text=name, width=300)
        self.AddCell(Frame=Frame, text=status)
        

    def AddCell(self,Frame: any, text: str, width: int = 40):
        frame = ctk.CTkFrame(master=Frame,border_width=2,border_color='black',
                            bg_color="black",corner_radius=0,
                            fg_color= 'light green' if text == 'P' else 'red',
                            height=40,)
        frame.pack(side='left')
        ctk.CTkLabel(master=frame,text=text,width=width,
                     font=("Roboto Medium", -16,'bold'),
                     anchor='w'
                     ).pack(padx=8,pady=8)
    
    def _Onsubmit(Frame: ctk.CTkFrame, command: Callable, workbook: str):
        ''' Function on submiting the Attendence'''
        command()
        service=DriveService.getInstance()
        service.Upload_File(workbook)
        Frame.destroy()    

