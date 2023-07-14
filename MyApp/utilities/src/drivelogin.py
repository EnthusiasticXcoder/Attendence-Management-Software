from utilities.CustomThread import CustomThread

import services

def download_logindata():
    service = services.DriveService()
    download = CustomThread(target = service.download_logindata)
    download.start()

def upload_logindata():
    service = services.DriveService()
    upload = CustomThread(target = service.upload_logindata)
    upload.start()