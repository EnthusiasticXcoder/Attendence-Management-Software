import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from threading import Thread
from tkinter import messagebox
from PIL import Image, ImageTk

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from xlcalculator import ModelCompiler
from xlcalculator import Evaluator

from utilits import Drive_uplode
from static.ScrollFrame import ScrollFrame



class Cell(ctk.CTkLabel):
    def __init__(self, *args, 
                bg_color=None, 
                fg_color="default_theme", 
                text_color="default_theme", 
                corner_radius="default_theme", 
                width=140, 
                height=28, 
                text=" ", 
                text_font="default_theme", 
                anchor="nw", 
                **kwargs):

        super().__init__(*args, 
                            bg_color=bg_color, 
                            fg_color=fg_color, 
                            text_color=text_color, 
                            corner_radius=0,
                            width=int(len(str(text))*9.1), 
                            height=40, 
                            text=text, 
                            text_font=("Roboto Medium", -16,'bold'), 
                            anchor=anchor, **kwargs)

class Tabularcell(ctk.CTkEntry):
    def __init__(self, *args, text,column,maxr=False,
                bg_color=None, 
                fg_color="default_theme", 
                text_color="default_theme", 
                placeholder_text_color="default_theme", 
                text_font=('Times New Roman', 14, 'bold'), 
                placeholder_text=None, 
                corner_radius=0, 
                border_width=2, 
                border_color="default_theme", 
                width=30, 
                height=28, 
                state=tk.DISABLED, 
                textvariable: tk.Variable = None, **kwargs):

        width= 200 if column==2 else 30
        width= 50 if column in [22,31,32] else width
        width= 150 if column==1 else width 
        width= 34 if column==0 else width
        width=384 if maxr==True and column==0 else width

        textvariable=tk.StringVar(value=text)
        justify= 'left' if width==200 else 'center'

        super().__init__(*args, bg_color=bg_color, 
                        fg_color=fg_color, 
                        text_color=text_color, 
                        placeholder_text_color=placeholder_text_color, 
                        text_font=text_font, 
                        placeholder_text=placeholder_text, 
                        corner_radius=corner_radius, 
                        border_width=border_width, 
                        border_color=border_color, 
                        width=width, 
                        height=height, 
                        state=state, 
                        justify=justify,
                        textvariable=textvariable, **kwargs)


class Headcell(ctk.CTkTextbox):
    def __init__(self, *args, text,column,head=False,
                bg_color=None, 
                fg_color="default_theme", 
                border_color="default_theme", 
                border_width=10, 
                corner_radius=2, 
                text_font=('Times New Roman', 11, 'bold'), 
                text_color="default_theme", 
                width=200, height=80, **kwargs):
        
        border_color=("#565B5E",'#565B5E')
        if column<2 : text_font=('Times New Roman', 13, 'bold')
        if column==2 : text_font=('Times New Roman', 17, 'bold')
        if head:
            width= 0
        else:
            width= 200 if column==2 else 30
            width= 50 if column in [22,31,32] else width
            width= 150 if column==1 else width 
            width= 34 if column==0 else width

        height= height-25 if 2<column<22 else height
        height= height-25 if 22<column<31 else height

        height= 25 if head==True else height

        super().__init__(*args, bg_color=bg_color, 
                        fg_color=fg_color, 
                        border_color=border_color, 
                        border_width=border_width, 
                        corner_radius=corner_radius, 
                        text_font=text_font, 
                        text_color=text_color, 
                        width=width, height=height, **kwargs)

        self.insert('0.0',f"{text}")
        self.configure(state="disabled")



