from tkinter import*
from PIL import Image,ImageTk
from customer import CustWin
from restmenu import RestMenu
from room import RoomBooking
from roominfo import RoomInfo








class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


    ##############Top Image##########
        img1=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\hotel1.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=1550,height=140)


     #############LOGO##########
        img2=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\hotel logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        label1.place(x=0,y=0,width=230,height=140)    

    #######Title########
        lbtitle=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        lbtitle.place(x=0,y=140,width=1550,height=50)


        #####Main frame#####
        mframe=Frame(self.root,bd=4,relief=RIDGE)
        mframe.place(x=0,y=190,width=1550,height=620)


        #######menu######
        menu1=Label(mframe,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        menu1.place(x=0,y=0,width=230)


        #####Buttonframe######
        btframe=Frame(mframe,bd=4,relief=RIDGE)
        btframe.place(x=0,y=35,width=228,height=190)


        #####Buttons####
        custbt=Button(btframe,text="CUSTOMER",command=self.custdetails,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,relief=RIDGE,cursor="hand2")
        custbt.grid(row=0,column=0,pady=1)

        roombt=Button(btframe,text="ROOM BOOKING",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,relief=RIDGE,cursor="hand2")
        roombt.grid(row=1,column=0,pady=1)

        detailsbt=Button(btframe,text="ROOM AMENITIES",command=self.rinfo,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,relief=RIDGE,cursor="hand2")
        detailsbt.grid(row=2,column=0,pady=1)

        restbt=Button(btframe,text="RESTAURANT MENU",command=self.rest,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,relief=RIDGE,cursor="hand2")
        restbt.grid(row=3,column=0,pady=1)

        logoutbt=Button(btframe,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="blue",bd=0,relief=RIDGE,cursor="hand2")
        logoutbt.grid(row=4,column=0,pady=1)
        

        ####main frame img#######
        img3=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\hotel 2.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label2=Label(mframe,image=self.photoimg3,bd=4,relief=RIDGE)
        label2.place(x=225,y=0,width=1310,height=590)

        #######down images#####

        img4=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\bed.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label3=Label(mframe,image=self.photoimg4,bd=4,relief=RIDGE)
        label3.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\restaurant.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        label4=Label(mframe,image=self.photoimg5,bd=4,relief=RIDGE)
        label4.place(x=0,y=420,width=230,height=190)


    def custdetails(self):
        self.new_win=Toplevel(self.root)
        self.app=CustWin(self.new_win)

    def roombooking(self):
        self.new_win=Toplevel(self.root)
        self.app=RoomBooking(self.new_win)

    def rinfo(self):
        self.new_win=Toplevel(self.root)
        self.app=RoomInfo(self.new_win)
        
    def rest(self):
        self.new_win=Toplevel(self.root)
        self.app=RestMenu(self.new_win)  
      
    def logout(self):
        self.root.destroy()





if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
                
