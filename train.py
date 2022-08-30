#from dbm import _Database
from tkinter import*
from tkinter import ttk
#from turtle import right
from PIL import Image,ImageTk
from tkinter import  messagebox
import mysql.connector
import cv2
import os
import numpy as np

# os.environ['TCL_LIBRARY']='C:\\Users\\ashiu\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tcl8.6'
# os.environ['TK_LIBRARY']='C:\\Users\\ashiu\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tK8.6'



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("Train data")

        title_lbl=Label(self.root,text="Train Data Set",font=("times new rooman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\first.png")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

# button 
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new rooman",30,"bold"),bg="gray",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)



        img_bottom=Image.open("C:\\Users\\ashiu\\3D Objects\\pythonpro\\atten\\image\\first.png")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)#antialias conver high to low
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')#  gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # TRAIN THE CLASSIFIER AND SAVE

        #clf=cv2.face.LBPHFaceRecognizer_create()
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training dataset completed!!!")







       









if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
