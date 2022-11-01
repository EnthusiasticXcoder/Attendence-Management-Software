import os
from threading import Lock
from tkinter import messagebox,filedialog

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
drive = GoogleDrive(gauth)


l=Lock()

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

def get_files(folder):
    folder_id=get_folderid(folder)
    try:    
        file_list =  drive.ListFile({'q' : f"'{folder_id}' in parents and trashed=false"}).GetList()
        return file_list
    except :             
        return


def upload_files(folder = 'user' , filename= 'all' ) :
    ID = get_folderid(folder)
    directory = os.getcwd()
    
    if folder == 'user' :
        path = directory+'\\users'
    else :
        path = directory+f'\\workbooks\\{folder}'
    
    files=[f for f in os.listdir(path)]     # Files in Localstorage

    if not files :
        return
    try:
        file_list =  drive.ListFile({'q' : f"'{ID}' in parents and trashed=false"}).GetList()   # Files in Drive                                                
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
    
    except Exception as e:
        if messagebox.askretrycancel("Internet Error",f"Unable To Upload\nPlease Cheack Your Internet Connection\n{e}") == True:
            upload_files(folder , filename ) 
        else: 
            os._exit(1)   


def download_files( folder = 'user' , filename = 'all' , savepath = False):
    ID = get_folderid(folder)

    if folder =='user' and savepath :
        return

    if filename != 'all' and savepath :
        path=filedialog.asksaveasfilename(filetypes=[("Excel Workbook","*.xlsx")],defaultextension='.xlsx')
    else:
        if folder == 'user':
            path ='users'
        else :
            path = f'workbooks/{folder}'
    
    if not savepath and folder != 'user' :
        try : os.mkdir(path)
        except : pass

    try:
        file_list = drive.ListFile({'q' : f"'{ID}' in parents and trashed=false"}).GetList()

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

