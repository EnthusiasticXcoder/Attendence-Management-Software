import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from threading import Thread

try:
    from utilits import Drive_uplode
    from static import ExcelTopup
except: pass


class DownloadFrame(ctk.CTkFrame):
    def __init__(self, *args, Path,Function,
                 bg_color=None, 
                 fg_color=('#C0C2C5','#343638'), 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
                 width=200, height=200, 
                 overwrite_preferred_drawing_method: str = None, 
                 **kwargs):

        super().__init__(*args, bg_color=bg_color, 
                         fg_color=fg_color, 
                         border_color=border_color, 
                         border_width=border_width, 
                         corner_radius=corner_radius,
                         width=width, height=height, 
                         overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                         **kwargs)
        tk.Frame(self,width=300,height=2,bg="black").grid(row=0,column=0,columnspan=3,sticky='w')
        self.green = self.loadPhoto("images/green.png",35)
        self.red= self.loadPhoto("images/x red.png",35)
        wb=Path.split("/")[-1]
        folder=Path.split("/")[-2]
        ctk.CTkLabel(master=self,text=wb,fg_color=('#C0C2C5','#343638'),text_font=("times new roman",15)).grid(row=1,column=0)
        ctk.CTkButton(master=self,text="",
                        fg_color=('#C0C2C5','#343638'),
                        image=self.green,width=40,border_width=2,
                        command=lambda:ExcelTopup.See_Excel(Path)).grid(row=1,column=1,padx=3)
        ctk.CTkButton(master=self,text="",
                        fg_color=('#C0C2C5','#343638'),
                        image=self.red,width=40,border_width=2,
                        command=lambda:Thread(target=Drive_uplode.DeleteFile,args=(folder,wb,Function)).start()).grid(row=1,column=2)
        tk.Frame(self,width=300,height=2,bg="black").grid(row=2,column=0,columnspan=3,sticky='w')

    def loadPhoto(self,path,size):
        return ImageTk.PhotoImage(Image.open(path).resize((size,size)))

