from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
import os

class TrainData:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face recognition system')

        title_lbl = Label( text= 'Train Data Set', font= ('times new roman', 35, 'bold'), bg= 'white', fg= 'green')
        title_lbl.place(x=0,y=0, width= 1530, height=54)

        train_btn = Button(self.root,text = 'Train Data',command=self.train_data, bg= 'blue', fg= 'white',font= ('times new roman', 20, 'bold'))
        train_btn.place(x=0, y=100, width= 1500, height=100)

    def train_data(self):
        data_dir = ('data')
        path = [os.path.join(data_dir, image) for image in os.listdir(data_dir)]
        
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imgNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)

            cv2.imshow('Training data', imgNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # -------------- training classifier -----------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, id)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo('Success',"Training data is completed")





if __name__ == '__main__':
    root = Tk()
    obj = TrainData(root)
    root.mainloop()