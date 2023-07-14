import os
from utilities.CustomThread import CustomThread

import services

def upload_all_workbook():
    driveservice = services.DriveService()
    upload = CustomThread(target = driveservice.Upload_all_File)
    upload.start()

def download_all_workbook():
    _driveService = services.DriveService()
    download = CustomThread(target = _driveService.Download_all_files )
    download.start()

def create_new_file(filepath):
    driveservice = services.DriveService()
    create_file = CustomThread(target=driveservice.Create_new_file, kwargs=({'filename' : os.path.basename(filepath)}))
    create_file.start()

def create_new_folder(Username):
    driveservice = services.DriveService()
    create_folder = CustomThread(target=driveservice.Create_Folder, args=(Username))
    create_folder.start()

def upload_file(workbook):
    driveservice = services.DriveService()
    upload = CustomThread(target= driveservice.Upload_File, args=(workbook))
    upload.start()

def download_file(workbook: str, path = None):
    _driveService = services.DriveService()
    download = CustomThread( target = _driveService.Download_File, kwargs={'filename' : workbook, 'path' : path })
    download.start()

def delete_folder(Username):
    _driveService = services.DriveService()
    thread = CustomThread(target= _driveService.Delete_folder, args=(Username))
    thread.start()

def get_files():
    _driveService = services.DriveService()
    return _driveService.File_List

def get_folder():
    _driveService = services.DriveService()
    return _driveService.FOLDER