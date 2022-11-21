from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1350x700")

        # ------ variables ------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_question = StringVar()
        self.var_security_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()


        self.bg = ImageTk.PhotoImage(file=r"D:\Programming\Artificial Intelligence\facial_attendance\images\image_blue.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=100, width=700, height=450)

        # register lebel
        register_lebel = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="black")
        register_lebel.place(x=250, y=10, width=200)

        # form

        # first name
        f_name = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        f_name.place(x=50, y=70)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname , font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=100, width=250)

        # last name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=350, y=70)
        lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lname_entry.place(x=350, y=100, width=250)

        # contact
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=130)
        contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=160, width=250)

        # email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=350, y=130)
        email_entry = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        email_entry.place(x=350, y=160, width=250)

        # security question
        security_question = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_question.place(x=50, y=190)
        security_question_entry = ttk.Combobox(frame,textvariable=self.var_security_question, font=("times new roman", 13, "bold"), state="readonly")
        security_question_entry['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        security_question_entry.current(0)
        security_question_entry.place(x=50, y=220, width=250)

        # answer
        answer = Label(frame, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        answer.place(x=350, y=190)
        answer_entry = ttk.Entry(frame,textvariable=self.var_security_answer, font=("times new roman", 15, "bold"))
        answer_entry.place(x=350, y=220, width=250)


        # password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=250)
        password_entry = ttk.Entry(frame,textvariable=self.var_password, font=("times new roman", 15, "bold"))
        password_entry.place(x=50, y=280, width=250)


        # confirm password
        confirm_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_password.place(x=350, y=250)
        confirm_password_entry = ttk.Entry(frame,textvariable=self.var_confirm_password, font=("times new roman", 15, "bold"))
        confirm_password_entry.place(x=350, y=280, width=250)


        # check button
        self.var_check = IntVar()
        check_btn = Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Conditions", onvalue=1, offvalue=0, bg="white", font=("times new roman", 12, "bold"))
        check_btn.place(x=50, y=310)


        # button
        img = Image.open(r"D:\Programming\Artificial Intelligence\facial_attendance\images\register.png")
        img = img.resize((150,60), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimg,command=self.register_data, cursor="hand2", borderwidth=0, activebackground='white')
        b1.place(x=50, y=350, width=150, height=60)


        img2 = Image.open(r"D:\Programming\Artificial Intelligence\facial_attendance\images\login.jpg")
        img2 = img2.resize((150,60), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(frame, image=self.photoimg2, cursor="hand2", borderwidth=0, activebackground='white')
        b2.place(x=300, y=350, width=150, height=60)

    # function declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_security_question.get() == "Select" or self.var_security_answer.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree our terms and conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="S1234@", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s", (self.var_email.get(),))
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exist, please try with another email", parent=self.root)
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_security_question.get(),
                        self.var_security_answer.get(),
                        self.var_password.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Register Successfully", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