def Display(frame,ws,evaluator):
    MAXC=ws.max_column
    MAXR=0
    while True:
        if ws['A'+str(MAXR+10)].value == None  :
            break  
        MAXR+=1
    MAXR +=11

    frame1=ctk.CTkFrame(master=frame,width=1200)
    frame1.grid(row=0,column=0,sticky='nsew')

    indexc=[i for i in range(MAXC)]
    indexr=[i for i in range(7)]

    frame1.rowconfigure(indexr,weight=0)
    frame1.columnconfigure(indexc,weight=1)

    frame2=ctk.CTkFrame(master=frame)
    frame2.grid(row=1,column=0,sticky='nsew')

    for row in range(1,MAXR+1):
        if row in [7,8,9] : continue
        span=1
        values=[]
        merge=[]
        col=[]
            
        for column,i in enumerate(ws[str(row)]):
            if 'MergedCell' in str(i) :
                span+=1
            else:
                if column==0:
                    if row==9:
                        try:
                            arr=i.value.split("\n")
                            value=f'{arr[0]}\n{arr[1]}\n{arr[2]}'
                        except :
                            pass
                    else:
                        values.append(i.value)
                    col.append(column)
                else:
                    if column in [22,31,32] and 9<row<MAXR or row==MAXR :
                        if i.value==None:
                            values.append(i.value)
                        else:
                            alfacol=get_column_letter(column+1)
                            val = evaluator.evaluate(f'{ws.title}!{alfacol}{row}')
                            values.append(val) if val != None else values.append(0)
                    else:
                        values.append(i.value)
                    merge.append(span)
                    col.append(column)
                span=1
        merge.append(span)
    
        s= 'n' if row in[1,2,'THEORY','PRACTICAL'] else 'nw'

        table= True if row>9 else False

        if [None]*MAXC==values : 
            if table :
                row-=2
                frame2.rowconfigure(row,minsize=55)
            else: frame1.rowconfigure(row,minsize=40)
            continue

        if table:
            rowframe=ctk.CTkFrame(master=frame2,corner_radius=0)
            rowframe.grid(row=row-1,column=0,sticky='nsew')
            for value,span,column in zip(values,merge,col):
                if value == None : continue
                if value==0 and row==MAXR: continue
                maxr= True if row==MAXR else False 
                Tabularcell(master=rowframe,text=value,column=column,maxr=maxr).grid(row=0,column=column,columnspan=span,sticky=s)
        elif row<7:
            for value,span,column in zip(values,merge,col):
                if value==None : 
                    continue
                else:
                    Cell(master=frame1,text=value,corner_radius=0).grid(row=row-1,column=column,columnspan=span,sticky=s)    

    
    headframe=ctk.CTkFrame(master=frame2,corner_radius=0)
    headframe.grid(row=0,column=0,sticky='nsew')

    headframe.rowconfigure(0,weight=1)
    headframe.rowconfigure(1,weight=2)

    for column,i in enumerate(ws['8']) :
        val= " " if i.value==None else i.value
        if val in ['THEORY',"PRACTICAL"] : 
            headwidth=0
            headcell=Headcell(master=headframe,column=column,text=val,height=25,head=True)
            headcell.grid(row=0,column=column,columnspan=19,sticky='nw')
        row,span=0,1
        if column>2 and column not in [22,31,32] : row+=1
        else : span=2 

        if 2<column<22 or 22<column<31 :
            try:
                char=get_column_letter(column+1)
                val=ws[f'{char}9'].value
                if val==None : 
                    continue
                arr=val.split("\n")
                val=f'{arr[0]}\n{arr[1]}\n{arr[2]}'
                headwidth+=1
                headcell.configure(width=int(headwidth*30.42))
            except :
                continue
        Headcell(master=headframe,column=column,text=val).grid(row=row,column=column,rowspan=span,sticky='nw')

