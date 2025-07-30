from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 25, "bold"), bg="white", fg="BLUE")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        
        img_top = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\DESK.jpeg")
        img_top = img_top.resize((1275, 590), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=1275, height=590)
        
        dep_lebel=Label(f_lbl2,text="EMAIL:anishasah411@gmail.com",font=("times new roman", 20, "bold"),bg="white")
        dep_lebel.place(x=600,y=250)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)  # Use the correct class name 'Help'
    root.mainloop()
