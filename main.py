import tkinter as tk
from PasswordBackend import *

def generatePassword():
  password = baseLetters()
  if numBool.get() == 'True':
    password += addNumbers()
  if capBool.get() =='True':
    password = capPassword(password)
  if charBool.get() == 'True':
    password += specialChar()

  print(password)

root = tk.Tk()

root.resizable(False, False)
root.title('Password Generator and Validator')
root.columnconfigure(0)
root.rowconfigure(0)


numBool= tk.StringVar()
numbers=tk.Checkbutton(
  root, text="Add numbers", 
  onvalue="True", offvalue="False", variable= numBool
).grid(column=0, row = 0)

capBool= tk.StringVar()
caps=tk.Checkbutton(
  root, text="Capitalize", 
  onvalue="True", offvalue="False", variable= capBool
).grid(column=1, row = 0)

charBool= tk.StringVar()
char=tk.Checkbutton(
  root, text="special character", 
  onvalue="True", offvalue="False", variable= charBool
).grid(column=2, row = 0)

submit=tk.Button(root, text="Generate Password", command=generatePassword
).grid(column=0, row=1)




###     somewhere here has the password output    ###


root.mainloop()