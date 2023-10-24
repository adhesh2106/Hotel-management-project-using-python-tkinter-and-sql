from tkinter import*
from PIL import Image,ImageTk

class RestMenu:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        self.root.geometry("1295x550+230+220")
        
         #######Title########
        lbtitle=Label(self.root,text="RESTAURANT MENU",font=("times new roman",18,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        lbtitle.place(x=0,y=0,width=1295,height=50)


        
        ########LOGO##########
        img2=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\hotel logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        label1.place(x=5,y=2,width=100,height=40)
        
        ###Restaurant menu
        ####main frame img#######
        img6=Image.open(r"C:\Users\Dr.N.T.Murali Mohan\Desktop\Hotel project pics\menu.png")
        img6=img6.resize((1310,590),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        label2=Label(self.root,image=self.photoimg6,bd=4,relief=RIDGE)
        label2.place(x=0,y=50,width=1310,height=590)
        
if __name__=="__main__":
    root=Tk()
    obj=RestMenu(root)
    root.mainloop()