def See_Excel(WBname,root=None):
    Top=ctk.CTkToplevel(master=root)
    Top.geometry('1000x500')
    if '/' in WBname:
        folder=WBname.split("/")[-2]
        wbtitle=WBname.split("/")[-1]
    elif '\\' in WBname:
        folder=WBname.split("\\")[-2]
        wbtitle=WBname.split("\\")[-1]

    Top.title(f" SHEET  VIEW        \t\t\t\t\t\t\t\t\t\t\t{wbtitle}")
    DownloadFrame=ctk.CTkFrame(master=Top,fg_color=('#EBEBEC','#212325'))
    DownloadFrame.pack(pady=20,fill=tk.X)

    img = ImageTk.PhotoImage(Image.open("images/download.png").resize((35,35)))
    B_Download = ctk.CTkButton(master=DownloadFrame, 
                                text = "Download",
                                fg_color="green",text_color="white",image=img,
                                text_font=("times new roman",15,'bold'),
                                command= lambda : Thread(target=Drive_uplode.download_files , args=( folder , wbtitle , True)).start())  
    B_Download.pack(side=tk.RIGHT,padx=100,ipadx=50)

    # Create A Main Frame
    main_frame = ctk.CTkFrame(Top)
    main_frame.pack(fill=tk.BOTH, expand=1)

    Scroll=ScrollFrame(master=main_frame,PlaceScrollBar='Both')
    Scroll.pack(fill=tk.BOTH,expand=1)
    Scroll.updateScrollBar()

    my_notebook = ttk.Notebook(Scroll.Frame)
    my_notebook.pack(padx=10)

    style=ttk.Style()
    #style
    noteback= '#2A2D2E' if ctk.get_appearance_mode()=='Dark' else "#D1D5D8"
    tabbg= "#2B2B2B" if ctk.get_appearance_mode()=='Dark' else '#D1D5D8' 
    tabfg= "white" if ctk.get_appearance_mode()=='Dark' else 'black' 
    style.theme_use('clam')
    style.configure("TNotebook",tabmargins=[10, 1, 5 , 0],background=noteback)
    style.configure("TNotebook.Tab",padding= [1, 5] , font=('consolas italic', 14), borderwidth=[5])
    style.map("TNotebook.Tab",foreground=[("selected", tabfg), ('!active', tabfg), ('active', tabfg)],
                                 background=[("selected", "#2A73AC"), ('!active', tabbg ), ('active', "#144870")],
                                font=[("active", ('consolas italic', 14,'bold')) ,("!active", ('consolas italic', 15)),("selected", ('consolas italic', 14,'bold'))],
                                expand= [("selected", [1, 1, 1, 0])])
    style.layout("Tab",
                        [('Notebook.tab', {'sticky': 'nswe', 'children':
                            [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                [('Notebook.label', {'side': 'top', 'sticky': ''})],
                            })],
                        })]
                    ) 

    try :
        wb=load_workbook(WBname)
    except :
        messagebox.showerror("Error","Error! Unable To Open\nPlease Try Again")

    compiler = ModelCompiler()
    new_model = compiler.read_and_parse_archive(WBname)
    evaluator = Evaluator(new_model)

    for i in wb.sheetnames :
        ws=wb[i]
        frame=ctk.CTkFrame(master=my_notebook,
                            height=ws.max_row*30,
                            width=ws.max_column*43,
                            )
        frame.pack(fill=tk.BOTH, expand=1)
        my_notebook.add(frame, text=i)
        Display(frame,ws,evaluator)


if __name__=="__main__":
    
    r=ctk.CTk()
    r.title("CustomTkinter complex_example.py")
    r.state('zoomed')

    ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")
    # ============ create two frames ============
    ctk.CTkButton(master=r,command=lambda :See_Excel("workbooks/Attendence.xlsx",r)).pack()
    ModeChange = ctk.CTkOptionMenu(master=r,
                                            values=["Light", "Dark", "System"],
                                            command=ctk.set_appearance_mode)
    ModeChange.pack()

    r.mainloop()




