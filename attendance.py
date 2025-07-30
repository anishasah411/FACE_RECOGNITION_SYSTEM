from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import  filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        
        #==============================Variables==================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        # First Image
        img = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\ce.jpeg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\dan.jpeg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=200)
        
        # Background Image
        img3 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\bg_image.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=450)

        # Title Label
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=385)
        
        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=650, height=365)
        
        img_left = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\mri.jpeg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl2 = Label(left_frame, image=self.photoimg_left)
        f_lbl2.place(x=5, y=0, width=640, height=80)
        
        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=90, width=640, height=200)
        
        # Labeled entry
        
        # Attendance ID
        attId_label = Label(left_inside_frame, text="ATTENDANCE ID:", font=("times new roman", 10, "bold"), bg="white")
        attId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        attdentID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id, font=("times new roman", 10, "bold"))
        attdentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Roll
        roll_label = Label(left_inside_frame, text="ROLL:", font=("times new roman", 10, "bold"), bg="white")
        roll_label.grid(row=0, column=2, pady=8)
        
        roll_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll, font=("times new roman", 10, "bold"))
        roll_entry.grid(row=0, column=3, pady=8)
        
        # Name
        name_label = Label(left_inside_frame, text="NAME:", font=("times new roman", 10, "bold"), bg="white")
        name_label.grid(row=1, column=0)
        
        name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("times new roman", 10, "bold"))
        name_entry.grid(row=1, column=1, pady=8)
        
        # Department
        dept_label = Label(left_inside_frame, text="DEPARTMENT:", font=("times new roman", 10, "bold"), bg="white")
        dept_label.grid(row=1, column=2)
        
        dept_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep, font=("times new roman", 10, "bold"))
        dept_entry.grid(row=1, column=3, pady=8)
        
        # Time
        time_label = Label(left_inside_frame, text="TIME:", font=("times new roman", 10, "bold"), bg="white")
        time_label.grid(row=2, column=0)
        
        time_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=("times new roman", 10, "bold"))
        time_entry.grid(row=2, column=1, pady=8)
        
        # Date
        date_label = Label(left_inside_frame, text="DATE:", font=("times new roman", 10, "bold"), bg="white")
        date_label.grid(row=2, column=2)
        
        date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 10, "bold"))
        date_entry.grid(row=2, column=3, pady=8)
        
        # Attendance Status
        attendance_label = Label(left_inside_frame, text="ATTENDANCE STATUS:", bg="white", font="comicsansns 10 bold")
        attendance_label.grid(row=3, column=0)
        
        self.atten_status = ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansns 10 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)
        
        # Button frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=290, width=640, height=35)
        
        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv, width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn = Button(btn_frame, text="Update", width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=670, y=10, width=580, height=365)
        
        tab_frame = Frame(right_frame, bd=2, relief=RIDGE)
        tab_frame.place(x=5, y=5, width=565, height=300)
        
        #============================SCROLL BAR===============================================
        scroll_x=ttk.Scrollbar(tab_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(tab_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(tab_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_Y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
       
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        #============================================fetch data =====================================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #IMPORT CSV        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file", "*.csv"), ("All Files", "*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
            
    #EXPORT CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file", "*.csv"), ("All Files", "*.*")),parent=self.root)  
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        #===================================reset=========================================
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
            
        
                            
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
