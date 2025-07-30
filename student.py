from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        
        
        
        # First Image
        img = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\images.jpeg")
        img = img.resize((500, 135), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=135)

        # Second Image
        img1 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\img2.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\img1.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)
        
        
         # Background Image
        img3 = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\bg_image.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=40)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1500,height=675)
        
                #left lebel frame
        
        left_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=650, height=435)
        
        img_left = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\mri.jpeg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl2 = Label(left_frame, image=self.photoimg_left)
        f_lbl2.place(x=5, y=0, width=640, height=80)
        
          #current course
        current_course_frame = LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=65,width=640, height=95)
        
        #Deparment
        dep_lebel=Label(current_course_frame,text="Department",font=("times new roman", 10, "bold"),bg="white")
        dep_lebel.grid(row=0,column=0,padx=10)
        
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 10, "bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer","IT","CIVIL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)
        
        #Course
        course_lebel=Label(current_course_frame,text="Course",font=("times new roman", 10, "bold"),bg="white")
        course_lebel.grid(row=0,column=2,padx=10,sticky=W)
        
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 10, "bold"),state="readonly",width=17)
        course_combo["values"]=("Select course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_lebel=Label(current_course_frame,text="Year",font=("times new roman", 10, "bold"),bg="white")
        year_lebel.grid(row=1,column=0,padx=10,sticky=W)
        
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 10, "bold"),state="readonly",width=17)
        year_combo["values"]=("Select year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
         #Semester
        sem_lebel=Label(current_course_frame,text="Semester",font=("times new roman", 10, "bold"),bg="white")
        sem_lebel.grid(row=1,column=2,padx=10,sticky=W)
        
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 10, "bold"),state="readonly",width=17)
        sem_combo["values"]=("Select semester","semester-1","semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
         #class student information
        class_student__frame = LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student__frame.place(x=5, y=160,width=640, height=250)
        
        #studentid
        stuId_lebel=Label(class_student__frame,text="StudentID:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_std_id,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #studentname
        stuId_lebel=Label(class_student__frame,text="Student Name:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_std_name,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        stuId_lebel=Label(class_student__frame,text="Class Division:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_div,width=20,font=("times new roman", 10, "bold"))
        #studentID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student__frame,textvariable=self.var_div,font=("times new roman", 10, "bold"),state="readonly",width=17)
        div_combo["values"]=("A","B","C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        #ROLLNO
        stuId_lebel=Label(class_student__frame,text="Rollno:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_roll,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #GENDER
        stuId_lebel=Label(class_student__frame,text="Gender:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        #studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_gender,width=20,font=("times new roman", 10, "bold"))
        #studentID_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student__frame,textvariable=self.var_gender,font=("times new roman", 10, "bold"),state="readonly",width=17)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        #DOB
        stuId_lebel=Label(class_student__frame,text="DOB:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_dob,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #EMAIL
        stuId_lebel=Label(class_student__frame,text="EMAIL:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_email,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #PHONENO
        stuId_lebel=Label(class_student__frame,text="Phoneno:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_phone,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #ADDRESS
        stuId_lebel=Label(class_student__frame,text="Address:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_address,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #TEACHER NAME
        stuId_lebel=Label(class_student__frame,text="Teacher Name:",font=("times new roman", 10, "bold"),bg="white")
        stuId_lebel.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student__frame,textvariable=self.var_teacher,width=20,font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student__frame,variable=self.var_radio1,text="take photo sample",value="yes")
        Radiobutton1.grid(row=5,column=0) 
        
        
        Radiobutton2=ttk.Radiobutton(class_student__frame,variable=self.var_radio1,text="No photo sample",value="No")
        Radiobutton2.grid(row=5,column=1)  
        
        #button frame
        btn_frame=Frame(class_student__frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=190,width=635,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        Update_btn=Button(btn_frame,text="Update",command=self.update_data, width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
        takephoto_btn=Button(btn_frame,text="Take photo",command=self.generate_dataset,width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=4)
       
        updatephoto_btn=Button(btn_frame,text="Update photo", width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=0,column=5)
        
        #right lebel frame
        
        right_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=670, y=10, width=580, height=435)
        
        img_right = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\top.jpeg")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl2 = Label(right_frame, image=self.photoimg_right)
        f_lbl2.place(x=5, y=0, width=640, height=80)
        
          
        #=====================================SEARCH SYSTEM=======================================
        search_frame = LabelFrame(right_frame, bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=80,width=640, height=60)  
        
        search_lebel=Label(search_frame,text="Search By:",font=("times new roman", 10, "bold"),bg="white")
        search_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)   
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman", 10, "bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Rollno","phoneno")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 10, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W) 
        
        #Update_btn=Button(btn_frame,text="Update", width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        #Update_btn.grid(row=0,column=1)
        
        search_btn=Button(search_frame,text="Search", width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        show_btn=Button(search_frame,text="Show All", width=14,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4,padx=4)
        
           #================================TABLE FRAME=============================================
        table_frame =Frame(right_frame, bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5, y=150,width=570, height=250)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
                
    #====================================function DECRETION========================================= 
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due To: {str(ex)}", parent=self.root)
            finally:
                if 'conn' in locals() and conn.is_connected():
                    my_cursor.close()
                    conn.close()
                    
                    
    #=============================FETCH DATA=========================================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #======================================GET CURSOR=======================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"] 
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]), 
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]), 
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]), 
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
        
    #===========================================UPDATE FUNCTION========================================
   
    
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSampleStatus=%s WHERE StudentID=%s",
                                  (
                                      self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_gender.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      "Yes",  # Assuming 'Yes' indicates PhotoSample present
                                      self.var_std_id.get()
                                  )
                              )
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Photo sample status updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

        
   
   
    #========================================DELETE FUNCTION===================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want TO Delete This Student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()  
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),) 
                    my_cursor.execute(sql,val)
                else:
                    if not delete :
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
                
                
    #==========================================RESET==============================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    #=====================================Generate data set take photo samples=================
    def generate_dataset(self):
      if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
          messagebox.showerror("Error", "All Fields are required", parent=self.root)
      else:
          try:
              Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
              if Update:
                  conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                  my_cursor = conn.cursor()
                  my_cursor.execute("select * from student")
                  myresult = my_cursor.fetchall()
                  id = 0
                  for x in myresult:
                      id += 1
                      my_cursor.execute(
                          "update student set Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSampleStatus=%s where StudentID=%s",
                          (
                              self.var_dep.get(),
                              self.var_course.get(),
                              self.var_year.get(),
                              self.var_semester.get(),
                              self.var_div.get(),
                              self.var_roll.get(),
                              self.var_gender.get(),
                              self.var_dob.get(),
                              self.var_email.get(),
                              self.var_phone.get(),
                              self.var_address.get(),
                              self.var_teacher.get(),
                              "Yes",  # Assuming 'Yes' indicates PhotoSample present
                              self.var_std_id.get()
                              )
                          )
                      conn.commit()
                      self.fetch_data()
                      self.reset_data()
                      conn.close()
                      face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                      def face_cropped(img):
                          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                          faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                          for (x, y, w, h) in faces:
                              face_cropped = img[y:y+h, x:x+w]
                              return face_cropped
                          return None
                      cap = cv2.VideoCapture(0)
                      img_id = 0
                      while True:
                          ret, my_frame = cap.read()
                          if ret:
                              cropped_face = face_cropped(my_frame)
                              if cropped_face is not None:
                                  img_id += 1
                                  face = cv2.resize(cropped_face, (450, 450))
                                  face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                  file_name_path = f"data/user.{id}.{img_id}.jpeg"
                                  cv2.imwrite(file_name_path, face)
                                  cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                                  cv2.imshow("Cropped Face", face)
                                  if cv2.waitKey(1) == 13 or img_id == 100:
                                      break
                                  cap.release()
                                  cv2.destroyAllWindows()
                                  messagebox.showinfo("Result", "Generating data sets completed!!!")
                
          except Exception as es:
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()         