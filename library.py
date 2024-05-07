from tkinter import *
import tkinter.messagebox
import Library_Database
import Teacher_Database
from tkinter import ttk
import datetime as dt
import dates
from tabulate import tabulate


root=Tk()
root.title("Library Management System")
root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\login_1Bi_icon.ico')    

def Login_win(root):
    def Student_issue_return():
        ROOT_1=Toplevel()
        ROOT_1.geometry('1330x560+100+100')
        ROOT_1.title("Library Management System")
        ROOT_1.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\study_7HK_icon.ico')
        
        
         
        DateOfIssue=StringVar()
        NameOfBook=StringVar()
        AccessionNo=StringVar()
        NumberOfBooks=IntVar()
        IssuedTo=StringVar()
        Class=StringVar()
        DateOfReturn=StringVar()
        instock=IntVar()
        cardid=StringVar()
        nameofstudent=StringVar()
        
            
        #************************Functions

        def iExit():
            iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to quit")
            if iExit>0:
                ROOT_1.destroy()
                root.destroy()
                return

        def ClearData():

            
            ROOT_1.cbo_5.current(0)
            ROOT_1.cbo_2.current(0)
            ROOT_1.txtIssuedTo.delete(0,END)
            ROOT_1.txtClass.delete(0,END)
            ROOT_1.txtinstock.delete(0,END)
            ROOT_1.cbo_3.current(0)
            ROOT_1.cbo_4.current(0)
            NumberOfBooks.set(1)
            

        def stock():
            if len(Library_Database.stock_books(ROOT_1.cbo_2.get()))!=0:
                for row in Library_Database.stock_books(ROOT_1.cbo_2.get()):
                    result=row[2]
                    instock.set(str(result))
                    result=row[0]
                    NameOfBook.set(result)
                    booklist.delete(0,END)
                    if row[2]<=0:
                        ans="stock empty  !"
                        booklist.insert(END,ans)
                        instock.set(0)
                    else:
                        ans="Book Available "
                        booklist.insert(END,ans)
                        
                        ROOT_1.btn=Button(DataFrameLEFT,text="search",height=1,width=5,bd=1,command=issuedata)
                        ROOT_1.btn.grid(row=4,column=3)
                        ROOT_1.btn=Button(DataFrameLEFT,text="search",height=1,width=5,bd=1,command=issuename)
                        ROOT_1.btn.grid(row=5,column=3)
        
                        
            else:
                booklist.delete(0,END)
                ans="No Book With This Accession No."
                booklist.insert(END,ans)

        def stock2():
            if len(Library_Database.stock_books2(ROOT_1.cbo_5.get()))!=0:
                for row in Library_Database.stock_books2(ROOT_1.cbo_5.get()):
                    result=row[2]
                    instock.set(str(result))
                    result=row[1]
                    AccessionNo.set(result)
                    booklist.delete(0,END)
                    if row[2]<=0:
                        ans="stock empty  !"
                        booklist.insert(END,ans)
                        instock.set(0)
                    else:
                        ans="Book Available "
                        booklist.insert(END,ans)
                        
                        ROOT_1.btn=Button(DataFrameLEFT,text="search",height=1,width=5,bd=1,command=issuedata)
                        ROOT_1.btn.grid(row=4,column=3)
                        ROOT_1.btn=Button(DataFrameLEFT,text="search",height=1,width=5,bd=1,command=issuename)
                        ROOT_1.btn.grid(row=5,column=3)
        
                        
            else:
                booklist.delete(0,END)
                ans="No Accession No. With This Book"
                booklist.insert(END,ans)

                
        def stockcopy():
            if len(Library_Database.stock_books(AccessionNo.get()))!=0:
                for row in Library_Database.stock_books(AccessionNo.get()):
                    result=row[2]
                    instock.set(str(result))
                    result=row[0]
                    NameOfBook.set(result)
                    booklist.delete(0,END)
                    if row[2]<0:
                        ans="stock empty  !"
                        booklist.insert(END,ans)
                        instock.set(0)
                    else:
                        ans="Book Issued ThankYou"
                        booklist.insert(END,ans)
                    
            
        def AddData():
            if len(AccessionNo.get())!=0 and type(NumberOfBooks.get())==int and len(nameofstudent.get())!=0 and len(Class.get())!=0  and instock.get()!=0 and cardid.get()!=0 and NameOfBook.get()!=0 and NumberOfBooks.get()<=instock.get():
                Library_Database.addData(AccessionNo.get(),NameOfBook.get(),NumberOfBooks.get(),nameofstudent.get(),Class.get(),DateOfReturn.get(),DateOfIssue.get(),ROOT_1.cbo_3.get())

                booklist.delete(0,END)
                booklist.insert(END,(AccessionNo.get(),NameOfBook.get(),nameofstudent.get(),NumberOfBooks.get(),cardid.get(),Class.get(),DateOfIssue.get(),DateOfReturn.get()))
                Library_Database.stockupdate(instock.get(),NumberOfBooks.get(),AccessionNo.get(),NameOfBook.get())
                stockcopy()
                ClearData()
            elif instock.get()==0:
                booklist.delete(0,END)
                ans="Stock Empty   Cant issue"
                booklist.insert(END,ans)
            elif NumberOfBooks.get()>instock.get():
                booklist.delete(0,END)
                ans="Cant issue"
                booklist.insert(END,ans)
            else:
                booklist.delete(0,END)
                ans="Specify every field please"
                booklist.insert(END,ans)
        
                
        def DisplayData():
            booklist.delete(0,END)
            for row in Library_Database.Display():
                if row[0]=="no data":
                    booklist.insert(END,row[0])
                else:
                    booklist.insert(END,row)
                

        def SelectedBook(event):
            global sb
            try:
                SearchBk=booklist.curselection()[0]
                sb=booklist.get(SearchBk)

                ROOT_1.txtDateOfIssue.delete(0,END)
                ROOT_1.txtDateOfIssue.insert(END,sb[6])
                NameOfBook.set(sb[1])
                AccessionNo.set(sb[0])
                ROOT_1.txtNumberOfBooks.delete(0,END)
                ROOT_1.txtNumberOfBooks.insert(END,sb[2])
                ROOT_1.txtClass.delete(0,END)
                ROOT_1.txtClass.insert(END,sb[4])
                ROOT_1.txtDateOfReturn.delete(0,END)
                ROOT_1.txtDateOfReturn.insert(END,sb[5])
                cardid.set(sb[7])
                nameofstudent.set(sb[3])
            except:
                pass
            

        def DeleteData():
            if len(cardid.get())!=0:
                global sb
                Library_Database.DelData(sb[7],sb[0])
                ClearData()
                DisplayData()

        def search():
            root_1=Toplevel()
            root_1.geometry('256x30+850+360')
            root_1.title("Search")
            root_1.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\search_xUJ_icon.ico')

            search=StringVar()
            mainframe=Frame(root_1)
            mainframe.grid()
            root_1.cbo_1=ttk.Combobox(mainframe,state='readonly',textvariable=search,font=('ariel',12),width=17)
            root_1.cbo_1['value']=(' ','Name','accsession id','card id','Date of issue','Date of return')
            root_1.cbo_1.current(0)
            root_1.cbo_1.grid(row=1,column=0)


            def proceed():
                value=root_1.cbo_1.get()

                def one():
                    value=name.get()
                    print()
                    print()
                    headers=["Accession No.","Name of book","No. of Books","Issued To","Class","Issue date","Return Date","Card id"]
                    L=[]
                    for row in Library_Database.one1(value):
                        L.append(row)
                    mydata=L
                    print(tabulate(mydata,headers=headers,tablefmt="grid"))
                        
                        
                def  two():
                    value=accsessionid.get()
                    print()
                    print()
                    headers=["Accession No.","Name of book","No. of Books","Issued To","Class","Issue date","Return Date","Card id"]
                    L=[]
                    for row in Library_Database.one2(value):
                        L.append(row)
                    mydata=L
                    print(tabulate(mydata,headers=headers,tablefmt="grid"))
                        
                def three():
                    value=cardid.get()
                    print()
                    print()
                    headers=["Accession No.","Name of book","No. of Books","Issued To","Class","Issue date","Return Date","Card id"]
                    L=[]
                    for row in Library_Database.one3(value):
                        L.append(row)
                    mydata=L
                    print(tabulate(mydata,headers=headers,tablefmt="grid"))
                        

                def four():
                    value=Dateofissue.get()
                    print()
                    print()
                    headers=["Accession No.","Name of book","No. of Books","Issued To","Class","Issue date","Return Date","Card id"]
                    L=[]
                    for row in Library_Database.one4(value):
                        L.append(row)
                    mydata=L
                    print(tabulate(mydata,headers=headers,tablefmt="grid"))
                        
                def five():
                    value=Dateofreturn.get()
                    print()
                    print()
                    headers=["Accession No.","Name of book","No. of Books","Issued To","Class","Issue date","Return Date","Card id"]
                    L=[]
                    for row in Library_Database.one5(value):
                        L.append(row)
                    mydata=L
                    print(tabulate(mydata,headers=headers,tablefmt="grid"))
                        
                    
                if value=="Name":
                    Root=Toplevel()
                    Root.geometry('256x30+850+360')
                    Root.title("Name")
                    Root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\search_xUJ_icon.ico')
                    mainframe=Frame(Root)
                    mainframe.grid()
                    name=StringVar()
                    Root.txtname=Entry(mainframe,font=('ariel',12),textvariable=name,width=20)
                    Root.txtname.grid(row=1,column=0)
                    Root.btn=Button(mainframe,text="proceed",height=1,width=10,bd=1,command=one)
                    Root.btn.grid(row=1,column=3)

                    Root.mainloop()
                if value=="accsession id":
                    Root=Toplevel()
                    Root.geometry('256x30+850+360')
                    Root.title("accsession id")
                    Root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\search_xUJ_icon.ico')
                    mainframe=Frame(Root)
                    mainframe.grid()
                    accsessionid=StringVar()
                    Root.txtname=Entry(mainframe,font=('ariel',12),textvariable=accsessionid,width=20)
                    Root.txtname.grid(row=1,column=0)
                    Root.btn=Button(mainframe,text="proceed",height=1,width=10,bd=1,command=two)
                    Root.btn.grid(row=1,column=3)

                    Root.mainloop()
                if value=="card id":
                    Root=Toplevel()
                    Root.geometry('256x30+850+360')
                    Root.title("card id")
                    Root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\search_xUJ_icon.ico')
                    mainframe=Frame(Root)
                    mainframe.grid()
                    cardid=StringVar()
                    Root.txtname=Entry(mainframe,font=('ariel',12),textvariable=cardid,width=20)
                    Root.txtname.grid(row=1,column=0)
                    Root.btn=Button(mainframe,text="proceed",height=1,width=10,bd=1,command=three)
                    Root.btn.grid(row=1,column=3)

                    Root.mainloop()
                if value=="Date of issue":
                    Root=Toplevel()
                    Root.geometry('256x30+850+360')
                    Root.title("Date of issue")
                    Root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\search_xUJ_icon.ico')
                    mainframe=Frame(Root)
                    mainframe.grid()
                    Dateofissue=StringVar()
                    Root.txtname=Entry(mainframe,font=('ariel',12),textvariable=Dateofissue,width=20)
                    Root.txtname.grid(row=1,column=0)
                    Root.btn=Button(mainframe,text="proceed",height=1,width=10,bd=1,command=four)
                    Root.btn.grid(row=1,column=3)

                    Root.mainloop()
                if value=="Date of return":
                    Root=Toplevel()
                    Root.geometry('256x30+850+360')
                    Root.title("Date of return")
                    Root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\search_xUJ_icon.ico')
                    mainframe=Frame(Root)
                    mainframe.grid()
                    Dateofreturn=StringVar()
                    Root.txtname=Entry(mainframe,font=('ariel',12),textvariable=Dateofreturn,width=20)
                    Root.txtname.grid(row=1,column=0)
                    Root.btn=Button(mainframe,text="proceed",height=1,width=10,bd=1,command=five)
                    Root.btn.grid(row=1,column=3)

                    Root.mainloop()
                
            root_1.btn=Button(mainframe,text="proceed",height=1,width=10,bd=1,command=proceed)
            root_1.btn.grid(row=1,column=3)

                
                
        
            root_1.mainloop()
            
            

                

                
                
        
        #************************Frames
        mainFrame=Frame(ROOT_1,bg="wheat1")
        mainFrame.grid()
        TitFrame=Frame(mainFrame,bd=13,width=1350,padx=10,pady=8,bg="wheat1",relief=RIDGE)
        TitFrame.pack(side=TOP)
        ROOT_1.lblTit=Label(TitFrame,padx=80,pady=20,font=('Verdana',25),text=" Cambridge International School:   Library Management System")
        ROOT_1.lblTit.grid(sticky=W)
    
        ButtonFrame=Frame(mainFrame,bd=2,width=1350,height=100,padx=20,pady=20,bg="wheat1",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
    
        FrameDetail=Frame(mainFrame,bd=10,width=1350,height=0,bg="lemon chiffon",padx=70,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)
    
        DataFrame=Frame(mainFrame,bd=1,width=1500,height=400,bg="lemon chiffon",padx=100,pady=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
    
        DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=800,height=300,padx=20,relief=RIDGE,font=('Verdana',12),text="Member Details",bg="peach puff")
        DataFrameLEFT.pack(side=LEFT)
    
        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=20,relief=RIDGE,font=('Verdana',12),text="Book Details",bg="peach puff")
        DataFrameRIGHT.pack(side=RIGHT)
    
        #************************Label and Entry
    
        
        ROOT_1.lblDateOfIssue=Label(DataFrameLEFT,font=('ariel',12),text="Date Of Issue:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblDateOfIssue.grid(row=7,column=0,sticky=W)
        now=dt.datetime.now()
        Y=str(now.year)
        M=str(now.month)
        D=str(now.day)
        DateOfIssue.set(D+"/"+M+"/"+Y)
        ROOT_1.txtDateOfIssue=Entry(DataFrameLEFT,font=('ariel',12),text="%s"%DateOfIssue,textvariable=DateOfIssue,width=25)
        ROOT_1.txtDateOfIssue.grid(row=7,column=1)
        
    
        ROOT_1.lblAccessionNo=Label(DataFrameLEFT,font=('ariel',12),text="Accession No:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblAccessionNo.grid(row=1,column=0,sticky=W)
        ROOT_1.cbo_2=ttk.Combobox(DataFrameLEFT,state='readonly',textvariable=AccessionNo,font=('ariel',12),width=23)
        asslist=[" "]
        for row in Library_Database.getassc():
            if row[0]=="no data":
                asslist.append(row)
            else:
                asslist.append(row[0])
        asslist.sort()
        
        ROOT_1.cbo_2['value']=asslist
        ROOT_1.cbo_2.current(0)
        ROOT_1.cbo_2.grid(row=1,column=1)

        ROOT_1.lblNumberOfBooks=Label(DataFrameLEFT,font=('ariel',12),text="Number Of Books",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblNumberOfBooks.grid(row=9,column=0,sticky=W)
        ROOT_1.txtNumberOfBooks=Entry(DataFrameLEFT,font=('ariel',12),textvariable=NumberOfBooks,width=25)
        ROOT_1.txtNumberOfBooks.grid(row=9,column=1)
        NumberOfBooks.set(1)
        ROOT_1.lblIssuedTo=Label(DataFrameLEFT,font=('ariel',12),text="Issued To",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblIssuedTo.grid(row=5,column=0,sticky=W)
        ROOT_1.txtIssuedTo=Entry(DataFrameLEFT,font=('ariel',12),textvariable=IssuedTo,width=25)
        ROOT_1.txtIssuedTo.grid(row=5,column=1)

        ROOT_1.lblClass=Label(DataFrameLEFT,font=('ariel',12),text="Class:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblClass.grid(row=6,column=0,sticky=W)
        ROOT_1.txtClass=Entry(DataFrameLEFT,font=('ariel',12),textvariable=Class,width=25)
        ROOT_1.txtClass.grid(row=6,column=1)

        ROOT_1.lblinstock=Label(DataFrameLEFT,font=('ariel',12),text="In Stock:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblinstock.grid(row=3,column=0,sticky=W)
        ROOT_1.txtinstock=Entry(DataFrameLEFT,font=('ariel',12),textvariable=instock,width=25)
        ROOT_1.txtinstock.grid(row=3,column=1)
        
        ROOT_1.lblcardid=Label(DataFrameLEFT,font=('ariel',12),text="Card Id:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblcardid.grid(row=4,column=0,sticky=W)
        ROOT_1.cbo_3=ttk.Combobox(DataFrameLEFT,state='readonly',textvariable=cardid,font=('ariel',12),width=23)
        bsslist=[" "]
        for row in Library_Database.getcrdid():
            if row[0]=="no data":
                bsslist.append(row[0])
            else:
                bsslist.append(row[0])
        
        bsslist.sort()
        ROOT_1.cbo_3['value']=bsslist
        ROOT_1.cbo_3.current(0)
        ROOT_1.cbo_3.grid(row=4,column=1)

        ROOT_1.cbo_4=ttk.Combobox(DataFrameLEFT,state='readonly',textvariable=nameofstudent,font=('ariel',12),width=23)
        csslist=[" "]
        for row in Library_Database.getcrdid2():
            if row[0]=="no data":
                csslist.append(row[0])
            else:
                csslist.append(row[0])
        csslist.sort()
        ROOT_1.cbo_4['value']=csslist
        ROOT_1.cbo_4.current(0)
        ROOT_1.cbo_4.grid(row=5,column=1)

        ROOT_1.cbo_5=ttk.Combobox(DataFrameLEFT,state='readonly',textvariable=NameOfBook,font=('ariel',12),width=23)
        dsslist=[" "]
        for row in Library_Database.getassc2():
            if row[0]=="no data":
                dsslist.append(row)
            else:
                dsslist.append(row[0])
        dsslist.sort()
        ROOT_1.cbo_5['value']=dsslist
        ROOT_1.cbo_5.current(0)
        ROOT_1.cbo_5.grid(row=2,column=1)
        
        ROOT_1.lblDateOfReturn=Label(DataFrameLEFT,font=('ariel',12),text="Date Of Return:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblDateOfReturn.grid(row=8,column=0,sticky=W)

        
        def issuedata():
            value=ROOT_1.cbo_3.get()
            for row in Library_Database.getdata(value):
                if row[0]=="no data":
                    print("no data available")
                else:
                    ROOT_1.cbo_4.set(row[0])
        def issuename():
            value=ROOT_1.cbo_4.get()
            for row in Library_Database.getdata2(value):
                if row[0]=="no data":
                    print("no data available")
                else:
                    ROOT_1.cbo_3.set(row[0])
                
                
        
        DateOfIssue.set(D+"/"+M+"/"+Y)
        if int(now.day)>23:
            dates.dates_h(DateOfReturn)
        elif int(now.month)==2 and (int(now.day)<=23 and int(now.day)>21):
            dates.dates_feb(DateOfReturn)  
        
        else:
            now=dt.datetime.now()
            Y=str(now.year)
            M=str(now.month)
            D=str(int(now.day)+7)
            DateOfReturn.set(D+"/"+M+"/"+Y)
              
        ROOT_1.txtDateOfReturn=Entry(DataFrameLEFT,font=('ariel',12),text="%s"%DateOfReturn,textvariable=DateOfReturn,width=25)
        ROOT_1.txtDateOfReturn.grid(row=8,column=1)

        ROOT_1.lblNameOfBook=Label(DataFrameLEFT,font=('ariel',12),text="Name Of Book:",padx=2,pady=2,bg="peach puff")
        ROOT_1.lblNameOfBook.grid(row=2,column=0,sticky=W)
        
        #************************ListBox and Scrollbar
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        booklist=Listbox(DataFrameRIGHT,width=45,height=12,font=('ariel',12),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        #************************Button Widget

        ROOT_1.btnAddData=Button(ButtonFrame,text="Issue",font=('ariel',14),height=2,width=16,bd=4,command=AddData)
        ROOT_1.btnAddData.grid(row=0,column=0)
            
        ROOT_1.btnDisplayData=Button(ButtonFrame,text="Student Data",font=('ariel',14),height=2,width=13,bd=4,command=DisplayData)
        ROOT_1.btnDisplayData.grid(row=0,column=1)
            
        ROOT_1.btnClearData=Button(ButtonFrame,text="New entry",font=('ariel',14),height=2,width=13,bd=4,command=ClearData)
        ROOT_1.btnClearData.grid(row=0,column=2)
            
        ROOT_1.btnDeleteData=Button(ButtonFrame,text="Delete student Data",font=('ariel',14),height=2,width=20,bd=4,command=DeleteData)
        ROOT_1.btnDeleteData.grid(row=0,column=3)

        def hah():
            ROOT_1.destroy()
            Student_issue_return()
            
            
        ROOT_1.btnUpdateData=Button(ButtonFrame,text="Restart ",font=('ariel',14),height=2,width=13,bd=4,command=hah)
        ROOT_1.btnUpdateData.grid(row=0,column=4)
            
        ROOT_1.btnSearchData=Button(ButtonFrame,text="Search ",font=('ariel',14),height=2,width=13,bd=4,command=search)
        ROOT_1.btnSearchData.grid(row=0,column=5)
            
        ROOT_1.btnExit=Button(ButtonFrame,text="Exit",font=('ariel',14),height=2,width=16,bd=4,command=iExit)
        ROOT_1.btnExit.grid(row=0,column=6)

        ROOT_1.btn=Button(DataFrameLEFT,text="search",height=1,width=5,bd=1,command=stock)
        ROOT_1.btn.grid(row=1,column=3)

        ROOT_1.btn=Button(DataFrameLEFT,text="search",height=1,width=5,bd=1,command=stock2)
        ROOT_1.btn.grid(row=2,column=3)
        
        
            
        
        
        

    #=================================================================================================================================================
    def return1():
        RooT=Toplevel()
        RooT.geometry('350x250+300+150')
        RooT.title("Return Book")
        RooT.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\return_PYp_icon.ico')
        
        mainFrame=Frame(RooT)
        mainFrame.grid()
        
        def fun():
            value=textbox1.get()
            print()
            print()
            headers=["Accession No.","Name of book","No. of Books","Issued To","Class","Issue date","Return Date","Card id"]
            L=[]
            for row in Library_Database.one3(value):
                L.append(row)
            mydata=L
            print(tabulate(mydata,headers=headers,tablefmt="grid"))
            if len(L)!=0:
                lable3=Label(RooT,text="Accession Id:",font=('ariel',13,'bold'))
                lable3.place(x=10,y=90)
                textbox3=Entry(RooT,bd=3)
                textbox3.place(x=150,y=90)

                lable4=Label(RooT,text="No. of Books",font=('ariel',13,'bold'))
                lable4.place(x=10,y=120)
                textbox4=Entry(RooT,bd=3)
                textbox4.place(x=150,y=120)

                result=StringVar()
                def ans1():
                    a=textbox3.get()
                    b=textbox4.get()
                    c=Library_Database.currentstock(a)
                    C=c[0][0]
                    d=Library_Database.getassc3(a)
                    Library_Database.stockupdate2(int(C),int(b),a)
                    ans=textbox1.get()
                    ANS=textbox3.get()
                    def del1():
                        Library_Database.DelData2(ans,ANS)
                    del1()
                    RooT.destroy()
                    
                    
                    

                button3=Button(RooT,text="Return",font=('ariel',12),width=35,command=ans1)
                button3.place(x=10,y=160)
            
    
       
        lable1=Label(RooT,text="Card id",font=('ariel',13,'bold'))
        lable1.place(x=10,y=30)
        textbox1=Entry(RooT,bd=3)
        textbox1.place(x=150,y=30)

        
        button1=Button(RooT,text="Search",font=('ariel',9),width=6,command=fun)
        button1.place(x=280,y=30)
        
        
        
        RooT.mainloop()
        
        
        
        
        



    def sec1():
        return1()
            
    

            
        
    def page2(root):
        
        ROOT=Toplevel()
        ROOT.geometry('500x70+900+490')
        ROOT.title("  Table Selection..  ")
        ROOT.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\table_grid_tXm_icon.ico')
        mainFrame=Frame(ROOT)
        mainFrame.grid()
        table=StringVar()
        ROOT.lbl_1=Label(mainFrame,font=('Verdana',12),text="Tables:",padx=2,pady=2)
        ROOT.lbl_1.grid(row=0,column=0,sticky=W)
        ROOT.cbo_1=ttk.Combobox(mainFrame,state='readonly',textvariable=table,font=('ariel',12),width=44)
        ROOT.cbo_1['value']=(' ','Issue book','Return book')
        ROOT.cbo_1.current(0)
        ROOT.cbo_1.grid(row=0,column=1)
        def val():
            value=ROOT.cbo_1.get()
            if value=="Issue book":
                Student_issue_return()
            elif value=="Return book":
                sec1()
            else:
                print("no table selected")
        
        button_1=Button(ROOT,text="Proceed",font=('Verdana',13),width=43,command=val)
        button_1.place(x=6,y=30)

                

    def ft():            
        username="admin"
        password="admin"
        result=StringVar()
        a=textbox_1.get()
        b=textbox_2.get()
        if a==username:
            if b==password:
                result.set("Login Successful")
                button_2=Button(root,text="Login",font=('Verdana',12),width=11,command=page2(root))
                button_2.place(x=200,y=170)
            else:
                result.set("Login Failed")       
        else:
            result.set("Login Failed")
        Entry(root,bd=5,text="%s"%result).place(x=200,y=220)
        
    root.geometry('500x350+900+100')
    mainFrame=Frame(root)
    mainFrame.grid()
    LoginFrame=Frame(mainFrame,width=500,height=300,padx=20,bd=20,bg="wheat1",relief=RIDGE)
    LoginFrame.pack(side=BOTTOM)
    lable_1=Label(root,text="Login Window",font=('Cooper Black',20))
    lable_1.place(x=150,y=300)
    lable_2=Label(root,text="UserName",bg="wheat1",font=('Verdana',13))
    lable_2.place(x=70,y=80)
    lable_3=Label(root,text="Password",bg="wheat1",font=('Verdana',13))
    lable_3.place(x=70,y=120)
    button_1=Button(root,text="Login",bg="lemon chiffon",font=('Verdana',11),width=9,command=ft)
    button_1.place(x=200,y=170)
    textbox_1=Entry(root,bd=5)
    textbox_1.place(x=200,y=80)
    textbox_2=Entry(root,bd=5,show='*')
    textbox_2.place(x=200,y=120)
    textbox_3=Entry(root,bd=5)
    textbox_3.place(x=200,y=220)        
    
                                
Login_win(root)

root.mainloop()

