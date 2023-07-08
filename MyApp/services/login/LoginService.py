import csv
import base64

from services.login.LoginExceptions import IncorrectPasswordException, InstanceAlreadyCreatedException ,UnableToCreateNewUserException, UnableToDeleteException, UnableToLoginException , UsernameNotFoundException

USERNAME = 'Username'
PASSWORD = 'Password'
LEVELORADMIN = 'LevelorAdmin'


class LoginService:
    __instance = None
    __LoginData = None

    @staticmethod
    def getInstance():
        if LoginService.__instance == None:
            LoginService()
        return LoginService.__instance

    def __init__(self) -> None:
        if LoginService.__instance != None:
            raise InstanceAlreadyCreatedException
        LoginService.__instance = self
    
    def TryLogin(self , UserName: str , Password: str ):
        ''' A Method for trying to LogIn using given Credentials 
         Return LoginData '''
        try :
            with open('logindata.csv',mode='r') as file:
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
        except Exception :
            raise UnableToLoginException
            
    def CreateLogin(self , UserName: str , Password: str , adminorlevel: str = 'Admin' ):
        ''' A Method To Create Login And Append Login Data To The logindata.csv File'''
        try :
            with open('logindata.csv',mode='a') as file:
                writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
                writer.writerow(
                    {USERNAME : self.EncryptData(UserName),
                    PASSWORD : self.EncryptData(Password),
                    LEVELORADMIN : self.EncryptData(adminorlevel)})
        except Exception :
            raise UnableToCreateNewUserException
        
    def _CheackUserName(self , UserName: str):
        ''' Method to cheack wether the username is valid or not 
        Return True for Vaild Username and False for invalid UserName'''
        try :
            with open('logindata.csv',mode='r') as file:
                reader = csv.DictReader(file,fieldnames=[USERNAME])
                usernames = [self.DecryptData(data[USERNAME]) for data in reader]
                if UserName in usernames : return False
                return True
        except Exception :
            raise FileNotFoundError
    
    def DeleteUser(self, UserName: str ):
        ''' A Method To Delete User with Username and password
        Return number of rows deleted'''
        NumberOfDelete = 0
        try :
            with open('logindata.csv',mode='r') as file :
                reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN]) 
                dataarray = []
                for data in reader :
                    if self.DecryptData(data[USERNAME]) == UserName or self.DecryptData(data[LEVELORADMIN]) == UserName :
                        NumberOfDelete += 1
                        continue
                    dataarray.append(data)
        except Exception : 
            raise FileNotFoundError

        if NumberOfDelete == 0 : 
            raise UnableToDeleteException

        try : 
            with open('logindata.csv', mode='w'):
                writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
                writer.writerows(dataarray)
            return NumberOfDelete
        except Exception :
            raise UnableToDeleteException

    def ChangePassword(self, UserName: str, OldPassword: str, NewPassword: str):
        ''' A Method To change password of current login '''
        try :
            with open('logindata.csv',mode='r') as file :
                reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN]) 
                dataarray = []
                for data in reader :
                    if self.DecryptData(data[USERNAME]) == UserName :
                        if self.DecryptData(data[PASSWORD]) == OldPassword :
                            data[PASSWORD] = self.EncryptData(NewPassword)
                            LoginService.__LoginData[PASSWORD] = NewPassword
                            break
                        else : raise IncorrectPasswordException
                    dataarray.append(data)
                else : raise UsernameNotFoundException        
        except Exception : 
            raise FileNotFoundError

    def GetPasswordFromUserName(self, UserName: str):
        ''' Return LoginData From UserName'''
        try :
            with open('logindata.csv',mode='r') as file:
                reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
                for data in reader :
                    if self.DecryptData(data[USERNAME]) == UserName :
                        return {
                                USERNAME: self.DecryptData(data[USERNAME]),
                                PASSWORD: self.DecryptData(data[PASSWORD]),
                                LEVELORADMIN: self.DecryptData(data[LEVELORADMIN])
                                }
                else : raise UsernameNotFoundException
        except Exception :
            raise FileNotFoundError
        

    def EncryptData(self , data: str ):
        ''' A Method To Encrypt Data Before Writing It To File '''
        return base64.b64encode(bytes(data, 'utf-8'))
    
    def DecryptData(self, data: str ):
        ''' A Method To Decrypt Data After Readinging It from the File '''
        return base64.b64decode(data).decode("utf-8")
      