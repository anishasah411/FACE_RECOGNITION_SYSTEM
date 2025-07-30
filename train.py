from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
from tkinter import messagebox
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 25, "bold"), bg="white", fg="RED")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        
        img_top = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\ts.jpeg")
        img_top = img_top.resize((1530, 250), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=1530, height=250)
        
        # BUTTON
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="RED", fg="white")
        b1_1.place(x=0, y=300, width=1530, height=60)
        
        img_botm = Image.open(r"C:\Users\anisha\Desktop\face recognition\college_images\tos.jpeg")
        img_botm = img_botm.resize((1530, 250), Image.LANCZOS)
        self.photoimg_botm = ImageTk.PhotoImage(img_botm)

        f_lbl2 = Label(self.root, image=self.photoimg_botm)
        f_lbl2.place(x=0, y=360, width=1530, height=250)
        
    def train_classifier(self):
        print("Starting training classifier")
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory does not exist!")
            print("Data directory does not exist")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpeg') or file.endswith('.png')]
        if len(path) == 0:
            messagebox.showerror("Error", "No images found in the data directory!")
            print("No images found in the data directory")
            return

        faces = []
        ids = []
        for image in path:
            try:
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')
                filename = os.path.split(image)[1]
                id_str = os.path.splitext(filename)[0].split('.')[1]  # Extracting ID from filename
                id = int(id_str)
                faces.append(imageNp)
                ids.append(id)
                print(f"Processed image {filename} with ID {id}")
            except Exception as e:
                print(f"Error processing image {image}: {e}")

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid images found for training!")
            return

        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!!")
        print("Training completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 