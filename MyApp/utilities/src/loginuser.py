from tkinter import messagebox

import services
import utilities

from utilities.exception import (
    IncorrectPasswordException, 
    CannotDeleteCurrentLoginUserException, 
    UnableToDeleteException )

from utilities.constants import CREATENEWADMIN, CREATENEWUSER


def create_new_login(Username: str, Password: str, ConfirmPassword: str, Level: str):
    if Username.strip() == '' or Password.strip() == '' or ConfirmPassword.strip() == '':
        return messagebox.showerror('Error','All Fields Are Required')

    if Password != ConfirmPassword :
        return messagebox.showerror('Error','New Password And Confirm New Password Are Not Same')
    
    try :
        loginservice = services.LoginService()
        if loginservice.CheackUserName(Username):
            if Level == CREATENEWADMIN :
                loginservice.CreateLogin(UserName=Username, Password=Password, isadmin= True)
                utilities.create_new_folder(Username)
            elif Level == CREATENEWUSER :
                loginservice.CreateLogin(UserName=Username, Password=Password)
            
            utilities.upload_logindata()
            messagebox.showinfo('Sucess','New Login Credentials Entered Successfully')
        else : 
            return messagebox.showerror('Error','Username Exists Try Another Username')
    except Exception :
        return messagebox.showerror('Error','Unable To Create New User')
    
def change_password(OldPassword: str, NewPassword: str, ConfirmPassword: str):
    if OldPassword.strip() == '' or NewPassword.strip() == '' or ConfirmPassword.strip() == '':
        return messagebox.showerror('Error','All Fields Are Required')

    if OldPassword == NewPassword :
        return messagebox.showerror('Error','Old Password And New Password Must Be Different')
        
    if NewPassword != ConfirmPassword :
        return messagebox.showerror('Error','New Password And Confirm New Password Are Not Same')
    
    try :
        loginservice = services.LoginService()
        loginservice.ChangePassword(OldPassword=OldPassword, NewPassword=NewPassword)
        
        utilities.upload_logindata()
        messagebox.showinfo('Sucess','Password Changed Successfully')
    except IncorrectPasswordException :
        return messagebox.showerror('Error','Incorrect Password')
    except Exception :
        return messagebox.showerror('Error','Unable To Change Password')
    
def delete_user(Username: str):
    if Username.strip() == '':
        return messagebox.showerror('Error','All Fields Are Required')

    try :
        service = services.LoginService()
        service.DeleteUser(UserName=Username) 
        
        utilities.upload_logindata()
        utilities.delete_folder(Username)

        messagebox.showinfo(f'Username: {Username} Deleted Sucessfully')
    except CannotDeleteCurrentLoginUserException :
        return messagebox.showerror('Cannot Delete Current Login User')
    except UnableToDeleteException :
        return messagebox.showerror('Error','Unable To Delete User')
    except Exception :
        return messagebox.showerror('Error','Unable To Delete User')
    
