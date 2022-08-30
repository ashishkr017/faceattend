from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from studetail import Student
import os
from train  import Train
from face_recog import Face_Recognition

# os.environ['TCL_LIBRARY']='C:\\Users\\ashiu\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tcl8.6'
# os.environ['TK_LIBRARY']='C:\\Users\\ashiu\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tK8.6'


class Face_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("face Recogniton system")

        #function btn======

        #first 
        img=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\first.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

# second
       # img1=Image.open(r"C:\Users\ashiu\3D Objects\pythonpro\atten\image\first.png")
        img1=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\first.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

#third
        #img2=Image.open(r"C:\Users\ashiu\3D Objects\pythonpro\atten\image\first.png")
        img2=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\first.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        # background image
        img3=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\second.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new rooman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # stu button
        img4=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\smain.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.studentDetail,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.studentDetail,cursor="hand2",font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


         # detect face button
        img5=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\crowd.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


         # attendance button
        img6=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\atted.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


         # help button
        img7=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


         # train face button
        img8=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="training data ",cursor="hand2",command=self.train_data,font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        # Photos face button
        img9=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\phot.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="photos ",cursor="hand2",command=self.open_img,font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        # exit face button
        img10=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\exit.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="exit ",cursor="hand2",font=("times new rooman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")


        #function btn======

    def studentDetail(self):

        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):

        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):

        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


















if __name__=="__main__":
    root=Tk()
    obj=Face_System(root)
    root.mainloop()
