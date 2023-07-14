from tkinter import messagebox

import services


def send_mail(Username: str):
    acknowledgement = messagebox.askyesno('Forget passward','Are You Shure Want To Forget Passward')

    if acknowledgement is True :
        if Username.split() == '' :
            return messagebox.showerror('Error','Username Required')
        loginservice = services.LoginService()
        logindata = loginservice.GetPasswordFromUserName(Username)
        email_receiver = services.send_email(logindata)
        messagebox.showinfo("Password send",f"Password is been mailed to your admin at {email_receiver}")
