from tkinter import*
from tkinter.ttk import Combobox, Treeview

from PIL import Image,ImageTk
from tkinter import messagebox
import random

import mysql.connector
from time import strftime
from datetime import datetime

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        self.root.geometry("1295x550+230+220")


        #######Title########
        lbtitle=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        lbtitle.place(x=0,y=0,width=1295,height=50)


        
        ########LOGO##########
        img2=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\hotel logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        label1.place(x=5,y=2,width=100,height=40)

        ##Variables
        self.var_roomno=StringVar()
        x=random.randint(100,999)
        self.var_roomno.set(str(x))

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_noofdays=StringVar()
        self.var_meal=StringVar()
        self.var_bill=StringVar()


        #######labelframe#########
        lbl=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking Details",font=("arial",12,"bold"),padx=2,pady=6)
        lbl.place(x=5,y=50,width=425,height=490)


        ##Custcontact
        lbl_cust_contact=Label(lbl,text="Customer Contact no.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_contact)
        entry_contact.grid(row=0,column=1)

       

        ##Check in
        check_in_date=Label(lbl,text="Check-In Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        entry_checkin=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_checkin)
        entry_checkin.grid(row=1,column=1)

        ##Check out
        check_out_date=Label(lbl,text="Check-Out Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        entry_checkout=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_checkout)
        entry_checkout.grid(row=2,column=1)


        ##Room type
        lbl_roomtype=Label(lbl,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0,sticky=W)

        combo_roomtype=Combobox(lbl,font=("arial",12,"bold"),width=20,state="readonly",textvariable=self.var_roomtype)
        combo_roomtype["value"]=("Standard","Standard AC","Deluxe","Deluxe AC")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        ##Meal
        lbl_meal=Label(lbl,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=4,column=0,sticky=W)

        combo_meal=Combobox(lbl,font=("arial",12,"bold"),width=20,state="readonly",textvariable=self.var_meal)
        combo_meal["value"]=("Breakfast","Lunch","Dinner","All")
        combo_meal.current(0)
        combo_meal.grid(row=4,column=1)
        

        ##No. of days
        lbl_noofdays=Label(lbl,text="No. of days",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_noofdays.grid(row=5,column=0,sticky=W)

        entry_ref=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_noofdays)
        entry_ref.grid(row=5,column=1)

        ###Available room

        lbl_avr=Label(lbl,text="Room no.",font=("arial",12,"bold"),padx=2,pady=6,)
        lbl_avr.grid(row=6,column=0,sticky=W)

        entry_avr=Entry(lbl,font=("arial",13,"bold"),width=22,state="readonly",textvariable=self.var_roomno)
        entry_avr.grid(row=6,column=1)

        ##Bill
        lbl_total=Label(lbl,text="Total Bill",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_total.grid(row=7,column=0,sticky=W)

        entry_total=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_bill)
        entry_total.grid(row=7,column=1)

        ##Billlbtn###

        btnbill=Button(lbl,text="BILL",command=self.total,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btnbill.grid(row=8,column=0,padx=1)

        ########btns#########

        btn_frame=Frame(lbl,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        

        btndel=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btndel.grid(row=0,column=1,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btnreset.grid(row=0,column=2,padx=1)



        ####Rightsideimage
        img4=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\bed.jpg")
        img4=img4.resize((520,300),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label3=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        label3.place(x=600,y=55,width=520,height=200)


         ######TableFrame######
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details",font=("arial",12,"bold"),padx=2,pady=6)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        


        #Show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.room_table=Treeview(details_table,column=("Contact","Check-in","Check-out","Room type","available room","meal","No.ofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=X)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact No.")
        self.room_table.heading("Check-in",text="Check-In")
        self.room_table.heading("Check-out",text="Check-Out")
        self.room_table.heading("Room type",text="Room Type")
        self.room_table.heading("available room",text="Available room")
        
        self.room_table.heading("meal",text="Meal")
        
        self.room_table.heading("No.ofdays",text="No. of days")
        
        

        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.column("Contact",width=100)       
        self.room_table.column("Check-in",width=100) 
        self.room_table.column("Check-out",width=100) 
        self.room_table.column("Room type",width=100)
        self.room_table.column("available room",width=100)   
         
        self.room_table.column("meal",width=100) 
        
        self.room_table.column("No.ofdays",width=100) 
        
         

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
       
        self.fetch_data()

    #Add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()
                    
                                   
                                                                
                                                                                            
                                                                                            
                                                                                            
                                                                        

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    
    
    
    #Fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomno.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
        
        
    
    
    
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root) 
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        
        x=random.randint(100,999)
        self.var_roomno.set(str(x))
        self.var_bill.set("")
    
    
     
    
    
    
    
    
    
    
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Standard"):
            q1=float(200)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Standard AC"):
            q1=float(200)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Deluxe"):
            q1=float(200)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)                   
    
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Deluxe AC"):
            q1=float(200)
            q2=float(2500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
    
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Standard"):
            q1=float(600)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Standard AC"):
            q1=float(600)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe"):
            q1=float(600)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe AC"):
            q1=float(600)
            q2=float(2500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Standard"):
            q1=float(700)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Standard AC"):
            q1=float(700)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe"):
            q1=float(700)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe AC"):
            q1=float(700)
            q2=float(2500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
            
            
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Standard"):
            q1=float(1500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Standard AC"):
            q1=float(1500)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Deluxe"):
            q1=float(1500)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)
        
        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Deluxe AC"):
            q1=float(1500)
            q2=float(2500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            TT="Rs."+str("%.2f"%((q5)))
            self.var_bill.set(TT)        
        
        
        
        
        
        
        
        
    
                









if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop() 
        