class MenuFrame(ctk.CTkFrame):
    def __init__(self, *args, Level,
                 bg_color=None, 
                 fg_color="default_theme", 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
                 width=200, height=200, 
                 overwrite_preferred_drawing_method: str = None, 
                 **kwargs):

        super().__init__(*args, bg_color=bg_color, 
                         fg_color=fg_color, 
                         border_color=border_color, 
                         border_width=border_width, 
                         corner_radius=corner_radius,
                         width=width, height=height, 
                         overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                         **kwargs)

        if Level=='admin':
            Level=True
        elif Level=='login':
            Level=False

        Buttonarray=[]

        self.grid_rowconfigure(1, minsize=20)   # empty row with minsize as spacing
        self.grid_rowconfigure(12, weight=1)  # empty row as spacing
        self.grid_rowconfigure(14, minsize=15)    # empty row with minsize as spacing
        self.grid_rowconfigure(16, minsize=10)

        self.grid_columnconfigure(2, minsize=15)


        self.HomeButton = ctk.CTkButton(master=self,text="Home")
        Buttonarray.append(self.HomeButton)
        
        self.NewSheetButton = ctk.CTkButton(master=self,text="Create New Sheet")
        Buttonarray.append(self.NewSheetButton)
        
        if Level :
            self.ImportWbButton = ctk.CTkButton(master=self,text="Import Workbook")
            Buttonarray.append(self.ImportWbButton)

        self.EnterExcelButton = ctk.CTkButton(master=self,text="Enter Attendence")
        Buttonarray.append(self.EnterExcelButton)

        self.DownloadExcelButton = ctk.CTkButton(master=self,text="Download Excel")
        Buttonarray.append(self.DownloadExcelButton)

        if Level :
            self.CreateAdminButton = ctk.CTkButton(master=self,text="Create New Admin")
            Buttonarray.append(self.CreateAdminButton)

            self.CreateUserButton = ctk.CTkButton(master=self,text="Create New User")
            Buttonarray.append(self.CreateUserButton)

        self.ChangePasswordButton = ctk.CTkButton(master=self,text="Change Password")
        Buttonarray.append(self.ChangePasswordButton)

        if Level :
            self.DeleteEntryButton = ctk.CTkButton(master=self,text="Delete Entry")
            Buttonarray.append(self.DeleteEntryButton)

        self.LogOutButton = ctk.CTkButton(master=self,text="Log Out")
        Buttonarray.append(self.LogOutButton)

        ModeChange = ctk.CTkOptionMenu(master=self,
                                            values=["Light", "Dark", "System"],
                                            command=ctk.set_appearance_mode)

        self.imgmenu = self.loadImage("images/menu.png",35)
        self.imgx = self.loadImage("images/x.png",35)
        
        self.imghome=self.loadImage("images/home.png",35)
        self.imgsheet=self.loadImage("images/file-plus.png",35)
        self.imgdown=self.loadImage("images/arrow-down-circle.png",35)
        self.imgenter=self.loadImage("images/edit.png",35)
        self.imgshow=self.loadImage("images/file-text.png",35)
        self.imgcreate=self.loadImage("images/user-plus.png",35)
        self.imgroup=self.loadImage("images/users.png",35)
        self.imgchange=self.loadImage("images/change.webp",35)
        self.imgdel=self.loadImage("images/delete.png",35)
        self.imglogout=self.loadImage("images/log-out.png",35)

        Labelarray=[]
        self.HomeLabel=ctk.CTkButton(self,image=self.imghome,fg_color='sky blue3',text="",width=40)
        Labelarray.append(self.HomeLabel)
        self.SheetLabel=ctk.CTkButton(self,image=self.imgsheet,fg_color='sky blue3',text="",width=40)
        Labelarray.append(self.SheetLabel)
        if Level :
            self.DownLabel=ctk.CTkButton(self,image=self.imgdown,fg_color='sky blue3',text="",width=40)
            Labelarray.append(self.DownLabel)
        self.EnterLabel=ctk.CTkButton(self,image=self.imgenter,fg_color='sky blue3',text="",width=40)
        Labelarray.append(self.EnterLabel)
        self.ShowLabel=ctk.CTkButton(self,image=self.imgshow,fg_color='sky blue3',text="",width=40)
        Labelarray.append(self.ShowLabel)
        if Level :
            self.CreateLabel=ctk.CTkButton(self,image=self.imgcreate,fg_color='sky blue3',text="",width=40)
            Labelarray.append(self.CreateLabel)
            self.GroupLabel=ctk.CTkButton(self,image=self.imgroup,fg_color='sky blue3',text="",width=40)
            Labelarray.append(self.GroupLabel)
        self.ChangeLabel=ctk.CTkButton(self,image=self.imgchange,fg_color='sky blue3',text="",width=40)
        Labelarray.append(self.ChangeLabel)
        if Level :
            self.DeleteLabel=ctk.CTkButton(self,image=self.imgdel,fg_color='sky blue3',text="",width=40)
            Labelarray.append(self.DeleteLabel)
        self.LogoutLabel=ctk.CTkButton(self,image=self.imglogout,fg_color='sky blue3',text="",width=40)
        Labelarray.append(self.LogoutLabel)

        self.ModeSwitch = ctk.CTkSwitch(master=self,text="",command=self.change_mode)

        for i,imglabel in enumerate(Labelarray):
            imglabel.grid(row=i+2,column=0,padx=20,pady=8)
        self.ModeSwitch.grid(row=15, column=0, pady=20, padx=20)

        def close(e):
            label.configure(image=self.imgmenu)
            label.bind("<Button-1>",open)
            for button in Buttonarray:
                button.grid_forget()
            ModeChange.grid_forget()
            self.configure(width=100)
            for i,imglabel in enumerate(Labelarray):
                imglabel.grid(row=i+2,column=0,padx=20,pady=8)
            self.ModeSwitch.grid(row=15, column=0, pady=20, padx=20)

        def open(e):
            label.configure(image=self.imgx)
            label.bind("<Button-1>",close)
            for imglabel in Labelarray:
                imglabel.grid_forget()
            self.ModeSwitch.grid_forget()
            for row , button in enumerate(Buttonarray):
                button.grid(row=row+2, column=1, pady=7, padx=20)
            ModeChange.grid(row=15, column=1, pady=10, padx=20, sticky="w")
            
        label=tk.Label(self,image=self.imgmenu,bg=fg_color,cursor='hand2')
        label.grid(row=0,column=0,sticky='w',padx=20)
        label.bind("<Button-1>",open)
        
    def loadImage(self,path,size):
        return ImageTk.PhotoImage(Image.open(path).resize((size,size)))

    def change_mode(self):
        if self.ModeSwitch.get() == 0:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


