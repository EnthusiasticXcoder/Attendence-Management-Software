import os
import shutil
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from utilities.exception import UnableToFindFolderException
from utilities.constants import ID, TITLE

class DriveService :
    __instance = None

    def __new__(cls):
        if cls.__instance is None :
            return super().__new__(cls)
        return cls.__instance
    
    def __init__(self) -> None:
        DriveService.__instance = self

        gauth = GoogleAuth()
        self.drive = GoogleDrive(gauth)
    
    def setVariable(self, foldername: str):
        try :
            self.FOLDER = self._Get_Folder(foldername)
        except UnableToFindFolderException :
            self.FOLDER = self.Create_Folder(foldername)
        
        self.File_List = self.get_files()

    def _Get_Folder(self,folder_name):    
        query = f"title = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed=false"
        file_list = self.drive.ListFile({'q': query, 'maxResults': 1}).GetList()
        if file_list == [] : 
            raise UnableToFindFolderException
        return file_list.pop()

    def get_files(self):
        folderID = self.FOLDER.get(ID)
        return self.drive.ListFile({'q' : f"'{folderID}' in parents and trashed=false"}).GetList()
    
    def Create_Folder(self, folderName):
        matadata = { 'title': folderName ,
                     'mimeType':'application/vnd.google-apps.folder'}
        file = self.drive.CreateFile(matadata)
        file.Upload()
        return file
    
    def Upload_File(self,filename: str):
        ''' Function to Upload Files to Drive'''
        for file in self.File_List:
            if file[TITLE] == filename : 
                filepath = os.path.join(os.getcwd(), self.FOLDER.get(TITLE), file[TITLE])
                Gfile = self.drive.CreateFile({'id' : file[ID]})
                Gfile.SetContentFile(filepath)
                Gfile.Upload()

    def Download_File(self, filename: str, path: str = None):
        ''' Function To Download Files From Drive'''
        for file in self.File_List :
            if file[TITLE] == filename : 
                filepath = path if path is not None else os.path.join(os.getcwd(), self.FOLDER.get(TITLE), file[TITLE])   
                Gfile=self.drive.CreateFile({ 'id' : file[ID] })
                Gfile.GetContentFile(filepath)

    def Download_all_files(self):
        for file in self.File_List : 
            filepath = os.path.join(os.getcwd(), self.FOLDER.get(TITLE), file[TITLE])   
            Gfile=self.drive.CreateFile({ 'id' : file[ID] })
            Gfile.GetContentFile(filepath)

    def Upload_all_File(self):
        ''' Function to Upload Files to Drive'''
        for file in self.File_List:
            filepath = os.path.join(os.getcwd(), self.FOLDER.get(TITLE), file[TITLE])
            Gfile = self.drive.CreateFile({'id' : file[ID]})
            Gfile.SetContentFile(filepath)
            Gfile.Upload()
        time.sleep(2)
        shutil.rmtree(self.FOLDER.get(TITLE))
    
    def upload_logindata(self):        
        query = f"'root' in parents and title = 'logindata.csv' or title = 'sheetdata.csv' and trashed=false"
        file_list = self.drive.ListFile({'q': query, 'maxResults': 2}).GetList()
        if file_list == [] :
            for file in ['logindata.csv','sheetdata.csv'] :
                Gfile=self.drive.CreateFile({ 'title' : file })
                Gfile.SetContentFile(file)
                Gfile.Upload()
        else :
            for file in file_list:
                Gfile=self.drive.CreateFile({ 'id' : file[ID] })
                Gfile.SetContentFile(file[TITLE])
                Gfile.Upload()
    
    def download_logindata(self):
        query = f"'root' in parents and title = 'logindata.csv' or title = 'sheetdata.csv' and trashed=false"
        file_list = self.drive.ListFile({'q': query, 'maxResults': 2}).GetList()
        
        if file_list == [] :
            return

        for file in file_list:
            Gfile=self.drive.CreateFile({ 'id' : file[ID] })
            Gfile.GetContentFile(file[TITLE])

    def Create_new_file(self, filename):
        filepath = os.path.join(os.getcwd(), self.FOLDER.get(TITLE), filename)
        Gfile=self.drive.CreateFile({ 'title' : filename })
        Gfile.SetContentFile(filepath)
        Gfile.Upload()
        self.File_List.append(Gfile)
   
    def Delete_file(self, filename):
        for file in self.File_List :
            if file[TITLE] == filename :
                Gfile= self.drive.CreateFile({'id': file[ID]})
                Gfile.Delete()
                self.File_List.remove(Gfile)
    
    def Delete_folder(self, folderName):
        matadata = { 'title': folderName ,
                     'mimeType':'application/vnd.google-apps.folder'}
        file = self.drive.CreateFile(matadata)
        file.Delete()

    def getWBNames(self):
        name = []
        for file in self.File_List:
            name.append(file.get(TITLE))
        return name