from tkinter import *
import tkinter.messagebox
import Library_Database
from tkinter import ttk

root=Tk()
root.title("Add Books")
root.geometry("380x230+900+200")
canvas=Canvas(width=380,height=230,bg='blue')
canvas.place(x=0,y=0)

photo=PhotoImage(file="C:\\Users\\abhishek\\Desktop\\schl\\lib files\\images.png")
canvas.create_image(0,0,image=photo,anchor=NW)


BookName=StringVar()
inStock=IntVar()
AccessionNo=StringVar()



def addbooks():
    if len(AccessionNo.get())!=0 and type(inStock.get())==int and len(BookName.get())!=0:
        B=BookName.get()          
        A=AccessionNo.get()
        I=inStock.get()
        Library_Database.add_book(B,A,I)
        result=StringVar()
        result.set("Book Added")
        root.txtBook=Entry(root,font=('ariel',12),text='%s'%result,width=35)
        root.txtBook.place(x=0,y=150)
    else:
        result=StringVar()
        result.set("Check your details correctly")
        root.txtBook=Entry(root,font=('ariel',12),text='%s'%result,width=35)
        root.txtBook.place(x=0,y=150)
        

    


def Deletebook():
    ROOT=Toplevel()
    AccessionNod=StringVar()
    ROOT.title("Remove Books")
    ROOT.geometry("380x190+900+470")
    ROOT.lblAccessionNod=Label(ROOT,font=('ariel',12),text="Enter Accession No.",padx=2,pady=2)
    ROOT.lblAccessionNod.grid(row=1,column=0,sticky=W)
    ROOT.txtAccessionNod=Entry(ROOT,font=('ariel',12),textvariable=AccessionNod,width=24)
    ROOT.txtAccessionNod.grid(row=1,column=1)
    def del5():
        if len(AccessionNod.get())!=0:
            A=AccessionNod.get()
            Library_Database.remove_book(A)
            
            result=StringVar()
            result.set("Book deleted")
                
                    
            ROOT.txtBook=Entry(ROOT,font=('ariel',12),text='%s'%result,width=38)
            ROOT.txtBook.place(x=0,y=150)
            ROOT.destroy()
        else:
            result=StringVar()
            result.set("Check your details correctly")
            ROOT.txtBook=Entry(ROOT,font=('ariel',12),text='%s'%result,width=38)
            ROOT.txtBook.place(x=0,y=150)
            


    button=Button(ROOT,text="Delete Book",font=('Verdana',13),command=del5,width=33)
    button.place(x=5,y=50)
    ROOT.txtBook=Entry(font=('ariel',12),text="Book Added",width=35)
    ROOT.txtBook.place(x=0,y=150)
        
    ROOT.mainloop()

def addmore():
    AccessionNo.set("")
    BookName.set("")
    inStock.set(0)
    root.txtBook=Entry(root,font=('ariel',12),text="",width=35)
    root.txtBook.place(x=0,y=150)
    
def show():
    print()
    print()
    print("Book name\tAccession number")
    print()
    for row in Library_Database.show_books():
        if row[0]=="n":
            print()
            print('NO DATA ')
        else:
            print(row[0],"\t\t",row[1])
                
    
    
root.lblBookName=Label(font=('ariel',12,'bold'),text="Book Name",padx=2,pady=2,bg='lavender')
root.lblBookName.grid(row=0,column=0,sticky=W)
root.txtBookName=Entry(font=('ariel',12),textvariable=BookName,width=29)
root.txtBookName.grid(row=0,column=1)


root.lblAccessionNo=Label(font=('ariel',12,'bold'),text="Access. No.",padx=2,pady=2,bg='lavender')
root.lblAccessionNo.grid(row=1,column=0,sticky=W)
root.txtAccessionNo=Entry(font=('ariel',12),textvariable=AccessionNo,width=29)
root.txtAccessionNo.grid(row=1,column=1)

root.lblinStock=Label(font=('ariel',12,'bold'),text="In Stock       ",padx=2,pady=2,bg='lavender')
root.lblinStock.grid(row=2,column=0,sticky=W)
root.txtinStock=Entry(font=('ariel',12),textvariable=inStock,width=29)
root.txtinStock.grid(row=2,column=1)

button_1=Button(root,text="Add Book",font=('Verdana',13),command=addbooks)
button_1.place(x=10,y=100)

button_2=Button(root,text="Remove Book",font=('Verdana',13),command=Deletebook)
button_2.place(x=125,y=100)

root.txtBook=Entry(font=('ariel',12),width=40)
root.txtBook.place(x=4,y=150)
def iExit():
    iExit=tkinter.messagebox.askyesno("Card maker","Do you want to quit ?")
    if iExit>0:
        root.destroy()
        return

button_3=Button(root,text="Exit",font=('Verdana',13),width=15,command=iExit)
button_3.place(x=200,y=190)

button_4=Button(root,text="Add More",font=('Verdana',13),width=8,command=addmore)
button_4.place(x=275,y=100)

button_4=Button(root,text="all data",font=('Verdana',13),width=15,command=show)
button_4.place(x=6,y=190)




root.mainloop()
