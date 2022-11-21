from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
from main import Face_recognition_system

# def main():
#     root = Tk()
#     app = Login_window(root)
#     root.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1350x700")

        self.bg = ImageTk.PhotoImage(file=r"D:\Programming\Artificial Intelligence\facial_attendance\images\image_blue.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=340, height=450)

        # diu image
        img = Image.open(r"D:\Programming\Artificial Intelligence\facial_attendance\images\diu2.png")
        img = img.resize((120, 120), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        lbl_img = Label(frame,image=self.photoImg, bg="white", bd=0)
        lbl_img.place(x=100, y=30, width=150, height=120)

        # username

        lbl_user = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_user.place(x=50, y=170)

        self.txt_user = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_user.place(x=50, y=200, width=250)

        # password
        lbl_pass = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_pass.place(x=50, y=230)

        self.txt_pass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_pass.place(x=50, y=260, width=250)

        # login button
        btn_login = Button(frame, text="Login",command=self.login_user, font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2", activebackground="blue", activeforeground="white")
        btn_login.place(x=50, y=310, width=250, height=35)

        # registration button
        btn_reg = Button(frame, text="Register New User",command=self.register_window, font=("times new roman", 10, "bold"),borderwidth=0, bg="white", fg="black", cursor="hand2", activebackground="white", activeforeground="black")
        btn_reg.place(x=11, y=360, width=100)

        # forget password button
        btn_forget = Button(frame, text="Forget Password",command=self.forget_password_window, font=("times new roman", 10, "bold"),borderwidth=0, bg="white", fg="black", cursor="hand2", activebackground="white", activeforeground="black")
        btn_forget.place(x=7, y=390, width=100)

    # registration window

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # login
    def login_user(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="S1234@", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (self.txt_user.get(), self.txt_pass.get()))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showinfo("Error", "Invalid Username or Password", parent=self.root)
            else:
                self.new_window = Toplevel(self.root)
                self.app = Face_recognition_system(self.new_window)
            conn.commit()
            conn.close()

    # reset
    def reset(self):
        if self.security_question_entry() == "Select" or self.answer_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        elif self.new_password_entry.get() == "" :
            messagebox.showerror("Error", "New Password field is required", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="S1234@", database="face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and security_question=%s and answer=%s")
            value = (self.txt_user.get(), self.security_question_entry.get(), self.answer_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please select correct security question and answer", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.new_password_entry.get(), self.txt_user.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with new password", parent=self.root2)
                self.root2.destroy()


    # forget password window-------------------

    def forget_password_window(self):
        if self.txt_user.get() == "":
            messagebox.showerror("Error", "Please enter your email address to reset your password", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username = "root", password = "S1234@", database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txt_user.get(),) 
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Please enter a valid email address", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password",)
                self.root2.geometry("340x450+610+170")

                
                # security question
                lbl_security = Label(self.root2, text="Forget Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                lbl_security.place(x=80, y=5)

                security_question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_question.place(x=50, y=80)

                security_question_entry = ttk.Combobox(self.root2, font=("times new roman", 13, "bold"), state="readonly")
                security_question_entry['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                security_question_entry.current(0)
                security_question_entry.place(x=50, y=110, width=250)

                # answer
                answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                answer.place(x=50, y=150)
                answer_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                answer_entry.place(x=50, y=180, width=250)


                # password
                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)
                new_password_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                new_password_entry.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2", activebackground="blue", activeforeground="white")
                btn.place(x=50, y=300, width=250, height=35)

        


# class Register:
#     def __init__(self,root):
#         self.root = root
#         self.root.title("Register")
#         self.root.geometry("1350x700+0+0")

#         # ------ variables ------
#         self.var_fname = StringVar()
#         self.var_lname = StringVar()
#         self.var_contact = StringVar()
#         self.var_email = StringVar()
#         self.var_security_question = StringVar()
#         self.var_security_answer = StringVar()
#         self.var_password = StringVar()
#         self.var_confirm_password = StringVar()


#         self.bg = ImageTk.PhotoImage(file=r"D:\Programming\Artificial Intelligence\facial_attendance\images\image_blue.jpg")
#         lbl_bg = Label(self.root, image=self.bg)
#         lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


#         frame = Frame(self.root, bg="white")
#         frame.place(x=400, y=100, width=700, height=450)

#         # register lebel
#         register_lebel = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="black")
#         register_lebel.place(x=250, y=10, width=200)

#         # form

#         # first name
#         f_name = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         f_name.place(x=50, y=70)

#         fname_entry = ttk.Entry(frame,textvariable=self.var_fname , font=("times new roman", 15, "bold"))
#         fname_entry.place(x=50, y=100, width=250)

#         # last name
#         l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         l_name.place(x=350, y=70)
#         lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
#         lname_entry.place(x=350, y=100, width=250)

#         # contact
#         contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         contact.place(x=50, y=130)
#         contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
#         contact_entry.place(x=50, y=160, width=250)

#         # email
#         email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         email.place(x=350, y=130)
#         email_entry = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
#         email_entry.place(x=350, y=160, width=250)

#         # security question
#         security_question = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         security_question.place(x=50, y=190)
#         security_question_entry = ttk.Combobox(frame,textvariable=self.var_security_question, font=("times new roman", 13, "bold"), state="readonly")
#         security_question_entry['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
#         security_question_entry.current(0)
#         security_question_entry.place(x=50, y=220, width=250)

#         # answer
#         answer = Label(frame, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         answer.place(x=350, y=190)
#         answer_entry = ttk.Entry(frame,textvariable=self.var_security_answer, font=("times new roman", 15, "bold"))
#         answer_entry.place(x=350, y=220, width=250)


#         # password
#         password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         password.place(x=50, y=250)
#         password_entry = ttk.Entry(frame,textvariable=self.var_password, font=("times new roman", 15, "bold"))
#         password_entry.place(x=50, y=280, width=250)


#         # confirm password
#         confirm_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
#         confirm_password.place(x=350, y=250)
#         confirm_password_entry = ttk.Entry(frame,textvariable=self.var_confirm_password, font=("times new roman", 15, "bold"))
#         confirm_password_entry.place(x=350, y=280, width=250)


#         # check button
#         self.var_check = IntVar()
#         check_btn = Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Conditions", onvalue=1, offvalue=0, bg="white", font=("times new roman", 12, "bold"))
#         check_btn.place(x=50, y=310)


#         # button
#         img = Image.open(r"D:\Programming\Artificial Intelligence\facial_attendance\images\register.png")
#         img = img.resize((150,60), Image.ANTIALIAS)
#         self.photoimg = ImageTk.PhotoImage(img)
#         b1 = Button(frame, image=self.photoimg,command=self.register_data, cursor="hand2", borderwidth=0, activebackground='white')
#         b1.place(x=50, y=350, width=150, height=60)


#         img2 = Image.open(r"D:\Programming\Artificial Intelligence\facial_attendance\images\login.jpg")
#         img2 = img2.resize((150,60), Image.ANTIALIAS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)
#         b2 = Button(frame, image=self.photoimg2, cursor="hand2", borderwidth=0, activebackground='white')
#         b2.place(x=300, y=350, width=150, height=60)

#     # function declaration
#     def register_data(self):
#         if self.var_fname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_security_question.get() == "Select" or self.var_security_answer.get() == "":
#             messagebox.showerror("Error", "All Fields are required", parent=self.root)
#         elif self.var_password.get() != self.var_confirm_password.get():
#             messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
#         elif self.var_check.get() == 0:
#             messagebox.showerror("Error", "Please Agree our terms and conditions", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(host="localhost", username="root", password="S1234@", database="face_recognition")
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("select * from register where email=%s", (self.var_email.get(),))
#                 row = my_cursor.fetchone()
#                 if row != None:
#                     messagebox.showerror("Error", "User already exist, please try with another email", parent=self.root)
#                 else:
#                     my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
#                         self.var_fname.get(),
#                         self.var_lname.get(),
#                         self.var_contact.get(),
#                         self.var_email.get(),
#                         self.var_security_question.get(),
#                         self.var_security_answer.get(),
#                         self.var_password.get()
#                     ))

#                     conn.commit()
#                     conn.close()
#                     messagebox.showinfo("Success", "Register Successfully", parent=self.root)
            
#             except Exception as es:
#                 messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()