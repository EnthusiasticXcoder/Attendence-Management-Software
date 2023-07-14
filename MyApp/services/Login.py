import csv
import base64

from utilities.exception import (
    UnableToDeleteException,
    UsernameNotFoundException,
    IncorrectPasswordException,
    CannotDeleteCurrentLoginUserException )
from utilities.constants import USERNAME, PASSWORD, ADMIN, LEVELORADMIN
from utilities.constants.routes import LOGINDATA


class LoginService:
    __instance = None
    __LoginData = None

    def __new__(cls):
        if cls.__instance is None :
            return super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        LoginService.__instance = self
    
    def TryLogin(self , UserName: str , Password: str ):
        ''' A Method for trying to LogIn using given Credentials 
         Return LoginData '''
        
        with open( LOGINDATA ,mode='r') as file:
            reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            for data in reader :
                if self.DecryptData(data[USERNAME]) == UserName :
                    if self.DecryptData(data[PASSWORD]) == Password : 
                        LoginService.__LoginData = {
                                USERNAME: self.DecryptData(data[USERNAME]),
                                PASSWORD: self.DecryptData(data[PASSWORD]),
                                LEVELORADMIN: self.DecryptData(data[LEVELORADMIN])
                            }
                        return LoginService.__LoginData
                    else : raise IncorrectPasswordException
            else : raise UsernameNotFoundException
               
    def CreateLogin(self , UserName: str , Password: str , isadmin: bool = False ):
        ''' A Method To Create Login And Append Login Data To The logindata File'''
        if isadmin : 
            level =ADMIN
        else : 
            level = LoginService.__LoginData[USERNAME]
        
        with open( LOGINDATA ,mode='a') as file:
            writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            writer.writerow({
                    USERNAME : self.EncryptData(UserName),
                    PASSWORD : self.EncryptData(Password),
                    LEVELORADMIN : self.EncryptData(level)})
        
    def CheackUserName(self , UserName: str):
        ''' Method to cheack wether the username is valid or not 
        Return True for Vaild Username and False for invalid UserName'''
        with open( LOGINDATA ,mode='r') as file:
            reader = csv.DictReader(file,fieldnames=[USERNAME])
            usernames = [self.DecryptData(data[USERNAME]) for data in reader]
            if UserName in usernames : return False
            return True
       
    def DeleteUser(self, UserName: str ):
        ''' A Method To Delete User with Username and password
        Return number of rows deleted'''
        NumberOfDelete = 0
        if LoginService.__LoginData[USERNAME] == UserName :
            raise CannotDeleteCurrentLoginUserException
    
        with open( LOGINDATA ,mode='r') as file :
            reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN]) 
            dataarray = []
            for data in reader :
                if self.DecryptData(data[USERNAME]) == UserName or self.DecryptData(data[LEVELORADMIN]) == UserName :
                    NumberOfDelete += 1
                    continue
                dataarray.append(data)

        if NumberOfDelete == 0 : 
            raise UnableToDeleteException

        with open( LOGINDATA , mode='w') as file:
            writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            writer.writerows(dataarray)
        return NumberOfDelete

    def ChangePassword(self, OldPassword: str, NewPassword: str):
        ''' A Method To change password of current login '''
        UserName = LoginService.__LoginData[USERNAME]
        with open( LOGINDATA ,mode='r') as file :
            reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])        
            dataarray = []
            for data in reader :
                if self.DecryptData(data[USERNAME]) == UserName :
                    if self.DecryptData(data[PASSWORD]) == OldPassword :
                        data[PASSWORD] = self.EncryptData(NewPassword)
                        LoginService.__LoginData[PASSWORD] = NewPassword
                    else : raise IncorrectPasswordException
                dataarray.append(data) 

        with open( LOGINDATA , mode='w') as file:
            writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            writer.writerows(dataarray)    
        
    def GetPasswordFromUserName(self, UserName: str):
        ''' Return LoginData From UserName'''
        
        with open( LOGINDATA ,mode='r') as file:
            reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            for data in reader :
                if self.DecryptData(data[USERNAME]) == UserName :
                    return {
                            USERNAME: self.DecryptData(data[USERNAME]),
                            PASSWORD: self.DecryptData(data[PASSWORD]),
                            LEVELORADMIN: self.DecryptData(data[LEVELORADMIN])
                            }
            else : 
                raise UsernameNotFoundException
        
    def EncryptData(self , data: str ):
        ''' A Method To Encrypt Data Before Writing It To File '''
        return base64.b64encode(data.encode()).decode()
    
    def DecryptData(self, data ):
        ''' A Method To Decrypt Data After Readinging It from the File '''
        return base64.b64decode(data).decode()
