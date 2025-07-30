from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 25, "bold"), bg="white", fg="BLUE")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        
        img_top = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\LOP.jpeg")
        img_top = img_top.resize((1530, 590), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=1530, height=590)
        
        #FRAME
        main_frame=Frame(f_lbl2,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=365,height=500)
        
        
        img_top1 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\img.1.jpeg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl2 = Label(main_frame, image=self.photoimg_top1)
        f_lbl2.place(x=200, y=0, width=150, height=200)
        
        # developer info
        dep_lebel=Label(main_frame,text="hello my name is Anisha sah",font=("times new roman", 13, "bold"),bg="white")
        dep_lebel.place(x=0,y=5)
        
        dep_lebel=Label(main_frame,text="I am Full stack developer",font=("times new roman", 13, "bold"),bg="white")
        dep_lebel.place(x=0,y=40)
        
        img2 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\img1.jpeg")
        img2 = img2.resize((500, 250), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(main_frame, image=self.photoimg2)
        f_lbl2.place(x=0, y=245, width=500, height=250)
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop() 