from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face recognition system')


        # ---------- variables ---------
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_semester = StringVar()
        self.var_email = StringVar()
        self.var_mobile = StringVar()
        self.var_year = StringVar()
        self.var_gender = StringVar()

        

        title_lbl = Label( text= 'Face recognition Attendance Sysetm', font= ('times new roman', 35, 'bold'), bg= 'blue', fg= 'red')
        title_lbl.place(x=0,y=0, width= 1530, height=54)

        img = Image.open(r'D:\Programming\Artificial Intelligence\facial_attendance\images\face_recognition.jpg')
        img = img.resize((1830, 800), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        bgImg = Label(self.root, image= self.photoImg)
        bgImg.place(x=0, y=55, width=1830, height=800)

        main_frame = Frame(bgImg, bd= 2, bg= 'white')
        main_frame.place(x=5, y= 55, width=1600, height=800 )

        # left label 
        left_frame = LabelFrame(main_frame, bd=2,bg = 'white', relief= RIDGE, text= 'Students details', font= ('times new roman', 12, 'bold') )
        left_frame.place(x=10, y=10, width= 750, height= 780)
        
        # left label inner frame
        f_lbl = Label(left_frame,bg='skyblue')
        f_lbl.place(x=5,y=0,width=720,height=130)

        # current course
        current_frame = LabelFrame(left_frame, bd=2,bg = 'white', relief= RIDGE, text= 'Current Course Information', font= ('times new roman', 12, 'bold') )
        current_frame.place(x=10, y=140, width= 720, height= 130)

        # department
        dep_label = Label(current_frame, text="Department",font= ('times new roman', 12, 'bold'), bg= 'white')
        dep_label.grid(row = 0, column = 0, padx=10)

        dep_combo = ttk.Combobox(current_frame,textvariable=self.var_dep, font= ('times new roman', 12, 'bold'),width=20,  state= 'readonly')
        dep_combo['values'] = ('select department', 'Software Engineering','Pharmacy', 'Civil', 'Textile' )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady= 10)


        # course
        dep_label = Label(current_frame, text="Course",font= ('times new roman', 12, 'bold'), bg= 'white')
        dep_label.grid(row = 0, column = 2, padx=10)

        dep_combo = ttk.Combobox(current_frame,textvariable=self.var_course, font= ('times new roman', 12, 'bold'),width=20,  state= 'readonly')
        dep_combo['values'] = ('select course', 'Math','English', 'Physics', 'Biology' )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=2, pady= 10)


        # Year
        dep_label = Label(current_frame, text="Year",font= ('times new roman', 12, 'bold'), bg= 'white')
        dep_label.grid(row = 1, column = 0, padx=10)

        dep_combo = ttk.Combobox(current_frame,textvariable=self.var_year, font= ('times new roman', 12, 'bold'),width=20,  state= 'readonly')
        dep_combo['values'] = ('select year', '2022','2023', '2024', '2025' )
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, padx=2, pady=10)

        # Semester
        dep_label = Label(current_frame, text="Semester",font= ('times new roman', 12, 'bold'), bg= 'white')
        dep_label.grid(row = 1, column = 2, padx=10)

        dep_combo = ttk.Combobox(current_frame,textvariable=self.var_semester, font= ('times new roman', 12, 'bold'),width=20,  state= 'readonly')
        dep_combo['values'] = ('select course', 'First Semester','Second Semester', 'Third Semester', 'Fourth Semester' )
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=2, pady= 10)

        # class student information
        info_frame = LabelFrame(left_frame, bd=2,bg = 'white', relief= RIDGE, text= "Student's Information", font= ('times new roman', 12, 'bold') )
        info_frame.place(x=10, y=280, width= 720, height= 350)

        # id
        id_label = Label(info_frame, text="Student's id",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 0, column = 0,)

        id_entry = ttk.Entry(info_frame,textvariable=self.var_id, font= ('times new roman', 12, 'bold') ,)
        id_entry.grid(row=0, column=1,pady=10, padx= 10,)


        # name
        name_label = Label(info_frame, text="Name",font= ('times new roman', 12, 'bold'), bg= 'white')
        name_label.grid(row = 0, column = 2,)

        name_entry = ttk.Entry(info_frame,textvariable=self.var_name, font= ('times new roman', 12, 'bold') )
        name_entry.grid(row=0, column=3,pady=10, padx= 10)

        # section
        section_label = Label(info_frame, text="Section",font= ('times new roman', 12, 'bold'), bg= 'white')
        section_label.grid(row = 1, column = 0,)

        section_entry = ttk.Entry(info_frame,textvariable=self.var_section,font= ('times new roman', 12, 'bold') )
        section_entry.grid(row=1, column=1,pady=10, padx= 10)


        # gender
        id_label = Label(info_frame, text="Gender",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 1, column = 2,)

        id_entry = ttk.Entry(info_frame,textvariable=self.var_gender, font= ('times new roman', 12, 'bold') )
        id_entry.grid(row=1, column=3,pady=10, padx= 10)


        # email
        name_label = Label(info_frame, text="Email",font= ('times new roman', 12, 'bold'), bg= 'white')
        name_label.grid(row = 2, column = 0,pady=10, padx= 10)

        name_entry = ttk.Entry(info_frame,textvariable=self.var_email, font= ('times new roman', 12, 'bold') )
        name_entry.grid(row=2, column=1,pady=10, padx= 10)

        # mobile
        section_label = Label(info_frame, text="mobile",font= ('times new roman', 12, 'bold'), bg= 'white')
        section_label.grid(row = 2, column =2,pady=10, padx= 10)

        section_entry = ttk.Entry(info_frame,textvariable=self.var_mobile, font= ('times new roman', 12, 'bold') )
        section_entry.grid(row=2, column=3,pady=10, padx= 10)


        # radio button
        self.radio_btn = StringVar()
        radio_btn = ttk.Radiobutton(info_frame,variable=self.radio_btn, text= 'Take Photo Sample',value= 'Yes')
        radio_btn.grid(row=3, column=0)

        radio_btn2 = ttk.Radiobutton(info_frame,variable=self.radio_btn, text= 'No Photo Sample', value = "No" )
        radio_btn2.grid(row=3, column=1)



        # button frame
        btn_frame = Frame(info_frame, relief= RIDGE, bg= 'white')
        btn_frame.place(x=0, y=200, width=700, height=120)

        save_btn = Button(btn_frame,command=self.add_data, text = 'Save', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        save_btn.grid(row=0, column=0, padx=1, pady= 10)

        update_btn = Button(btn_frame,command = self.update_data,text = 'Update', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        update_btn.grid(row=0, column=1, padx=1, pady= 10)

        delete_btn = Button(btn_frame,command = self.delete_data, text = 'Delete', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        delete_btn.grid(row=0, column=2, padx=1, pady= 10)

        reset_btn = Button(btn_frame,command=self.reset_data,text = 'Reset', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        reset_btn.grid(row=0, column=3, padx=1, pady= 10)

        # sample frame
        sample_frame = Frame(info_frame, relief= RIDGE, bg= 'white')
        sample_frame.place(x=0, y=250, width=700, height=50, )

        take_sample_btn = Button(sample_frame,command=self.generate_data, text="Take Photo Sample",font= ('times new roman', 12, 'bold'), width= 25, bg= 'blue', fg='white')
        take_sample_btn.grid(row=1, column=0, padx= 50, pady= 10)

        update_sample_btn = Button(sample_frame, text= "Update Photo Sample",font= ('times new roman', 12, 'bold'), width= 25, bg= 'blue', fg= 'white')
        update_sample_btn.grid(row=1, column=1, padx= 50, pady= 10)



        # # right frame
        right_frame = LabelFrame(main_frame, bd=2,bg = 'white', relief= RIDGE, text= 'Students Attendance Search', font= ('times new roman', 12, 'bold') )
        right_frame.place(x=780, y=10, width= 650, height= 780)

        f_lbl = Label(right_frame, bg='darkblue')
        f_lbl.place(x=0,y=0, width=620, height=130)


        # ======== search ======

        search_frame = LabelFrame(right_frame, bd=2, text='Search System', bg='white',font= ('times new roman', 12, 'bold'))
        search_frame.place(x=0,y= 150, width=620, height=100)

        search_label = Label(search_frame, text='Search by:',font= ('times new roman', 12, 'bold'))
        search_label.grid(row=0,column=0)

        search_combo = ttk.Combobox(search_frame, font= ('times new roman', 12, 'bold'), state= 'readonly')
        search_combo['values'] = ('Select', 'name', 'mobile')
        search_combo.current(0)
        search_combo.grid(row=0, column=1,)


        search_entry = ttk.Entry(search_frame,font= ('times new roman', 12, 'bold'))
        search_entry.grid(row=0, column=2,pady=5, padx= 10)

        search_btn = Button(search_frame,text = 'Search', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'))
        search_btn.grid(row=0, column=3, padx=5, pady= 10)

        showAll_btn = Button(search_frame,text = 'Show All', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'))
        showAll_btn.grid(row=0, column=4, padx=5, pady= 10)


        # -------- table frame -----------

        search_frame = LabelFrame(right_frame, bd=2, bg= 'white', relief= RIDGE)
        search_frame.place(x=0,y= 260, width=620, height=200)

        scroll_x = ttk.Scrollbar(search_frame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(search_frame, orient= VERTICAL)

        self.student_table = ttk.Treeview(search_frame, column=('id','name','dep', 'section','course','semester','mobile', 'year', 'email',"gender"))

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('id', text="Student's id")
        self.student_table.heading('name', text= 'Name')
        self.student_table.heading('dep', text='Department')
        self.student_table.heading('section', text= 'Section')
        self.student_table.heading('course', text='Course')
        self.student_table.heading('semester', text= 'Semester')
        self.student_table.heading('mobile', text= 'Mobile')
        self.student_table.heading('year', text='Year')
        self.student_table.heading('email', text= 'Email')
        self.student_table.heading('gender', text= 'Gender')

        self.student_table['show'] = 'headings'

        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("section", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("mobile", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()



        # ======== Add data =======
    def add_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_id.get() == '':
            messagebox.showerror("Error","All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'S1234@', database = 'face_recognition')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)', (

                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_section.get(),
                    self.var_course.get(),
                    self.var_semester.get(),
                    self.var_mobile.get(),
                    self.var_year.get(),
                    self.var_email.get(),
                    self.var_gender.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", 'students details has been saved', parent = self.root)

            except Exception as es:
                messagebox.showinfo("error", f'(Due to {str(es)})', parent = self.root)

    # -------------- fetch data -----------------
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost',username = 'root', password = 'S1234@', database = 'face_recognition' )
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student')
        data = my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('', END, values=i)
            conn.commit()

        conn.close()

    # ============= get cursor ==============

    def get_cursor(self, event = ''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_section.set(data[3]),
        self.var_course.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_mobile.set(data[6]),
        self.var_year.set(data[7]),
        self.var_email.set(data[8]),
        self.var_gender.set(data[9])
        # self.radio_btn.set(data[10])

    # ------- update ---------
    def update_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_id.get() == '':
            messagebox.showerror("Error","All fields are required", parent = self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "do you want to update ?")
                if update > 0:
                    conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'S1234@', database = 'face_recognition')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set name=%s, department= %s, section= %s, course=%s, semester= %s,mobile= %s, year= %s, email= %s, gender= %s  where id= %s",(

                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_section.get(),
                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_mobile.get(),
                        self.var_year.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_id.get(),
                    ))

                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details is successfully updated", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent = self.root)

    # ---------- delete ----------
    def delete_data(self):
        if self.var_id == "":
            messagebox.showerror("Error", "Id required")
        else:
            try:
                delete = messagebox.askyesno('Alart', 'Do you want to delete ?')
                if delete > 0:
                    conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'S1234@', database = 'face_recognition')
                    my_cursor = conn.cursor()
                    sql = 'delete from student where id = %s'
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Deleted', 'Successfully deleted', parent = self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"{str(es)}")


    # ========== reset =========
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_section.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_email.set("")
        self.var_mobile.set("")
        self.var_year.set("Select Year")
        self.var_gender.set("")
        # self.radio_btn.set("")


    # ========== generate data set ============
    def generate_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_name.get() == '' or self.var_id.get() == '':
            messagebox.showerror("Error","All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'S1234@', database = 'face_recognition')
                my_cursor = conn.cursor()
                my_cursor.execute(" select * from student")
                my_result = my_cursor.fetchall()
                id = 0

                for i in my_result:
                    id +=1
                
                my_cursor.execute("update student set name=%s, department= %s, section= %s, course=%s, semester= %s,mobile= %s, year= %s, email= %s, gender= %s  where id= %s",(

                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_section.get(),
                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_mobile.get(),
                        self.var_year.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_id.get() == id+1
                    ))


                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # -------- classifier ---------
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(1)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path = 'data/user.'+ str(id)+'.'+str(img_id)+'.jpg'
                        cv2.imwrite(file_path, face  )
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('cropped face', face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 10:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'comleted')

            except Exception as es:
                messagebox.showerror("Error", f"{str(es)}")


                





        

if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()