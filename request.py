from tkinter import *
import sqlite3

def customer():

        origin=Tk()
        origin.geometry("1600x800+0+0")
        origin.title("Pizza Delivery system")
        origin.configure(bg="pink")


        Tops=Frame(origin, width=800, height=60, bg="pink")
        Tops.pack(side=TOP)

        f1=Frame(origin, width=800, height=700, bg="white")
        f1.pack(side=TOP)


        lblinfo = Label(Tops, font=('calibri', 50 ), text="Pizza Management System" , fg="gold",bg="white", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)



        lab=Label(f1,text="\n\n\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)


        l2=Label(f1,text="\n\n\n\n",bg="white")
        l2.grid(row=0,column=0)
        L1 = Label(f1, text="Name : ",font=('arial',15,'bold'),fg="gold",bg="white")
        L1.grid(row=1,column=0)
        l3=Label(f1,text="\t\t\t",bg="white")
        l3.grid(row=1,column=1)
        E1 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E1.grid(row=1,column=2)


        var = IntVar()
        l4=Label(f1,text="\n",bg="white")
        l4.grid(row=3,column=0)
        L2 = Label(f1, text="Address : ",font=('arial',15,'bold'),fg="gold",bg="white")
        L2.grid(row=4,column=0)
        l5=Label(f1,text="\t\t\t",bg="white")
        l5.grid(row=4,column=1)
        E2 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E2.grid(row=4,column=2)


        l5=Label(f1,text="\n",bg="white")
        l5.grid(row=5,column=0)
        L3 = Label(f1, text="Phone No : ",font=('arial',15,'bold'),fg="gold",bg="white")
        L3.grid(row=6,column=0)
        l6=Label(f1,text="\t\t\t",bg="white")
        l6.grid(row=6,column=1)
        E3 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove")
        E3.grid(row=6,column=2)


        l7=Label(f1,text="\n",bg="white")
        l7.grid(row=9,column=0)
        L5 = Label(f1, text="Password : ",font=('arial',15,'bold'),fg="gold",bg="white")
        L5.grid(row=10,column=0)
        l8=Label(f1,text="\t\t\t",bg="white")
        l8.grid(row=10,column=1)
        E5 = Entry(f1, bd =5,width=50,font=('arial',10,'bold'),relief="groove",show="*")
        E5.grid(row=10,column=2)

        
        lab3=Label(f1,text="\n",bg="white")
        lab3.grid(row=9,column=0)
        def getvalue():
                        name=E1.get()
                        address=E2.get()
                        phone=E3.get()
                        passw=E5.get()
                        conn = sqlite3.connect('pds.db')
                        c=conn.cursor()
                        c.execute("insert into user_detail(name,gender,address,phone,email,password) values('"+name+"',"+str(var.get())+",'"+address+"',"+phone+",'"+email+"','"+passw+"');")
                        
                        tkMessageBox.showinfo("Registered","Registration Successful")
                                
                        conn.commit()
                        conn.close()
                        
        B=Button(f1,text="Submit",width=20,font=('arial',10,'bold'),fg="white",bg="pink",command=getvalue)
        B.grid(row=14,column=2)

        origin.mainloop()
if __name__=="__main__":
        customer()
