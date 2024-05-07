from tkinter import *
import tkinter.messagebox
import Library_Database
from tkinter import ttk
import time
import sys

root=Tk()
root.title("Home")
root.iconbitmap(r'C:\\Users\\abhishek\\Desktop\\schl\\lib files\\icons\\study_7HK_icon.ico')
root.geometry("900x300+150+200")
canvas=Canvas(width=1100,height=500)
canvas.place(x=0,y=0)

photo=PhotoImage(file="C:\\Users\\abhishek\\Desktop\\schl\\lib files\\homeBG.png")
canvas.create_image(0,0,image=photo,anchor=NW)

lable=Label(root,text=" Library management system",font=('Cooper Black',20))
lable.place(x=200,y=24)


homevalues=StringVar()

root.cbo=ttk.Combobox(state='readonly',textvariable=homevalues,font=('ariel',12),width=23)
root.cbo['value']=[" select options "," ","Stock Management","Card Maker","issue/return","About us"]
root.cbo.current(0)
root.cbo.place(x=400,y=150)

def ans():
    value=root.cbo.get()
    if value=="Stock Management":
        root.destroy()
        import add_books_into_stock
    if value=="Card Maker":
        root.destroy()
        import card_maker
    if value=="issue/return":
        root.destroy()
        import library
    if value=="About us":
        root.destroy()
        import about
def ans1():
    import help_me
    
    

photo1=PhotoImage(file="C:\\Users\\abhishek\\Desktop\\schl\\lib files\\ok-mark.png")
button=Button(root,image=photo1,bd=0,command=ans)
button.place(x=650,y=145)

photo2=PhotoImage(file="C:\\Users\\abhishek\\Desktop\\schl\\lib files\\question.png")
button1=Button(root,image=photo2,bd=0,command=ans1)
button1.place(x=850,y=20)

def get_time():
    ts=time.strftime("%I:%M:%S:%p")
    clock.config(text=ts)
    clock.after(200,get_time)


clock=Label(root,font=('ariel',17))
clock.place(x=700,y=250)
get_time()

root.mainloop()
