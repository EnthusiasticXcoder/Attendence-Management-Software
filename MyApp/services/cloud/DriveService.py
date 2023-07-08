from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class InstanceAlreadyCreatedException(Exception) :
    ''' Exception when someone directly calls the initialiser'''

class DriveService :
    __instance = None

    @staticmethod
    def getInstance():
        if DriveService.__instance == None :
            DriveService()
        return DriveService.__instance
    
    def __init__(self) -> None:
        if DriveService.__instance != None:
            raise InstanceAlreadyCreatedException
        DriveService.__instance = self

        gauth = GoogleAuth()
        self.drive = GoogleDrive(gauth)