class AdminFrame(ctk.CTkFrame):
    def __init__(self, *args,Level,Username,
                 bg_color=None, 
                 fg_color="sky blue3", 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
                 width=200, height=200, 
                 overwrite_preferred_drawing_method: str = None, 
                 **kwargs):

        super().__init__(*args, bg_color=bg_color, 
                         fg_color=fg_color, 
                         border_color=border_color, 
                         border_width=border_width, 
                         corner_radius=corner_radius,
                         width=width, height=height, 
                         overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                         **kwargs)
         
        UpperFrame = ctk.CTkFrame(master=self,fg_color=fg_color,corner_radius=0)
        UpperFrame.place(x=0,y=0,relheight=0.163,relwidth=1)
        
        UpperFrame.grid_columnconfigure(0, weight=0)
        UpperFrame.grid_columnconfigure(1, weight=10)
        
        self.img= tk.PhotoImage(file='images\logoies.png') 
        label=tk.Label(UpperFrame,image=self.img,bg=fg_color)
        label.grid(row=0,column=0,sticky='n')
        
        Frame=ctk.CTkFrame(master=UpperFrame,fg_color=fg_color)
        Frame.grid(row=0,column=1,sticky='nsew')
        
        NameFrame=ctk.CTkFrame(master=Frame,fg_color=fg_color)
        NameFrame.pack(side=tk.RIGHT,padx=20,ipadx=50)
        NameLabel=ctk.CTkLabel(master=NameFrame,text="Login as : ",text_color='black',
                                text_font=('Goudy old style',13,"bold"),anchor='w')
        NameLabel.pack()
        NameLabel=ctk.CTkLabel(master=NameFrame,text=Username,text_font=('Goudy old style',18,"bold"),text_color='red')
        NameLabel.pack()

