import os
from tkinter import messagebox
from customtkinter import filedialog

import services
from utilities.constants import USERNAME, TITLE
from utilities.exception import UnableToCreateWorksheetException, CreateNewWorksheetException
import utilities

def import_workbook():
    filePath = filedialog.askopenfilename(
        initialdir='D:/',
        title="Import A File",
        filetypes=[("xlsx files","*.xlsx")]
        )
    if filePath :
        wbservice = services.WorkBookService()
        dirname = services.LoginService.__LoginData[USERNAME]
        wbservice.addWorkbook(dirname=dirname, filesrc=filePath)

        utilities.create_new_file(filePath)
        messagebox.showinfo('Sucess','WorkBook Imported Successfully')

def get_workbook_names():
    _driveservice = services.DriveService()
    return _driveservice.getWBNames()

def create_worksheet(workbook: str, sheetname: str):
    if workbook.strip() == '' or sheetname.strip() == '':
        messagebox.showerror('All Fields Are Required')
    
    wbpath = os.path.join(os.getcwd(), services.LoginService.__LoginData[USERNAME], workbook)

    try :
        wbservice = services.WorkBookService()
        wbservice.CreateNewWorksheet(wbpath, sheetname)
        
        utilities.upload_logindata()
        utilities.upload_file(workbook)

        messagebox.showinfo('Sucess', 'New Worksheet Created Successfully')
    except UnableToCreateWorksheetException :
        messagebox.showerror('Error', 'Unable To Create Worksheet')
    except FileNotFoundError :
        messagebox.showerror('Error', 'File Not Found')

def enter_attendence(workbook: str, isTheory: bool, DateTime: str, CSVRollno: str):
    utilities.download_file(workbook)
    
    _driveService = services.DriveService()
    wbpath = os.path.join(_driveService.FOLDER.get(TITLE), workbook)
    
    try:
        wbservice = services.WorkBookService()
        return wbservice.EnterAttendence(wbPath=wbpath, 
                                        isTheory=isTheory, 
                                        DateTime=DateTime, 
                                        CSVRollno=CSVRollno)             
    except CreateNewWorksheetException :
        messagebox.showerror('Error', 'Create New Sheet')
    except Exception :
        messagebox.showerror('Error', 'Unable To Enter Attendence')

def get_worksheet_from_path(wbPath):
    _wbservice = services.WorkBookService()
    return _wbservice.get_worksheet_from_path(wbPath)

def get_evaluator(wbpath):
    _wbservice = services.WorkBookService()
    return _wbservice.get_evaluator(wbpath)

def get_number_of_entry(worksheet):
    _wbservice = services.WorkBookService()
    return _wbservice.getNumberofEntry(worksheet) + 11