'''
from tkinter import *
def Display(frame,ws,evaluator):
    MAXC=ws.max_column
    MAXR=0
    while True:
        if ws['A'+str(MAXR+10)].value == None  :
            break  
        MAXR+=1
    MAXR +=11
    X,Y=100,256

    
    for j,row in enumerate(ws.iter_rows( max_col=MAXC, max_row=MAXR-1)):
        value=""
        if j not in [7,8]:
            for k,i in enumerate(row):
                if  k<3 or j<8:
                    if i.value==None:
                        value += " "
                        continue
                    if j==4 and k==0 :
                        value = value+str(i.value)+"\t      "
                    elif k==1 and j>8:
                        value = value+str(i.value)+"      "
                    elif j>8 and j<18 and k==0 :
                        value = value+str(i.value)+"     "
                    else:
                        value = value+str(i.value)+"   "
            if j>8:
                j=j+1
            Label(frame,text=value,font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=X-50,y=Y-206+j*28)
    Label(frame,text="   \t      TOTAL PRESENT ",font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=X-50,y=Y-206+(MAXR)*28)
        #======================================
    
    for j,row in enumerate(ws.iter_rows( max_col=MAXC, max_row=MAXR-1)):
        for k,i in enumerate(row): 
            if j>7 and k>2:
                if k>22: k+=1
                if i.value==None:
                    continue
                elif j==8:
                    try:
                        arr=i.value.split("\n")
                        value=f'{arr[0]}\n{arr[1]}\n{arr[2]}'
                    except :
                        pass
                    Label(frame,text=value,font=('Times New Roman', 10, 'bold'),fg="black",bd=0).place(x=X+350+k*26,y=Y+26)
                    continue
                elif k==22 or k==32 or k==33 :
                    if k==32 or k==33 :
                        column=get_column_letter(k)
                    else :
                        column=get_column_letter(k+1)
                    val1 = evaluator.evaluate(f'{ws.title}!{column}{j+1}')
                    if k==33 :
                        Label(frame,text=val1,font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=X+364+(k+1)*26,y=Y-206+(j+1)*28)
                    elif k in [22,32] :
                        Label(frame,text=val1,font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=X+364+(k)*26,y=Y-206+(j+1)*28)
                    continue
                Label(frame,text=i.value,font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=X+350+k*26,y=Y-206+(j+1)*28)
    
    for i in range(3,MAXC):
        column=get_column_letter(i+1)
        val1 = evaluator.evaluate(f'{ws.title}!{column}{MAXR}')
        if val1==0:
            continue
        if i>22: i=i+1
        if i == 33 : i=i+1.3
        if i in [32,22] : i=i+0.3
        Label(frame,text=val1,font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=int(X+350+i*26),y=Y-206+MAXR*28)
        #=====================================================
    X,Y,H=100,256,72+(MAXR-9)*28
    a='S.\nNo'
    s='Enrollment No.'
    d='''#Name of Candidate
          #      Date
