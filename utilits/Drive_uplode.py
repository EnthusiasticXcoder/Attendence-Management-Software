import os
from tkinter import messagebox,filedialog
from time import sleep

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


DStoreID=None

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

class DriveFile_list :
    def __init__(self,folder) -> None:
        self.folderID=get_folderid(folder)
        self.Files=get_files(folder)

    def Update(self,folder):
        self.Files=get_files(folder)

def Define(folder):
    global DStoreID
    DStoreID=DriveFile_list(folder)

def get_folderid(foldername):
    try:
        folder="1IZzpZ-uXQP1Fu4_A2fU4-fi2-hGqMCQg"
        folder_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()

        for gfolder in folder_list:
            if gfolder['title'] == foldername:
                return gfolder['id']
        else:
            gfolder= drive.CreateFile({'parents' : [{'id' : folder}], 'title': foldername ,'mimeType':'application/vnd.google-apps.folder'})
            gfolder.Upload()
            return gfolder['id']
    except Exception as e :             
        if messagebox.askretrycancel("Internet Error",f"Unable To Upload\nPlease Cheack Your Internet Connection\n{e}") == True:
            get_folderid(foldername)
        else: 
            os._exit(1)

def get_files(folder):
    folder_id=get_folderid(folder)
    try:    
        file_list =  drive.ListFile({'q' : f"'{folder_id}' in parents and trashed=false"}).GetList()
        return file_list
    except :             
        return


def dfolder(foldername):
    try:
        folder="1IZzpZ-uXQP1Fu4_A2fU4-fi2-hGqMCQg"
        folder_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
        for gfolder in folder_list:
            if gfolder['title'] == foldername:
                delfold= drive.CreateFile({'parents' : [{'id' : folder}], 'id':gfolder['id'],'mimeType':'application/vnd.google-apps.folder'})
                delfold.Delete()
                return
    except :             
        if messagebox.askretrycancel("Internet Error","Unable To Upload\nPlease Cheack Your Internet Connection") == True:
            dfolder(foldername)
        else: 
            os._exit(1)

def DeleteFile(foldername,filename,Function):
    if messagebox.askyesno("Parmanrntly Delete File",f"Are You Shure Want To Delete {filename} Paemanently"):
        try:
            folder=DStoreID.folderID if DStoreID!=None else get_folderid(foldername)
            file_list=DStoreID.Files if DStoreID!=None else drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()

            for gfolder in file_list:
                if gfolder['title'] == filename:
                    delfold= drive.CreateFile({'parents' : [{'id' : folder}], 'id':gfolder['id']})
                    delfold.Delete()
                    Path=f'workbooks/{foldername}/{filename}'
                    os.remove(Path)
                    if DStoreID!=None: DStoreID.Update(foldername)
                    Function.HideDownload()
                    Function.Configmenu(foldername)
                    Function.ShowDownload()
                    return
        except :             
            if messagebox.askretrycancel("Internet Error","Unable To Upload\nPlease Cheack Your Internet Connection") == True:
                dfolder(foldername)
            else: 
                os._exit(1)
    else:
        return



def upload_files(folder = 'user' , filename= 'all' ,Function=None ) :
    if folder != 'user':
        ID=DStoreID.folderID if DStoreID!=None else get_folderid(folder)
    else: ID="13J2SZLADGgg5wPNZfi4wPxjzwUbVVnWI"

    directory = os.getcwd()
    path = directory+'\\users' if folder == 'user' else directory+f'\\workbooks\\{folder}'
    
    files=[f for f in os.listdir(path)]     # Files in Localstorage

    if not files :
        return
    
    file_list =DStoreID.Files if DStoreID!=None and folder != 'user' else drive.ListFile({'q' : f"'{ID}' in parents and trashed=false"}).GetList()   # Files in Drive   

    try:                                               
        if file_list :
            for file in file_list:
                if filename=='all':
                    if file['title'] in files:
                        filepath = os.path.join(path, file['title'])
                        files.remove(file['title'])
                        gfile = drive.CreateFile({'parents' : [{'id' : ID}], 'id' : file['id'] })
                        gfile.SetContentFile(filepath)
                        gfile.Upload()
                elif filename==file['title'] :
                    filepath = os.path.join(path, file['title'])
                    gfile = drive.CreateFile({'parents' : [{'id' : ID}], 'id' : file['id'] })
                    gfile.SetContentFile(filepath)
                    gfile.Upload()
                    return 
        if files :
            for file in files:
                filepath = os.path.join(path, file)
                if filename=='all':
                    gfile = drive.CreateFile({'parents' : [{'id' : ID}], 'title': file })
                    gfile.SetContentFile(filepath)
                    gfile.Upload()      
                elif filename==file: 
                    gfile = drive.CreateFile({'parents' : [{'id' : ID}], 'title': file })
                    gfile.SetContentFile(filepath)
                    gfile.Upload()
                    if Function!=None:
                        Function.HideDownload()
                        Function.Configmenu(folder)
    
    except Exception as e:
        if messagebox.askretrycancel("Internet Error",f"Unable To Upload\nPlease Cheack Your Internet Connection\n{e}") == True:
            upload_files(folder , filename ) 
        else: 
            os._exit(1)   


def download_files( folder = 'user' , filename = 'all' , savepath = False):
    if folder != 'user':
        ID=DStoreID.folderID if DStoreID!=None else get_folderid(folder)
    else : ID="13J2SZLADGgg5wPNZfi4wPxjzwUbVVnWI"

    if folder =='user' and savepath :
        return

    if filename != 'all' and savepath :
        path=filedialog.asksaveasfilename(filetypes=[("Excel Workbook","*.xlsx")],defaultextension='.xlsx')
    else:
        path ='users' if folder == 'user' else f'workbooks/{folder}'
    
    if not savepath and folder != 'user' :
        try : os.mkdir(path)
        except : pass

    try:
        if folder != 'user' : file_list =DStoreID.Files if DStoreID!=None else drive.ListFile({'q' : f"'{ID}' in parents and trashed=false"}).GetList()   # Files in Drive
        else : file_list= drive.ListFile({'q' : f"'{ID}' in parents and trashed=false"}).GetList()

        if not file_list :
            return

        for file in file_list:
            if filename == 'all':
                file_get=drive.CreateFile({ 'id' : file['id'] })
                file_get.GetContentFile(f"{path}/{file['title']}")
            else:
                if filename == file['title']:
                    file_get=drive.CreateFile({ 'id' : file['id'] })
                    if path and savepath :
                        file_get.GetContentFile(path)
                        return 
                    file_get.GetContentFile(f"{path}/{file['title']}")
                    return
    except Exception as e:
        if messagebox.askretrycancel("Internet Error",f"Unable To Upload\nPlease Cheack Your Internet Connection\n{e}") == True:
            download_files( folder , filename , savepath )
        else: 
            os._exit(1)
