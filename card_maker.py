from tkinter import *
import tkinter.messagebox
import Library_Database
from tkinter import ttk

root=Tk()
root.title("Card maker")
root.geometry("380x230+900+200")
canvas=Canvas(width=380,height=230,bg='blue')
canvas.place(x=0,y=0)

photo=PhotoImage(file="C:\\Users\\abhishek\\Desktop\\schl\\lib files\\images.png")
canvas.create_image(0,0,image=photo,anchor=NW)

root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\books_stack_of_three_4It_icon.ico')

studentname=StringVar()
admissionno=StringVar()
cardid=StringVar()



def addcard():
    if len(admissionno.get())!=0 and len(cardid.get())!=0 and len(studentname.get())!=0:
        B=studentname.get()          
        A=admissionno.get()
        I=cardid.get()
        Library_Database.add_card(B,A,I)
        result=StringVar()
        result.set(" Done ")
        root.txtBook=Entry(root,font=('ariel',12),text='%s'%result,width=35)
        root.txtBook.place(x=6,y=150)
    else:
        result=StringVar()
        result.set("Check your details correctly")
        root.txtBook=Entry(root,font=('ariel',12),text='%s'%result,width=35)
        root.txtBook.place(x=6,y=150)
        

    
def iExit():
    iExit=tkinter.messagebox.askyesno("Card maker","Do you want to quit ?")
    if iExit>0:
        root.destroy()
        return

def Deletecard():
    ROOT=Toplevel()
    admissionnod=StringVar()
    ROOT.title("Delete card")
    ROOT.geometry("380x190+900+470")
    ROOT.lbladmissionnod=Label(ROOT,font=('ariel',12),text="Enter Admission No.",padx=2,pady=2)
    ROOT.lbladmissionnod.grid(row=1,column=0,sticky=W)
    ROOT.txtadmissionnod=Entry(ROOT,font=('ariel',12),textvariable=admissionnod,width=20)
    ROOT.txtadmissionnod.grid(row=1,column=1)
    def del5():
        if len(admissionnod.get())!=0:
            A=admissionnod.get()
            Library_Database.remove_card(A)
            result=StringVar()
            result.set("Card deleted")
            ROOT.txtBook=Entry(ROOT,font=('ariel',12),text='%s'%result,width=38)
            ROOT.txtBook.place(x=0,y=150)
            ROOT.destroy()
        else:
            result=StringVar()
            result.set("Check your details correctly")
            ROOT.txtBook=Entry(ROOT,font=('ariel',12),text='%s'%result,width=38)
            ROOT.txtBook.place(x=0,y=150)


    button=Button(ROOT,text="Delete",font=('Verdana',13),width=32,command=del5)
    button.place(x=10,y=50)
    ROOT.txtBook=Entry(font=('ariel',12),text="Book Added",width=35)
    ROOT.txtBook.place(x=0,y=150)
        
    ROOT.mainloop()

def addnew():
    admissionno.set("")
    studentname.set("")
    cardid.set("")
    root.txtBook=Entry(root,font=('ariel',12),text="",width=35)
    root.txtBook.place(x=6,y=150)

def card_generator():
    a=studentname.get()
    b=a[0:3]
    c=admissionno.get()
    cardid.set(b+c)
    
def show():
    print()
    print()
    print("Admission number","\t","\t","Name")
    print()
    for row in Library_Database.show_stu():
        if row[0]=="n":
            print()
            print('NO DATA ')
        else:
            print(row[1],"\t","\t","\t","\t",row[0])
                
        
    
root.lblstudentname=Label(font=('ariel',12,'bold'),text="Student Name ",padx=2,pady=2,bg='lavender')
root.lblstudentname.grid(row=0,column=0,sticky=W)
root.txtstudentname=Entry(font=('ariel',12),textvariable=studentname,width=23)
root.txtstudentname.grid(row=0,column=1)


root.lbladmissionno=Label(font=('ariel',12,'bold'),text="Admission No.",padx=2,pady=2,bg='lavender')
root.lbladmissionno.grid(row=1,column=0,sticky=W)
root.txtadmissionno=Entry(font=('ariel',12),textvariable=admissionno,width=23)
root.txtadmissionno.grid(row=1,column=1)

root.lblcardid=Label(font=('ariel',12,'bold'),text="Card Id              ",padx=2,pady=2,bg='lavender')
root.lblcardid.grid(row=2,column=0,sticky=W)
root.txtcardid=Entry(font=('ariel',12),textvariable=cardid,width=23)
root.txtcardid.grid(row=2,column=1)

button_1=Button(root,text="issue card",font=('Verdana',13),command=addcard)
button_1.place(x=10,y=100)

button_2=Button(root,text="delete card",font=('Verdana',13),command=Deletecard)
button_2.place(x=135,y=100)

root.txtBook=Entry(font=('ariel',12),width=40)
root.txtBook.place(x=6,y=150)

button_3=Button(root,text="Exit",font=('Verdana',13),width=16,command=iExit)
button_3.place(x=190,y=190)

button_4=Button(root,text="create",command=card_generator)
button_4.place(x=335,y=29)

button_4=Button(root,text="new",font=('Verdana',13),width=8,command=addnew)
button_4.place(x=275,y=100)

button_4=Button(root,text="All data",font=('Verdana',13),width=15,command=show)
button_4.place(x=6,y=190)



root.mainloop()