'''
    f='THEORY'																	
    g='Total\nTheory\nAttend.'
    h='PRACTICAL'
    i='Total\nPrac.'
    j='Total\nTh+P'

    Label(frame,text=a,font=('Times New Roman', 12, 'bold'),fg="black",bd=0).place(x=X-47,y=Y+20)
    Label(frame,text=s,font=('Times New Roman', 15, 'bold'),fg="black",bd=0).place(x=X-5,y=Y+20)
    Label(frame,text=d,font=('Times New Roman', 18, 'bold'),fg="black",bd=0).place(x=X+180,y=Y+10)
    Label(frame,text=f,font=('Times New Roman', 14, 'bold'),fg="black",bd=0).place(x=X+645,y=Y+2)
    Label(frame,text=g,font=('Times New Roman', 10, 'bold'),fg="black",bd=0).place(x=X+924,y=Y+10)
    Label(frame,text=h,font=('Times New Roman', 13, 'bold'),fg="black",bd=0).place(x=X+1029,y=Y+2)
    Label(frame,text=i,font=('Times New Roman', 12, 'bold'),fg="black",bd=0).place(x=X+1189,y=Y+10)
    Label(frame,text=j,font=('Times New Roman', 12, 'bold'),fg="black",bd=0).place(x=X+1239,y=Y+10)

    canvas=Canvas(frame,height=36,width=34)
    canvas.place(x=X+200,y=Y+33)
    for j in range(12):
        canvas.create_line(12+j,2,12+j,20)
    for j in range(16):
        canvas.create_line(j+2,20+j,34-j,20+j)
    canvas=Canvas(frame,height=34,width=36)
    canvas.place(x=X+370,y=Y+32)
    for j in range(12):
        canvas.create_line(2,12+j,22,12+j)
    for j in range(16):
        canvas.create_line(22+j,j+2,22+j,34-j)


    Frame(frame,width=1334,height=2,bg="black").place(x=X-52,y=Y)
    Frame(frame,width=1338,height=2,bg="black").place(x=X-54,y=Y+72)
    Frame(frame,width=2,height=H,bg="black").place(x=X-54,y=Y)
    Frame(frame,width=2,height=H-28,bg="black").place(x=X-20,y=Y)
    Frame(frame,width=2,height=H-28,bg="black").place(x=X+136,y=Y)
    Frame(frame,width=2,height=H,bg="black").place(x=X+424,y=Y)

    for i in range(MAXC):
        if i==18 or i==20 or i==28 or i==30 or i==32 :
            Frame(frame,width=2,height=H,bg="black").place(x=X+450+i*26,y=Y)
        if i==19 or i==31 or i==29:
            continue
        Frame(frame,width=2,height=H-23,bg="black").place(x=X+450+i*26,y=Y+25)

    for i in range(MAXR-9): 
        i+=1   #no of entry+1
        Frame(frame,width=1336,height=2,bg="black").place(x=X-54,y=Y+72+i*28)

    Frame(frame,width=494,height=2,bg="black").place(x=X+424,y=Y+25)
    Frame(frame,width=210,height=2,bg="black").place(x=X+970,y=Y+25)


def see_excel(root,WBname):
    top =Toplevel(root)
    top.geometry('1000x500')
    if '/' in WBname:
        folder=WBname.split("/")[-2]
        title=WBname.split("/")[-1]
    elif '\\' in WBname:
        folder=WBname.split("\\")[-2]
        title=WBname.split("\\")[-1]

    top.title(f" SHEET  VIEW        \t\t\t\t\t\t\t\t\t\t\t{title}")
    
    DownloadFrame=Frame(top)
    DownloadFrame.pack(pady=20,fill="x")

    B_Download = Button(DownloadFrame, 
                        text = "Download",
                        bg="green",fg="white",
                        font=("times new roman",15,'bold'),
                        command= lambda : Thread(target=Drive_uplode.download_files , args=( folder , title , True)).start())  
    B_Download.pack(side="right",padx=100,ipadx=50)

    # Create A Main Frame
    main_frame = Frame(top)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y,padx=15)

    xscrollbar = Scrollbar(top, orient=HORIZONTAL, command=my_canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=BOTH,pady=15)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set,xscrollcommand=xscrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    def yscroll(e):
        my_canvas.yview_scroll(int(-1*(e.delta/120)),'units')
    def xscroll(e):
        my_canvas.xview_scroll(int(-1*(e.delta/120)),'units')

    top.bind("<MouseWheel>",yscroll)
    top.bind("<Shift-MouseWheel>",xscroll)
    my_notebook = ttk.Notebook(second_frame)
    my_notebook.pack(padx=10)
    style=ttk.Style()

    #style
    if style.theme_use()!= "beautiful":
        style.theme_create( "beautiful", parent = style.theme_use(), settings ={
                "TNotebook": {
                    "configure": {"tabmargins": [10, 1, 5 , 0], "background" : "grey71"}},
                "TNotebook.Tab": {
                    "configure": {"padding": [1, 5] , "font":('consolas italic', 14), "borderwidth":[5]},
                    "map":      {"foreground": [("selected", "dark green"), ('!active', "black"), ('active', "black")],
                                "font": [("active", ('consolas italic', 14,'bold')) , ("selected", ('consolas italic', 14,'bold'))],
                                "expand": [("selected", [1, 1, 1, 0])]}
                                }})
        style.theme_use('beautiful')
        style.layout("Tab",
                            [('Notebook.tab', {'sticky': 'nswe', 'children':
                                [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                    [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                })],
                            })]
                        ) 
    try :
        wb=load_workbook(WBname)
    except :
        messagebox.showerror("Error","Error! Unable To Open\nPlease Try Again")
    compiler = ModelCompiler()
    new_model = compiler.read_and_parse_archive(WBname)
    evaluator = Evaluator(new_model)

    for i in wb.sheetnames :
        ws=wb[i]
        frame=Frame(my_notebook,height=ws.max_row*30,width=ws.max_column*43)
        frame.pack(fill=BOTH, expand=1)
        my_notebook.add(frame, text=i)
        Display(frame,ws,evaluator)
    top.mainloop()
'''