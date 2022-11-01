from threading import Thread
from tkinter import messagebox

from utilits import Drive_uplode, encript 


def login(userid,passward):
    try:
        if userid ==" " or passward==" ":
            return True , True
        if userid =="" or passward=="":
            return True , True
        with open("users/logindata.dat","rb") as f:
            for login in f.readlines() :
                decoded=encript.decode64(login)
                decoded=decoded.split(" ")
                
                if decoded[0] == 'admin' and userid == decoded[1] and passward == decoded[2] :
                    return decoded[1],'admin'
                elif decoded[0] != 'admin' and userid == decoded[1] and passward == decoded[2] :
                    return decoded[0],'login'
        return False , False
    except :
        messagebox.showerror("Error","Unknown login error")

def changepass(userid,password,newpassward,cnewpassward,pass_entry):
    try:
        if newpassward != cnewpassward :
            messagebox.showerror("Error","passward and confirm passward should be same")
            return
        if password ==" " or newpassward==" " :
            messagebox.showerror("Error","All Fields Are Required")
            return
        
        if password == "" or newpassward== "" :
            messagebox.showerror("Error","All Fields Are Required")
            return
        
        with open("users/logindata.dat","rb") as f:
            data=f.readlines()
        
        with open("users/logindata.dat","wb") as f :
            for info in data:
                decoded=encript.decode64(info)
                decoded = decoded.split(" ")
                if userid == decoded[1] and password == decoded[2]:
                    level = decoded[0]
                    continue
                f.write(info)
            
            write=f'{level} {userid} {newpassward}'
            encoded=encript.encode64(write)
            f.write(encoded)

        with open("users/logindata.dat","a") as f :
            f.write(" \n")

        pass_entry.delete(0,"end")
        pass_entry.insert(0,newpassward)
        messagebox.showinfo("Sucess","Password change sucessfully")
        Thread(target=Drive_uplode.upload_files ,args=('user','logindata.dat')).start()     
    except:
        messagebox.showerror("Error","Unknown change error ")
