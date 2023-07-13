import csv
import base64

import smtplib
from email.message import EmailMessage
import ssl


USERNAME = 'Username'
PASSWORD = 'Password'
LEVELORADMIN = 'LevelorAdmin'
ADMIN = 'Admin'
SUBJECT = 'Request to forgot passward'
BODY = '''
    This mail is with the regards to the request to forget password 
    made by a user of Attendence software .
    the username and password for the same are given below .
    '''

class InstanceAlreadyCreatedException(Exception) :
    ''' Exception when someone directly calls the initialiser'''

class IncorrectPasswordException(Exception) :
    ''' Exception when Password dosen't match with the password corrosponding with the Username'''
    
class UsernameNotFoundException(Exception) :
    ''' Exception when Username dosen't exist in logindata.csv file'''

class UnableToDeleteException(Exception) :
    ''' Exception raised when unable to Delete'''

class CannotDeleteCurrentLoginUserException(Exception) :
    ''' Exception raised when Given Username Is Cuttent Login Username '''

class LoginService:
    __instance = None
    __LoginData = None

    @staticmethod
    def getInstance():
        if LoginService.__instance is None:
            LoginService()
        return LoginService.__instance

    def __init__(self) -> None:
        if LoginService.__instance is not None:
            raise InstanceAlreadyCreatedException
        LoginService.__instance = self
    
    def TryLogin(self , UserName: str , Password: str ):
        ''' A Method for trying to LogIn using given Credentials 
         Return LoginData '''
        
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
               
    def CreateLogin(self , UserName: str , Password: str , isadmin: bool = False ):
        ''' A Method To Create Login And Append Login Data To The logindata.csv File'''
        if isadmin : 
            level =ADMIN
        else : 
            level = LoginService.__LoginData[USERNAME]
        
        with open('logindata.csv',mode='a') as file:
            writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            writer.writerow({
                    USERNAME : self.EncryptData(UserName),
                    PASSWORD : self.EncryptData(Password),
                    LEVELORADMIN : self.EncryptData(level)})
        
    def CheackUserName(self , UserName: str):
        ''' Method to cheack wether the username is valid or not 
        Return True for Vaild Username and False for invalid UserName'''
        with open('logindata.csv',mode='r') as file:
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
    
        with open('logindata.csv',mode='r') as file :
            reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN]) 
            dataarray = []
            for data in reader :
                if self.DecryptData(data[USERNAME]) == UserName or self.DecryptData(data[LEVELORADMIN]) == UserName :
                    NumberOfDelete += 1
                    continue
                dataarray.append(data)

        if NumberOfDelete == 0 : 
            raise UnableToDeleteException

        with open('logindata.csv', mode='w') as file:
            writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            writer.writerows(dataarray)
        return NumberOfDelete

    def ChangePassword(self, OldPassword: str, NewPassword: str):
        ''' A Method To change password of current login '''
        UserName = LoginService.__LoginData[USERNAME]
        with open('logindata.csv',mode='r') as file :
            reader = csv.DictReader(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])        
            dataarray = []
            for data in reader :
                if self.DecryptData(data[USERNAME]) == UserName :
                    if self.DecryptData(data[PASSWORD]) == OldPassword :
                        data[PASSWORD] = self.EncryptData(NewPassword)
                        LoginService.__LoginData[PASSWORD] = NewPassword
                    else : raise IncorrectPasswordException
                dataarray.append(data) 

        with open('logindata.csv', mode='w') as file:
            writer = csv.DictWriter(file,fieldnames=[USERNAME , PASSWORD , LEVELORADMIN])
            writer.writerows(dataarray)    
        

    def GetPasswordFromUserName(self, UserName: str):
        ''' Return LoginData From UserName'''
        
        with open('logindata.csv',mode='r') as file:
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
    
    def send_Email(self,data):
        ''' Function to send email '''
        email_sender=' Sender Email Address'
        email_password= " Secreat Password"
        email_receiver = 'Reciver Email Address'
       
        email = EmailMessage()

        email['From'] = email_sender
        email['To'] = email_receiver
        email['Subject']= SUBJECT

        content = BODY + f'{data}'
        email.set_content(content)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail (email_sender, email_receiver, email.as_string())

        return email_receiver
        
    def EncryptData(self , data: str ):
        ''' A Method To Encrypt Data Before Writing It To File '''
        return base64.b64encode(data.encode()).decode()
    
    def DecryptData(self, data ):
        ''' A Method To Decrypt Data After Readinging It from the File '''
        return base64.b64decode(data).decode()
