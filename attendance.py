from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from student import Student
import os
import csv


my_data = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face recognition system')


        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        title_lbl = Label( text= 'Attendance Details', font= ('times new roman', 35, 'bold'), bg= 'white', fg= 'blue')
        title_lbl.place(x=0,y=0, width= 1530, height=54)

        # main
        main_frame = Frame( bd= 2, bg= 'white')
        main_frame.place(x=20, y= 90, width=1600, height=800 )


        # left label
        left_frame = LabelFrame(main_frame, bd=2,bg = 'white', relief= RIDGE, text= 'Students details', font= ('times new roman', 12, 'bold') )
        left_frame.place(x=30, y=90, width= 700, height= 600)

        # left inner
        left_inner_frame = Frame(left_frame,relief=RIDGE, bd= 2, bg= 'white')
        left_inner_frame.place(x=10, y= 55, width=600, height=400 )

        # entry
        # id
        id_label = Label(left_inner_frame, text="Student's id",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 0, column = 0,)

        id_entry = ttk.Entry(left_inner_frame,textvariable=self.var_id, font= ('times new roman', 12, 'bold') ,)
        id_entry.grid(row=0, column=1,pady=10, padx= 10,)

        # name
        id_label = Label(left_inner_frame, text="Name",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 0, column =2,)

        id_entry = ttk.Entry(left_inner_frame,textvariable=self.var_name, font= ('times new roman', 12, 'bold') ,)
        id_entry.grid(row=0, column=3,pady=10, padx= 10,)

        # department
        id_label = Label(left_inner_frame, text="Department",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 1, column = 0,)

        id_entry = ttk.Entry(left_inner_frame,textvariable=self.var_dep, font= ('times new roman', 12, 'bold') ,)
        id_entry.grid(row=1, column=1,pady=10, padx= 10,)

        # time
        id_label = Label(left_inner_frame, text="Time",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 1, column =2 ,)

        id_entry = ttk.Entry(left_inner_frame,textvariable=self.var_time, font= ('times new roman', 12, 'bold') ,)
        id_entry.grid(row=1, column=3,pady=10, padx= 10,)

        # date
        id_label = Label(left_inner_frame, text="Date",font= ('times new roman', 12, 'bold'), bg= 'white')
        id_label.grid(row = 2, column = 0,)

        id_entry = ttk.Entry(left_inner_frame,textvariable=self.var_date, font= ('times new roman', 12, 'bold') ,)
        id_entry.grid(row=2, column=1,pady=10,padx=10)

        # attendance
        dep_label = Label(left_inner_frame, text="Attendance",font= ('times new roman', 12, 'bold'), bg= 'white')
        dep_label.grid(row = 3, column = 0, padx=10)

        dep_combo = ttk.Combobox(left_inner_frame,textvariable=self.var_attendance, font= ('times new roman', 12, 'bold'),width=20,  state= 'readonly')
        dep_combo['values'] = ('Status','Present', 'Absent' )
        dep_combo.current(0)
        dep_combo.grid(row=3, column=1, padx=10, pady= 10)


        # button frame
        btn_frame = Frame(left_inner_frame, relief= RIDGE, bg= 'white')
        btn_frame.place(x=20, y=200, width=550, height=120)

        save_btn = Button(btn_frame, text = 'Import csv',command=self.import_csv, bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        save_btn.grid(row=0, column=0, padx=10, pady= 10)

        update_btn = Button(btn_frame,text = 'Export csv',command=self.export_csv, bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        update_btn.grid(row=0, column=1, padx=10, pady= 10)

        delete_btn = Button(btn_frame, text = 'Update', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        delete_btn.grid(row=1, column=0, padx=10, pady= 10)

        reset_btn = Button(btn_frame,textvariable=self.reset_data,text = 'Reset', bg= 'blue', fg= 'white',font= ('times new roman', 12, 'bold'), width= 18)
        reset_btn.grid(row=1, column=1, padx=10, pady= 10)




        # right label
        right_frame = LabelFrame(main_frame, bd=2,bg = 'white', relief= RIDGE, text= 'Students Attendance', font= ('times new roman', 12, 'bold') )
        right_frame.place(x=780, y=90, width= 700, height= 600)

        # right_inner
        right_inner_frame = Frame(right_frame, relief= RIDGE, bg= 'white')
        right_inner_frame.place(x=20, y=50, width=650, height=400)


        # scroll bar

        scroll_x = ttk.Scrollbar(right_inner_frame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_inner_frame, orient= VERTICAL)

        self.attendance_table = ttk.Treeview(right_inner_frame, column=('id','name','dep', 'time', 'date', 'attendance'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)


        # heading

        self.attendance_table.heading('id', text="ID")
        self.attendance_table.heading('name', text= 'Name')
        self.attendance_table.heading('dep', text='Department')
        self.attendance_table.heading('time', text= 'Time')
        self.attendance_table.heading('date', text='Date')
        self.attendance_table.heading('attendance', text= 'Attendance')
        self.attendance_table['show'] = 'headings'

        self.attendance_table.column("id", width=100)
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("dep", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("attendance", width=100)

        self.attendance_table.pack(fill= BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)


    # fetch data
    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert('',END, values=i)

    def import_csv(self):
        global my_data
        my_data.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csv_read = csv.reader(myfile, delimiter=',')
            for i in csv_read:
                my_data.append(i)
            self.fetch_data(my_data)

    # export
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("Error", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode='w', newline='') as myfile:
                exp_write = csv.writer(myfile, delimiter=',')
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln)+" successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # cursor
    def get_cursor(self, event = ''):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        row = content['values']
        self.var_id.set(row[0])
        self.var_name.set(row[1])
        self.var_dep.set(row[2])
        self.var_time.set(row[3])
        self.var_date.set(row[4])
        self.var_attendance.set(row[5])

    def reset_data(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_dep.set('')
        self.var_time.set('')
        self.var_date.set('')
        self.var_attendance.set('')




if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()