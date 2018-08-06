import tkinter as tk
import sqlite3

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.config(background='black')
        tk.Label(self, text='Welcome to Worker Management App...', font=font32, fg='white', bg='black').grid(row=1, column=0, columnspan=3,padx=10,pady=10)
        tk.Label(self, text='Choose a category:', font=font32, fg='white', bg='black').grid(row=2, column=0, columnspan=3)
        tk.Button(self, text='1. New Entry', font=font28, fg='white', bg='black',command=lambda:NewEntry(self) ).grid(row=3, column=1, pady=25)
        tk.Button(self, text='2. Details of Existing Worker', font=font28, fg='white', bg='black', command=self.existing).grid(row=4, column=1, pady=25)
        tk.Button(self, text='3. Print Ledger', font=font28, fg='white', bg='black').grid(row=5, column=1, pady=25)

    def savedata(self,b):
        for strvar in string_var_list:
            print(strvar.get())

        cursor.execute('''INSERT INTO users(id, name, fname, address,
                        mobile, idcard, doj, skill, wage, ot)
                    VALUES(?,?,?,?,?,?,?,?,?,?)''',
                       (string_var_list[0].get(), string_var_list[1].get(), string_var_list[2].get(),
                        string_var_list[3].get(),
                        string_var_list[4].get(), string_var_list[5].get(),
                        string_var_list[6].get(), string_var_list[7].get(), string_var_list[8].get(),
                        string_var_list[9].get()))
        name = string_var_list[1].get()
        db1 = sqlite3.connect('databases/'+name+'.db')

        cursor1 = db1.cursor()
        try:
            cursor1.execute('''
             CREATE TABLE '''+name+'''(date TEXT, day INTEGER PRIMARY KEY, intime TEXT, lunchout TEXT, lunchin TEXT, outtime TEXT)
             ''')
            db1.commit()
        except:
            print('User already exists')
        db.commit()
        b.destroy()

    def existing(self):
        namedb = tk.StringVar()
        tk.Label(self, text='Enter name or id: ', font=font16, bg='black',fg='white').place(x=220, y=410)
        e1 = tk.Entry(self, textvariable=namedb)
        e1.place(x=420, y=420)
        e1.focus()
        tk.Button(self, text='Go', bg='black', fg='white', font=font12, command=lambda : Existing(self, namedb.get())).place(x=580, y=410)
