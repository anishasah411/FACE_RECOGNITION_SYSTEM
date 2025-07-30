from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
import os
import tkinter

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\mri_1.jpeg")
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=150)

        # Second Image
        img1 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\rec.jpeg")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\mri.jpeg")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\bg_image.jpeg")
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=800)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Time Label
        self.time_lbl = Label(bg_img, font=("times new roman", 14, "bold"), bg="white", fg="blue")
        self.time_lbl.place(x=1360, y=10, width=150, height=30)
        self.update_time()  # Start the time update

        # Student Button
        img4 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\stu.jpeg")
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=200, height=150)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=220, width=200, height=40)

        # Detect Face Button
        img5 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\dec.jpeg")
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=350, y=100, width=200, height=150)
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=350, y=220, width=200, height=40)

        # Attendance Button
        img6 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\ATT.jpeg")
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b3.place(x=650, y=100, width=200, height=150)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=650, y=220, width=200, height=40)

        # Help Desk Button
        img7 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\CHAT.jpeg")
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b4.place(x=950, y=100, width=200, height=150)
        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=950, y=220, width=200, height=40)

        # Train Data Button
        img8 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\TRAIN.jpeg")
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=100, y=350, width=200, height=150)
        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=100, y=460, width=200, height=40)

        # Photos Button
        img9 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\PHO.jpeg")
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=350, y=350, width=200, height=150)
        b6_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=350, y=460, width=200, height=40)

        # Developer Button
        img10 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\PER.jpeg")
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b7.place(x=650, y=350, width=200, height=150)
        b7_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=650, y=460, width=200, height=40)

        # Exit Button
        img11 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\EXIT.jpeg")
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.exit)
        b8.place(x=950, y=350, width=200, height=150)
        b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=950, y=460, width=200, height=40)

    # Time update function
    def update_time(self):
        time_string = strftime('%H:%M:%S %p')
        self.time_lbl.config(text=time_string)
        self.time_lbl.after(1000, self.update_time)
        
    def open_img(self):
        os.startfile("data")  
        
    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root) 
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    # Functions Button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)  # Corrected reference to Help class

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()

