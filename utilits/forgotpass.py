import smtplib
from email.message import EmailMessage
import ssl
from tkinter import messagebox

from utilits import encript


def forgot(userid):
    try:
        if messagebox.askyesno("Forget passward","Are You Shure Want To Forget Passward"):
            if userid =="" or userid==" ":
                messagebox.showerror("Error","Username required")
                return

            with open("users/logindata.dat","rb") as f :
                for info in f.readlines() :
                    decoded=encript.decode64(info)
                    if userid in decoded :
                        key=decoded
                        break
            arr=key.split(" ")
            password=arr[-1]
            sendmail(userid,password)
        else: 
            return
    except:
        messagebox.showerror("Error","Unable to forgot password")

def sendmail(userid,password):
    email_sender='attendence.login2022@gmail.com'
    email_password= "xzqv ekbm roax auqi"
    email_receiver = 'vkgupta.419@gmail.com'

    subject = "Request to forgot passward"

    body=f'''
This mail is with the regards to the request to forget password 
made by a user of Attendence softwate .
the username and password for the same are given below .

Username : {userid}
password : {password}

'''
    en=EmailMessage()

    en['From'] = email_sender
    en['To'] = email_receiver
    en['Subject']= subject
    en.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail (email_sender, email_receiver, en.as_string())
        messagebox.showinfo("Password send",f"Password is been mailed to your admin at {email_receiver}")

