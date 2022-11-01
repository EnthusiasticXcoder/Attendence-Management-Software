from tkinter import *
from tkinter import ttk
from threading import Thread
from tkinter import messagebox

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from xlcalculator import ModelCompiler
from xlcalculator import Evaluator

from utilits import Drive_uplode


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
    d='''Name of Candidate
                Date'''
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
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y,padx=15)

    xscrollbar = ttk.Scrollbar(top, orient=HORIZONTAL, command=my_canvas.xview)
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
