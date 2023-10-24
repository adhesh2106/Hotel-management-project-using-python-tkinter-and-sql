

from tkinter import*
from tkinter.ttk import Combobox, Treeview

from PIL import Image,ImageTk
from tkinter import messagebox
import random

import mysql.connector







class CustWin:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #####Variables#####
        self.var_ref=StringVar()
        x=random.randint(100,999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        self.var_idno=StringVar()
        self.var_nat=StringVar()

        #######Title########
        lbtitle=Label(self.root,text="ENTER CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        lbtitle.place(x=0,y=0,width=1295,height=50)


        
     #############LOGO##########
        img2=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\hotel logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        label1.place(x=5,y=2,width=100,height=40)



        #######labelframe#########
        lbl=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2,pady=6)
        lbl.place(x=5,y=50,width=425,height=490)


        ######Labels and entry#######

        ##Custref
        lbl_cust_ref=Label(lbl,text="Customer Reference No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=Entry(lbl,font=("arial",13,"bold"),textvariable=self.var_ref,width=22,state="readonly")
        entry_ref.grid(row=0,column=1)

        ####Customer name######
        lbl_cust_name=Label(lbl,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        txtname=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_cust_name)
        txtname.grid(row=1,column=1)

        #Gender combobox
        lbl_cust_gen=Label(lbl,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_gen.grid(row=2,column=0,sticky=W)
       

        combo_gen=Combobox(lbl,font=("arial",12,"bold"),width=20,state="readonly",textvariable=self.var_gender)
        combo_gen["value"]=("Male","Female","Other")
        combo_gen.current(0)
        combo_gen.grid(row=2,column=1)

        #Mobile no.
        lbl_cust_mob=Label(lbl,text="Mobile No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mob.grid(row=3,column=0,sticky=W)

        entry_mob=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_mobile)
        entry_mob.grid(row=3,column=1)

        #Email id
        lbl_cust_email=Label(lbl,text="Email ID",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=4,column=0,sticky=W)

        entry_email=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_email)
        entry_email.grid(row=4,column=1)

        #Nationality
        lbl_cust_nat=Label(lbl,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_nat.grid(row=5,column=0,sticky=W)

       

        combo_nat=Combobox(lbl,font=("arial",12,"bold"),width=20,state="readonly",textvariable=self.var_nat)
        combo_nat["value"]=("Indian","American","British")
        combo_nat.current(0)
        combo_nat.grid(row=5,column=1)


        #Address
        lbl_cust_add=Label(lbl,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_add.grid(row=6,column=0,sticky=W)

        entry_add=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_address)
        entry_add.grid(row=6,column=1)
        
        #ID type
        lbl_cust_idtype=Label(lbl,text="ID Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_idtype.grid(row=7,column=0,sticky=W)

        
        combo_id=Combobox(lbl,font=("arial",12,"bold"),width=20,state="readonly",textvariable=self.var_idproof)
        combo_id["value"]=("Aadhar Card","Driving License","Passport")
        combo_id.current(0)
        combo_id.grid(row=7,column=1)


        #ID number
        lbl_cust_idnum=Label(lbl,text="ID Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_idnum.grid(row=8,column=0,sticky=W)

        entry_idnum=Entry(lbl,font=("arial",13,"bold"),width=22,textvariable=self.var_idno)
        entry_idnum.grid(row=8,column=1)

        ########btns#########

        btn_frame=Frame(lbl,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        

        btndel=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btndel.grid(row=0,column=1,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="blue",width=10)
        btnreset.grid(row=0,column=2,padx=1)

        ######TableFrame######
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details",font=("arial",12,"bold"),padx=2,pady=6)
        Table_Frame.place(x=435,y=50,width=860,height=490)

       

        #Show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_table=Treeview(details_table,column=("Ref","Name","Gender","Mobile no.","Email ID","Nationality","Address","ID proof","ID no."),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=X)

        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("Ref",text="Reference No.")
        self.Cust_details_table.heading("Name",text="Name")
        self.Cust_details_table.heading("Gender",text="Gender")
        self.Cust_details_table.heading("Mobile no.",text="Mobile No.")
        self.Cust_details_table.heading("Email ID",text="Email ID")
        self.Cust_details_table.heading("Nationality",text="Nationality")
        self.Cust_details_table.heading("Address",text="Address")
        self.Cust_details_table.heading("ID proof",text="ID proof")
        self.Cust_details_table.heading("ID no.",text="ID No.")

        self.Cust_details_table["show"]="headings"
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        
        self.Cust_details_table.column("Ref",width=100)       
        self.Cust_details_table.column("Name",width=100) 
        self.Cust_details_table.column("Gender",width=100) 
        self.Cust_details_table.column("Mobile no.",width=100) 
        self.Cust_details_table.column("Email ID",width=100) 
        self.Cust_details_table.column("Nationality",width=100) 
        self.Cust_details_table.column("Address",width=100) 
        self.Cust_details_table.column("ID proof",width=100) 
        self.Cust_details_table.column("ID no.",width=100) 

        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_cust_name.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_ref.get(),
                                                                        self.var_cust_name.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_mobile.get(),
                                                                        self.var_email.get(),
                                                                        self.var_nat.get(),
                                                                        self.var_address.get(),
                                                                        self.var_idproof.get(),
                                                                        self.var_idno.get()
                                                                        

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nat.set(row[5]),
        self.var_address.set(row[6]),
        self.var_idproof.set(row[7]),
        self.var_idno.set(row[8])


    

                                                                        
               

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root) 
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_cust_name.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_idno.set("")
        
        x=random.randint(100,999)
        self.var_ref.set(str(x))

       




if __name__=="__main__":
    root=Tk()
    obj=CustWin(root)
    root.mainloop()        
