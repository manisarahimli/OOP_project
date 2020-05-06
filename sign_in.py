import sqlite3
from tkinter import *


def sign_in():

        origin=Tk()
        origin.geometry("1600x800+0+0")
        origin.title("Pizza Management system")
        origin.configure(bg="pink")


        Tops=Frame(origin, width=1600, height=50, bg="pink")
        Tops.pack(side=TOP)

        f1=Frame(origin, width=800, height=700, bg="white")
        f1.pack(side=TOP)


        lblinfo = Label(Tops, font=('calibri', 50 ), text="pizza management system" , fg="gold",bg="white", bd=17,anchor='w')
        lblinfo.grid(row=0,column=0)



        lab=Label(f1,text="\n\n\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)

        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)
        L1 = Label(f1, text="Name : ",font=('arial',15),fg="gold",bg="white")
        L1.grid(row=1,column=0)
        lab=Label(f1,text="\t",bg="white")
        lab.grid(row=1,column=1)
        E1 = Entry(f1, bd =5,width=40,font=('calibri',10),relief="groove")
        E1.grid(row=1,column=2)


        lab=Label(f1,text="\n\n\n\n\n\n",bg="white")
        lab.grid(row=2,column=0)
        L2 = Label(f1, text="Password : ",font=('calibri',15),fg="gold",bg="white")
        L2.grid(row=2,column=0)
        lab=Label(f1,text="\t",bg="white")
        lab.grid(row=2,column=1)
        E2 = Entry(f1, bd =5,width=40,font=('arial',10),relief="groove",show="*")
        E2.grid(row=2,column=2)
        def st():
                conn =sqlite3.connect('pds.db')
                c=conn.cursor()
                deta =c.execute("SELECT NAME , PASSWORD FROM USER_DETAIL")
                flag=0
                for row in deta:
                        if (row[0] ==E1.get() and row[1] ==E2.get()):
                                flag =1
                                break
             
        B1=Button(f1,text="Login",width=20,bd=5,font=('arial',10),fg="white",bg="green",relief="raised",command=st)
        B1.grid(row=3,column=2)

        origin.mainloop()

if __name__=="__main__":
        sign_in()
