import tkinter
from tkinter import ttk
window= tkinter.Tk() #instantiate and instance of a window
window.title("To DO LIST")
frame=tkinter.Frame(window)
frame.pack()
# Saving User Info
user_info_frame=tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

first_name_label=tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label=tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label=tkinter.Label(user_info_frame,text="Title")
title_combobox=ttk.Combobox(user_info_frame,values=["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2  )


age_label =tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)
window.mainloop()
nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox=ttk.Combobox(user_info_frame,values=["Nigeria","American","Canadian","Itakian"])

nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


# Saving Course Info
courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

registered_label=tkinter.Label(courses_frame,text="Registeration Status")
registered_check=tkinter.Checkbutton(courses_frame,text="Currently Registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)
window.mainloop()
# from tkinter import *
 

# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()