# ============ create two frames ============
        BottomFrame = ctk.CTkFrame(master=self,fg_color=fg_color)
        BottomFrame.place(x=0,rely=0.163,relheight=0.839,relwidth=0.9995)

        BottomFrame.grid_columnconfigure(1, weight=1)
        BottomFrame.grid_rowconfigure(0, weight=1)

        self.ToggelFrame=MenuFrame(master=BottomFrame,fg_color=fg_color,Level=Level,width=310,corner_radius=0)
        self.ToggelFrame.grid(row=0, column=0,sticky='nsew')
        
        self.MainFrame = ctk.CTkFrame(master=BottomFrame)
        self.MainFrame.grid(row=0, column=1, sticky="nswe")

        self.ToggelFrame.HomeButton.configure(command= lambda:self.Home(BottomFrame))
        self.ToggelFrame.HomeLabel.configure(command= lambda:self.Home(BottomFrame))

        self.right = ImageTk.PhotoImage(Image.open("images/right.png").resize((35,35)))
        self.pointerimg=ctk.CTkLabel(self.ToggelFrame,image=self.right,width=20,fg_color='sky blue3')
        self.downloadmenu=None

        self.BindConfigure()
        
        Thread(target=self.Configmenu,args=(Username,)).start()
    
    def Home(self,frame):
        self.MainFrame.destroy()
        self.MainFrame = ctk.CTkFrame(master=frame)
        self.MainFrame.grid(row=0, column=1, sticky="nswe")

    def Configmenu(self,folder):
        self.downloadmenu=ctk.CTkFrame(master=self,fg_color=('#C0C2C5','#343638'))
        self.downloadmenu.grid_rowconfigure(0,minsize=10)
        sheets=Drive_uplode.DStoreID.Files if Drive_uplode.DStoreID!=None else Drive_uplode.get_files(folder)
        if sheets==[]:
            ctk.CTkLabel(master=self.downloadmenu,text=" --- NO FILE TO DOWNLOAD ---").grid(row=0,column=0)
            return
        for i,wb in enumerate(sheets):
            path='workbooks/{0}/{1}'.format(folder,wb['title'])
            DownloadFrame(master=self.downloadmenu,Path=path,Function=self).grid(row=i+1,column=0)
        self.downloadmenu.grid_rowconfigure(i+2,minsize=10)
         
    def ShowDownload(self):
        self.bind_all('<Button-1>',self.HideDownload)
        self.update()
        y=self.ToggelFrame.DownloadExcelButton.winfo_rooty()-self.winfo_rooty() if self._widget_scaling==1 and self.ToggelFrame.winfo_width()>150 \
            else self.ToggelFrame.ShowLabel.winfo_rooty()-self.winfo_rooty() if self._spacing_scaling==1 and self.ToggelFrame.winfo_width()<150 \
            else self.ToggelFrame.DownloadExcelButton.winfo_rooty()-self.winfo_rooty()-91 if self.ToggelFrame.winfo_width()>150 \
            else self.ToggelFrame.DownLabel.winfo_rooty()-self.winfo_rooty()
        x=62 if self._spacing_scaling==1 and self.ToggelFrame.winfo_width()<150 else 240 if self._spacing_scaling==1 and self.ToggelFrame.winfo_width()>150 else 60 if self.ToggelFrame.winfo_width()<150 else 222
        yb=290 if self._spacing_scaling==1 and self.ToggelFrame.winfo_width()<150 else 230 if self._spacing_scaling==1 and self.ToggelFrame.winfo_width()>150 else 250 if self.ToggelFrame.winfo_width()<150 else 222
        self.pointerimg.place(x=x,y=yb)
        self.downloadmenu.place(x=x+29,y=y)
    
    def HideDownload(self,e=None):
        self.pointerimg.place_forget()
        self.downloadmenu.place_forget()
        self.unbind_all('<Button-1>')
    
    def BindConfigure(self):
        '''   Show Lables Of Image Buttons Bind Functions of Image Buttons --------------------------------
        -------------------------------------------------------------------------------------------------'''
        
        showlabel=ctk.CTkLabel(master=self,text="",fg_color="#2A2D2E",text_color='white',
                                anchor='center',height=18,width=70,text_font=("Helvetica", 9),
                                corner_radius=5,justify='center')
        
        def hide(e):
            showlabel.place_forget()

        def home(e1):
            showlabel.configure(text='Home')
            showlabel.place(x=10,y=self.ToggelFrame.HomeLabel.winfo_rooty()+20)
        def sheet(e1):
            showlabel.configure(text='Create\nSheet')
            showlabel.place(x=10,y=self.ToggelFrame.SheetLabel.winfo_rooty()+20)
        def down(e1):
            showlabel.configure(text='Import\nWorkbook')
            showlabel.place(x=10,y=self.ToggelFrame.DownLabel.winfo_rooty()+20)
        def enter(e1):
            showlabel.configure(text='Enter\nAttendence')
            showlabel.place(x=10,y=self.ToggelFrame.EnterLabel.winfo_rooty()+20)
        def show(e1):
            showlabel.configure(text='Download\nExcel')
            showlabel.place(x=10,y=self.ToggelFrame.ShowLabel.winfo_rooty()+20)
        def Create(e1):
            showlabel.configure(text='Create\nNew Admin')
            showlabel.place(x=10,y=self.ToggelFrame.CreateLabel.winfo_rooty()+20)
        def group(e1):
            showlabel.configure(text='Create\nNew User')
            showlabel.place(x=10,y=self.ToggelFrame.GroupLabel.winfo_rooty()+20)
        def change(e1):
            showlabel.configure(text='Change\nPassword')
            showlabel.place(x=10,y=self.ToggelFrame.ChangeLabel.winfo_rooty()+20)
        def delete(e1):
            showlabel.configure(text='Delete\nEntry')
            showlabel.place(x=10,y=self.ToggelFrame.DeleteLabel.winfo_rooty()+20)
        def logout(e1):
            showlabel.configure(text='Log Out')
            showlabel.place(x=10,y=self.ToggelFrame.LogoutLabel.winfo_rooty()+20)
        def swich(e1):
            showlabel.configure(text='Mode Switch')
            showlabel.place(x=10,y=self.ToggelFrame.ModeSwitch.winfo_rooty()-43)

        self.ToggelFrame.HomeLabel.bind('<Enter>',home)
        self.ToggelFrame.HomeLabel.bind('<Leave>',hide)
            
        self.ToggelFrame.SheetLabel.bind('<Enter>',sheet)
        self.ToggelFrame.SheetLabel.bind('<Leave>',hide)
            
        try :
            self.ToggelFrame.DownLabel.bind('<Enter>',down)
            self.ToggelFrame.DownLabel.bind('<Leave>',hide)
        except:pass
            
        self.ToggelFrame.EnterLabel.bind('<Enter>',enter)
        self.ToggelFrame.EnterLabel.bind('<Leave>',hide)

        self.ToggelFrame.ShowLabel.bind('<Enter>',show)
        self.ToggelFrame.ShowLabel.bind('<Leave>',hide)

        try:
            self.ToggelFrame.CreateLabel.bind('<Enter>',Create)
            self.ToggelFrame.CreateLabel.bind('<Leave>',hide)

            self.ToggelFrame.GroupLabel.bind('<Enter>',group)
            self.ToggelFrame.GroupLabel.bind('<Leave>',hide)
        except: pass

        self.ToggelFrame.ChangeLabel.bind('<Enter>',change)
        self.ToggelFrame.ChangeLabel.bind('<Leave>',hide)

        try:
            self.ToggelFrame.DeleteLabel.bind('<Enter>',delete)
            self.ToggelFrame.DeleteLabel.bind('<Leave>',hide)
        except : pass

        self.ToggelFrame.LogoutLabel.bind('<Enter>',logout)
        self.ToggelFrame.LogoutLabel.bind('<Leave>',hide)

        self.ToggelFrame.ModeSwitch.bind('<Enter>',swich)
        self.ToggelFrame.ModeSwitch.bind('<Leave>',hide)

        

        

        
if __name__=="__main__":
    r=ctk.CTk()
    r.title("CustomTkinter complex_example.py")
    r.state('zoomed')

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

    set_Scaling(r)
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")

    r.rowconfigure(0, weight=1)
    r.columnconfigure(0, weight=1)
    # ============ create two frames ============
    self=AdminFrame(master=r,Level='admin',Username="Anshul_verma")
    self.grid(row=0, column=0, sticky="nswe")

    self.ToggelFrame.DownloadExcelButton.configure(command=lambda:self.ShowDownload())
    self.ToggelFrame.ShowLabel.configure(command=lambda: self.ShowDownload())

    
    r.mainloop()
