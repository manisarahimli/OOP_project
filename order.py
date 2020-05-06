from tkinter import *


class opening(Frame):
    def __init__(self, cder=None):
        Frame.__init__(self, cder)               
        self.cder = cder
        self.init_opening()
    def init_opening(self):
        self.cder.title("Object Oriented Programming project")
        self.grid()
        Label(self,text=" Full name ").grid(row=0)
        Label(self,text="Address: ").grid(row=1)
        Label(self,text="E-mail: ").grid(row=2)
        self.Name = Entry(self, width=30)
        self.Name.grid(row=0, column=1, columnspan=2, sticky="EW")
        self.Address = Entry(self, state='disabled', width=45)
        self.Address.grid(row=1, column=1, columnspan=3, sticky="EW")
        self.e_mail = Entry(self, state='disabled', width=45)
        self.e_mail.grid(row=2, column=1, columnspan=3, sticky="EW")
        self.delivery = BooleanVar()
        self.Check = Checkbutton(self, text="Delivery", variable=self.delivery, command=self.Check)
        self.Check.grid(row=0, column=3)
        Label(self, text = "Pizzas").grid(row=3, column=0, columnspan=2, pady=(20,5))
        Label(self, text = "Quantity").grid(row=3, column=2, pady=(20,5))
        Label(self, text = "Prices").grid(row=3, column=3, pady=(20,5))
        
        j = 0
        global rows
        for i in Pizzas:
            self.i = IntVar()
            Label(self, text = i).grid(row=rows, columnspan=2)
            self.i = Spinbox(self, from_=0, to=5, width=5)
            self.i.grid(row=rows, column=2)
            Label(self, text = "$" + str(Pizza_Prices[j])).grid(row=rows, column=3)
            Pizza_Spinboxes.append(self.i)
            rows += 1
            j += 1
        Button(self, text='Submit', command=self.Pizza_Submit).grid(row=rows, column=0, pady=10, padx=5, sticky=N)
        self.Confirm_Button = Button(self, text='Confirm', command=self.Confirm)
        self.Confirm_Button.grid(row=rows+1, column=0, pady=10, padx=5, sticky=N)
        self.Confirm_Button.config(state=DISABLED)

        self.Scroll = Scrollbar(self)
        self.Scroll.grid(row=rows, column=4, rowspan=5, sticky="NS")
        self.Output = Text(self, width=35, height=18, yscrollcommand=self.Scroll.set)
        self.Output.grid(row=rows, column=1, columnspan=3, rowspan=3, pady=5)
        self.Output.insert('1.0', '')
        self.Output.config(state=DISABLED)
        self.Scroll.config(command=self.Output.yview)
        
    def Pizza_Submit(self):
        global Pizza_Spinboxes
        global rows
        global Final_Order
        
        Ordered = {}
        Total_Pizza_num = 0
        cost = 0
        j = 0
        error = False
        for i in Pizza_Spinboxes:
            Total_Pizza_num += int(i.get())

        self.Confirm_Button.config(state=DISABLED)        
        self.Output.config(state=NORMAL)
        self.Output.delete("1.0", END)

        if Total_Pizza_num == 0:
            self.Output.insert('1.0', " Choose the pizzas")
            error = True
        elif Total_Pizza_num > 5:
            self.Output.insert('1.0', " Less than 5 pizzas")
            error = True
        elif not self.Name.get():
            self.Output.insert('1.0', " Enter their name")
            error = True
        elif self.delivery.get() == True:
            if not self.Address.get():
                self.Output.insert('1.0', " Enter their address")
                error = True
            elif not self.e_mail.get():
                self.Output.insert('1.0', "Enter their e-mail")
                error = True
                
        if error == True:
            self.Output.configure(background="red", foreground="white")
            self.Output.config(state=DISABLED)
        else:
            if self.delivery.get() == True:
                Final_Order = " Name: {} \n Address: {} \n E-mail address {} \n -----Delivery----- \n \n".format(self.Name.get(), self.Address.get(), self.e_mail.get())
                cost += 3
            else:
                Final_Order = " Name: {} \n \n".format(self.Name.get())
            Final_Order = Final_Order + "Num   Cost    Pizza\n"
            for i in Pizza_Spinboxes:
                if int(i.get()) != 0:
                    Final_Order = Final_Order + " {}    {}    {} \n".format(i.get(), Pizza_Prices[j]*int(i.get()), Pizzas[j])
                    cost += Pizza_Prices[j] * int(i.get())
                j += 1


            self.Confirm_Button.config(state=NORMAL)

            Final_Order = Final_Order + "\n----------------------------------\n Total Cost         {}".format(cost)
            self.Output.insert('1.0', Final_Order)
            self.Output.configure(background="white", foreground="black")
            self.Output.config(state=DISABLED)
                        
    def Confirm(self):
        global Final_Order
        global Pizza_Spinboxes  


        Final_Order = Final_Order + "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
        
        print(Final_Order)
        self.Name.delete(0, END)
        self.Address.delete(0, END)
        self.e_mail.delete(0, END)
        self.delivery.set(False)
        self.Output.config(state=DISABLED)
        self.Output.delete("1.0", END)
        for i in Pizza_Spinboxes:       
            i.delete(0, 2)
            i.insert(0,[0])
        
    def Check(self):    
        if self.delivery.get() == True:
            self.Address.configure(state='normal')
            self.e_mail.configure(state='normal')
        else:
            self.Address.configure(state='disabled')
            self.e_mail.configure(state='disabled')

Pizzas=["Pepperoni   ", "Hawaiian", "Vegetarian", "Butter Chicken", "Margherita", "Seafood", "Fish", "Cheese", "Meatlovers", "Apricot Chicken", "Beef & Onion", "Supreme", "Plain"]
Pizza_Prices=[10.5, 10.5, 10.5, 20.0, 10.5, 10.5, 10.5, 10.5, 15.5, 15.5, 15.5, 15.5, 15.5]
Pizza_Spinboxes = []

Final_Order = ""
rows = 4


root = Tk()
root.geometry("375x690")
app = opening(root)
root.mainloop()
