from shutil import rmtree
import customtkinter as ctk
from threading import Thread

from static.pages import Loginpage as page 

from utilits import Drive_uplode


class Fmain(ctk.CTk):

    __SCALING = 1
    __X= 1350 
    __Y=850

    def __init__(self, *args, fg_color=None, **kwargs):
        ctk.set_appearance_mode('dark')
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        self.logout=False
        self.iconbitmap('images\MetroUI-Apps-Notepad-icon.ico')
        self.title("Attendence")
        self.wm_geometry('1350x850+250+70')
        self.wm_minsize(Fmain.__X,Fmain.__Y)
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
            ctk.set_widget_scaling(scal)
            ctk.set_window_scaling(scal)
        Fmain.__SCALING = factor
    
    def increment_scaling_event(self, new_scaling):
        Fmain.__SCALING+=0.1
        new_scaling_float = Fmain.__SCALING
        ctk.set_widget_scaling(new_scaling_float)
    
    def decrement_scaling_event(self, new_scaling):
        Fmain.__SCALING-=0.1
        new_scaling_float = Fmain.__SCALING
        ctk.set_widget_scaling(new_scaling_float)


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