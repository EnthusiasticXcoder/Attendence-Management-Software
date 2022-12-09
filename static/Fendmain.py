from shutil import rmtree
import customtkinter as ctk
from threading import Thread

from static.pages import Loginpage as page 

from utilits import Drive_uplode


class Fmain(ctk.CTk):
    def __init__(self, *args, fg_color="default_theme", **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.logout=False
        self.iconbitmap('images\MetroUI-Apps-Notepad-icon.ico')
        self.title("Attendence")
        self.wm_geometry('1342x814+235+66')
        self.wm_minsize(1340,810)
        self.state('zoomed')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.Login=page.LoginFrame(master=self)
        self.Login.grid(row=0, column=0, sticky='nsew')

        self.set_Scaling()
        
        self.Login.tkraise()
    
        
    def log_out(self,stor):
        self.logout=True
        self.end(stor)
        self.Login.Password.delete(0,"end")
        self.Login.tkraise()
    
    def end(self,stor):
        Thread(target=Drive_uplode.upload_files).start()
        def upload(folder):
            Drive_uplode.upload_files(folder=folder)
            rmtree(f"workbooks/{folder}")
        Thread(target=upload,args=(stor.admin_name,)).start()
    
    

    def set_Scaling(self):
        factor=1.25 if self.winfo_height()> 1000 and self.winfo_width()>1900 else 1
        scal=ctk.ScalingTracker.get_window_scaling(self)
        if scal==factor:
            return
        else:
            scal=factor/scal
            ctk.set_spacing_scaling(scal)
            ctk.set_widget_scaling(scal)
            ctk.set_window_scaling(scal)


if __name__=="__main__":
    r=ctk.CTk()
    r.title("CustomTkinter complex_example.py")
    r.state('zoomed')

    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")

    r.rowconfigure(0, weight=1)
    r.columnconfigure(0, weight=1)
        # ============ create two frames ============
    
    r.mainloop()



