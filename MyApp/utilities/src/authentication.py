import os
from tkinter import messagebox
import services
from utilities.exception import IncorrectPasswordException, UsernameNotFoundException
from utilities.constants import TITLE, LEVELORADMIN, ADMIN, ADMINSTATE, USERSTATE, LOGINSTATE
from utilities.src.driveworkbook import download_all_workbook


def authentatic_credentials(Username: str, Password: str):
    if Username.strip() == '' or Password.strip() == '' :
        messagebox.showerror('Error','All Fields Required')
        return LOGINSTATE

    try :  
        _loginService = services.LoginService()
        _driveService = services.DriveService()

        LoginData = _loginService.TryLogin(UserName=Username, Password=Password)
        _driveService.setVariable(Username)

        os.mkdir(_driveService.FOLDER.get(TITLE))
        download_all_workbook()
        if LoginData[LEVELORADMIN] == ADMIN:
             return ADMINSTATE
        else :
             return USERSTATE
    except IncorrectPasswordException :
        messagebox.showerror('Error','Incorrect Password')
        return LOGINSTATE
    except UsernameNotFoundException :
        messagebox.showerror('Error','Username Not Found')
        return LOGINSTATE
    except Exception as e:
        messagebox.showerror('Error',f'Unable To Login')
        return LOGINSTATE
