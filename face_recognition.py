from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
import os
from time import strftime
from datetime import datetime

class Recogniton:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face recognition system')

        title_lbl = Label( text= 'Face Recognition', font= ('times new roman', 35, 'bold'), bg= 'white', fg= 'blue')
        title_lbl.place(x=0,y=0, width= 1530, height=54)

        b1 = Button(text = 'Detect face', cursor='hand2',font= ('times new roman', 20, 'bold'), bg= 'dark blue', fg= 'white')
        b1.place(x=200,y=200,width=250, height=80)


    # -------------- Recognize --------------
    def face_reognizer(self):
        def draw_rect(img, classifier, scalefector, minNeigh, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scalefector, minNeigh)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0), 2)
                id, predict = clf.predict(gray[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'S1234@', database = 'face_recognition')
                my_cursor = conn.cursor()

                my_cursor.execute(" select name from student where id"+ str(id))
                n = my_cursor.fetchone()
                n = '+'.join(n)

                my_cursor.execute(" select id from student where id"+ str(id))
                i = my_cursor.fetchone()
                i = '+'.join(i)

                if confidence > 75:
                    cv2.putText(img,f"name:{n}",(x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img,f"ID:{i}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    self.mark_attendance(i,n)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 2)
                    cv2.putText(img, "Unknown Face",(x,y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                coord = [x,y,w,h]

            return coord

        def call_recognizer(img,clf, faceCasecade):
            coord = draw_rect(img,faceCasecade,1.1,10, clf)
            return img

        faceCasecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)

        while True:
            ret, image = video_cap.read()
            img = call_recognizer(image,clf,faceCasecade)
            cv2.imshow('Welcome', img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


    # --------- Attendance -----------
    def mark_attendance(self,i,n):
        with open('shakil.csv',"r+", newline='\n') as f:
            my_data = f.readlines()
            name_list = []
            for word in my_data:
                entry = word.split(",")
                name_list.append(entry[0])
            if (i not in name_list) and (n not in name_list):
                now = datetime.now()
                d = now.strftime("%d/%m/%Y")
                time_now = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{n},{time_now},{d}, Present ")



        



if __name__ == '__main__':
    root = Tk()
    obj = Recogniton(root)
    root.mainloop()