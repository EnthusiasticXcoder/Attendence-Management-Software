from tkinter import messagebox
from threading import Thread

from utilits import Drive_uplode, encript



def deletentry(userid,loginname):
    try:
        if userid ==" " or userid == "" or userid=="admin" :
            messagebox.showerror("Error","All fields are required")
            return
        if loginname==userid :
            messagebox.showerror("Error","Unable To Delete Active User")
            return
        
        admin=True

        with open("users/logindata.dat","rb") as f :
            data=f.readlines()
            
        with open("users/logindata.dat","wb") as f :
            for info in data:
                decoded=encript.decode64(info)
                if userid in decoded:
                    decoded=decoded.split(" ")
                    if userid == decoded[1] or userid == decoded[0]:
                        admin=False
                        if decoded[0] =='admin':
                            Thread(target=Drive_uplode.dfolder,args=(userid,)).start()
                        continue     
                f.write(info)
        if admin :
            messagebox.showerror("Error","Username not found")
            return
        Thread(target=Drive_uplode.upload_files , args=('user','logindata.dat')).start()
        messagebox.showinfo("Sucess",f"Entry deleted sucessfully By Username : {decoded[1]}")       
    except:
        messagebox.showerror("Error","Unknown error")