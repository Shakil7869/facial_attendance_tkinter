from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from train import TrainData
from face_recognition import Recogniton
from attendance import Attendance
from time import strftime
from datetime import datetime

class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face recognition system')

        img = Image.open(r"C:\Users\Asus\Pictures\attendance.jpg")
        # img = img.resize((500,130), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoImg)
        f_lbl.place(x = 0, y =0)

        title_lbl = Label(f_lbl, text= 'Face recognition Attendance Sysetm', font= ('times new roman', 35, 'bold'), bg= 'blue', fg= 'red')
        title_lbl.place(x=0,y=0, width= 1530, height=54)

        #--------- time -----------
        def time():
            string = strftime('%H:%M:%S %p')
            time_lbl.config(text=string)
            time_lbl.after(1000, time)

        time_lbl = Label(title_lbl, text= 'Face recognition Attendance Sysetm', font= ('times new roman', 35, 'bold'), bg= 'blue', fg= 'red')
        time_lbl.place(x=0,y=0, width= 500, height=50)
        time()
        
        b1 = Button(text = 'Students Details',command=self.student_details, cursor='hand2',font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b1.place(x=200,y=200,width=250, height=80)

        #train data
        b2 = Button(text = 'train data',command=self.train_data, cursor='hand2',font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b2.place(x=600,y=200,width=250, height=80)

        # photos
        b3 = Button(text = 'Photos',command=self.open_image , cursor='hand2',font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b3.place(x=1000,y=200,width=250, height=80)

        # face detector
        b4 = Button(text = 'Face Detection',command=self.face_detect, cursor='hand2',font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b4.place(x=200,y=400,width=250, height=80)

        # attendance
        b5 = Button(text = 'Attendance', cursor='hand2',command=self.attendance,font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b5.place(x=600,y=400,width=250, height=80)


        # exit
        b6 = Button(text = 'Exit', cursor='hand2',command=self.isExit,font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b6.place(x=1000,y=400,width=250, height=80)

     # ========= Student details ============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = TrainData(self.new_window)


    def open_image(self):
        os.startfile("data")

    def face_detect(self):
        self.new_window = Toplevel(self.root)
        self.app = Recogniton(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def isExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition Attendance System", "Confirm if you want to exit",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
            return



if __name__ == '__main__':
    root =Tk()
    obj = Face_recognition_system(root)
    root.mainloop()

    