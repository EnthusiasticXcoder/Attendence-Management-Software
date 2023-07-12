from threading import Thread
from tkinter import filedialog
from typing import Tuple
import customtkinter as ctk
from PIL import Image

from services.cloud.DriveService import DriveService
from services.workbook.WorkbookService import WorkBookService , get_column_letter


class ShowExcelView(ctk.CTkToplevel):
    def __init__(self, wbPath: str, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        self.geometry('1000x500')
        self.title(f'SHEET VIEW {wbPath}')
        
        img = ctk.CTkImage(light_image=Image.open("assets/icons/download.png"),
                           dark_image=Image.open("assets/icons/download.png"),size=(35,35))
        
        B_Download = ctk.CTkButton(master=self, 
                                text = "Download",
                                fg_color="green",text_color="white",image=img,
                                font=("times new roman",15,'bold'),
                                command= lambda: self._Ondownload(wbPath))  
        B_Download.pack(anchor = 'ne',padx=100,ipadx=50,pady=20)

        Tab = ctk.CTkTabview(master=self)
        Tab.pack(fill='both', expand=1)

        service = WorkBookService.getInstance()
        worksheets = service.get_worksheet_from_path(wbPath)
        evaluator = service.get_evaluator(wbPath)
        
        for worksheet in worksheets :
            newtab = Tab.add(worksheet.title)    
            Frame= ctk.CTkScrollableFrame(master=newtab,fg_color='transparent')
            Frame.pack(expand =1, fill='both')
            thread = Thread(target=self.BuildTab, kwargs={'master' : Frame, 'worksheet' : worksheet, 'evaluator' : evaluator})
            thread.start()

    def BuildTab(self, master: any, worksheet, evaluator):
        ''' Function to build excel worksheet '''
        MAXC=worksheet.max_column
        MAXR=0
        while True:
            if worksheet['A'+str(MAXR+10)].value == None  :
                break  
            MAXR+=1
        MAXR +=11

        frame1=ctk.CTkFrame(master=master,width=1200)
        frame1.grid(row=0,column=0,sticky='nsew')

        indexc=[i for i in range(MAXC)]
        indexr=[i for i in range(7)]

        frame1.rowconfigure(indexr,weight=0)
        frame1.columnconfigure(indexc,weight=1)

        frame2=ctk.CTkFrame(master=master)
        frame2.grid(row=1,column=0,sticky='nsew')

        for row in range(1,MAXR+1):
            if row in [7,8,9] : continue
            span=1
            values=[]
            merge=[]
            col=[]
                
            for column,i in enumerate(worksheet[str(row)]):
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
                            if i.value is None:
                                values.append(i.value)
                            else:
                                alfacol=get_column_letter(column+1)
                                try:val = evaluator.evaluate(f'{worksheet.title}!{alfacol}{row}')
                                except: val =0
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
                    self.Tabularcell(master=rowframe,text=value,column=column,maxr=maxr).grid(row=0,column=column,columnspan=span,sticky=s)
            elif row<7:
                for value,span,column in zip(values,merge,col):
                    if value==None : 
                        continue
                    else:
                        self.Cell(master=frame1,text=value).grid(row=row-1,column=column,columnspan=span,sticky=s)    

        
        headframe=ctk.CTkFrame(master=frame2,corner_radius=0)
        headframe.grid(row=0,column=0,sticky='nsew')

        headframe.rowconfigure(0,weight=1)
        headframe.rowconfigure(1,weight=2)

        for column,i in enumerate(worksheet['8']) :
            val= " " if i.value==None else i.value
            if val in ['THEORY',"PRACTICAL"] : 
                headwidth=0
                headcell=self.Headcell(master=headframe,column=column,text=val,height=25,head=True)
                headcell.grid(row=0,column=column,columnspan=19,sticky='nw')
            row,span=0,1
            if column>2 and column not in [22,31,32] : row+=1
            else : span=2 

            if 2<column<22 or 22<column<31 :
                try:
                    char=get_column_letter(column+1)
                    val=worksheet[f'{char}9'].value
                    if val==None : 
                        continue
                    arr=val.split("\n")
                    val=f'{arr[0]}\n{arr[1]}\n{arr[2]}'
                    headwidth+=1
                    headcell.configure(width=int(headwidth*30.42))
                except :
                    continue
            cell =self.Headcell(master=headframe,column=column,text=val)
            cell.grid(row=row,column=column,rowspan=span,sticky='nw')

    def Headcell(self,master,column,text,height=80,head=False):
        '''  '''
        border_color=None
        text_font=('Times New Roman', 11, 'bold')
        width=200
        height=80
        text_font= ctk.CTkFont('Times New Roman',11,'bold')
        border_color=("#565B5E",'#565B5E')
        if column<2 : text_font.configure(size = 13)
        if column==2 : text_font.configure(size = 17)
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
        
        textbox =ctk.CTkTextbox(master=master,
                        border_color=border_color,
                        border_width=0, 
                        corner_radius=2, 
                        #font=text_font, 
                        width=width, height=height,
                        activate_scrollbars=False,border_spacing=0,)

        textbox.insert('0.0',f"{text}")
        textbox.configure(state="disabled")
        
        return textbox

    def Cell(self, master,text) :
        '''   '''
        return ctk.CTkLabel(master=master,
                            corner_radius=0,
                            width=int(len(str(text))*9.1), 
                            height=40, 
                            text=text, 
                            font=("Roboto Medium", -16,'bold'))

    def Tabularcell(self,master,text,column,maxr):
        '''   '''
        width= 200 if column==2 else 30
        width= 50 if column in [22,31,32] else width
        width= 150 if column==1 else width 
        width= 34 if column==0 else width
        width=384 if maxr==True and column==0 else width

        textvariable=ctk.StringVar(value=text)
        justify= 'left' if width==200 else 'center'

        return ctk.CTkEntry(master=master,
                            width=width,
                            textvariable=textvariable,
                            justify=justify,
                            font=('Times New Roman', 14, 'bold'),
                            corner_radius=0, 
                            border_width=2, state=ctk.DISABLED,)
    
    def _Ondownload(self, wbname):
        path=filedialog.asksaveasfilename(filetypes=[("Excel Workbook","*.xlsx")],defaultextension='.xlsx')

        if path :
            service = DriveService.getInstance()
            thread = Thread(target=service.Download_File, kwargs={'filename' : wbname, 'path' : path })
            thread.start()
