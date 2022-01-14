import multiprocessing#, (test.py)
import tkinter as tk
from tkinter import ttk
import password_generator as pg #think you'll change 
import string
import pyperclip as pc
 
class PasswordManager(tk.Tk):

    
    def __init__(self,*args,**kwargs):
        super(PasswordManager,self).__init__(*args,**kwargs)
        self.title("Password Manager")
        self.geometry("800x600")
        self.password_txt='Hello'
                        
#-----------------password Generator UI---------------------------------


        self.lengthLabel=tk.Label(self,text="Insert password length:",width=20)
        self.lengthLabel.grid(row=0,column=0)
        self.lengthEntry=tk.Entry(self,width=10)
        self.lengthEntry.grid(row=0,column=1,padx=0,sticky=tk.W)
        self.generateButton=tk.Button(self,text="Generate",command=self.generator)
        self.generateButton.grid(row=1,column=1,sticky=tk.W)
        self.generatedPassword=tk.Text(self,width=50,height=1)
        self.generatedPassword.insert('1.0',self.password_txt)
        self.generatedPassword.grid(row=2,column=0,columnspan=4,padx=5,pady=5)
        self.passwordCopyButton=tk.Button(self,text="Copy",command=pc.copy(self.password_txt))
        self.passwordCopyButton.grid(row=2,column=5,sticky=tk.E,padx=5)

#--------to generate password in the entry box-------------------------------------

    def generator(self):
        password_length=(self.lengthEntry.get()).strip()
        try:
            password_length_int=int(password_length)
            self.password_txt=pg.generate_password(password_length_int)
        except ValueError:
            self.password_txt="Insert only numbers!!! Try again!!!!"

        self.generatedPassword.delete('1.0',tk.END)
        self.generatedPassword.insert('1.0',self.password_txt)
        self.generatedPassword.grid(row=2,column=0,columnspan=4,padx=5,pady=5)
        self.passwordCopyButton=tk.Button(self,command=pc.copy(self.password_txt))
#---------------------------------------------------------------------------------

    

if __name__ == '__main__':
    app=PasswordManager()
    app.mainloop()